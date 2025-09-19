#!/usr/bin/env python3
"""
FastAPI BVA Scraper API - No Database Version
Provides endpoints to search and fetch BVA decisions without any database dependencies.
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
import logging
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor
import re

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="BVA Decision Scraper API (No DB)",
    description="API for searching and fetching Board of Veterans' Appeals decisions - No database required",
    version="1.0.0"
)

# Thread pool for async operations
executor = ThreadPoolExecutor(max_workers=10)

# Configuration
USER_AGENT = "VetAI-API/1.0"
REQUEST_TIMEOUT = 15
RATE_LIMIT_DELAY = 2  # seconds between requests

# Pydantic models
class SearchRequest(BaseModel):
    query: str = Field(..., description="Search query (e.g., 'TDIU', 'PTSD')")
    year: Optional[int] = Field(None, description="Filter by year")
    max_pages: int = Field(1, ge=1, le=20, description="Maximum pages to search")
    page_size: int = Field(20, ge=10, le=50, description="Results per page")

class SearchResult(BaseModel):
    url: str
    title: str
    snippet: str
    year: int
    case_number: Optional[str]

class SearchResponse(BaseModel):
    query: str
    total_results: int
    pages_searched: int
    results: List[SearchResult]
    timestamp: str

class CaseDetail(BaseModel):
    url: str
    year: int
    case_number: Optional[str]
    docket_no: Optional[str]
    decision_date: Optional[str]
    outcome: Optional[str]
    judge: Optional[str]
    regional_office: Optional[str]
    issues: Optional[List[str]]
    citations: Optional[List[str]]
    text_length: int
    text_preview: str
    full_text: Optional[str]
    fetch_timestamp: str

class BatchSearchResult(BaseModel):
    query: str
    count: int
    urls: List[str]
    case_numbers: List[str]

# Parsing patterns (from original r.py)
DATE_RE = re.compile(r"Decision\s*Date\s*[:\-]\s*([A-Za-z]{3,9}\s+\d{1,2},\s+\d{4})", re.I)
DOCKET_RE = re.compile(r"Docket\s*No\.?\s*[:\-]?\s*([\w\-\s\/]+)", re.I)
OUTCOME_PATTERNS = [
    ("Granted", re.compile(r"\b(ORDER.*?)(GRANTED)\b", re.I | re.S)),
    ("Denied", re.compile(r"\b(ORDER.*?)(DENIED)\b", re.I | re.S)),
    ("Remanded", re.compile(r"\b(REMANDED)\b", re.I)),
]
ISSUES_RE = re.compile(r"ISSUES?\s*[:\-]?\s*(.*)", re.I)
CFR_CITATION_RE = re.compile(r"38\s*CFR\s*[§\u00A7]\s*([\d\.]+[a-z0-9\(\)]*)", re.I)
M21_RE = re.compile(r"M21-1[\w\-\.\s]*", re.I)
RO_RE = re.compile(r"Regional\s+Office\s+in\s+([A-Za-z\s,]+)", re.I)
JUDGE_RE = re.compile(r"(Veterans\s+Law\s+Judge|Acting\s+Veterans\s+Law\s+Judge)\s*[:\-]?\s*([A-Z][A-Za-z\s\-\.]+)")

# Helper functions
def parse_decision_text(text: str) -> Dict[str, Any]:
    """Parse BVA decision text to extract metadata."""
    d = {
        "decision_date": None,
        "docket_no": None,
        "outcome": None,
        "issues": [],
        "citations": [],
        "regional_office": None,
        "judge": None,
    }

    # Decision Date
    m = DATE_RE.search(text)
    if m:
        try:
            from datetime import datetime
            d["decision_date"] = datetime.strptime(m.group(1), "%B %d, %Y").strftime("%Y-%m-%d")
        except ValueError:
            pass

    # Docket
    m = DOCKET_RE.search(text)
    if m:
        d["docket_no"] = re.sub(r"\s+", " ", m.group(1)).strip()

    # Outcome
    upper_txt = text.upper()
    if "REMANDED" in upper_txt and "GRANTED" in upper_txt and "DENIED" in upper_txt:
        d["outcome"] = "Mixed"
    else:
        for label, pat in OUTCOME_PATTERNS:
            if pat.search(text):
                d["outcome"] = label
                break

    # Issues
    m = ISSUES_RE.search(text)
    if m:
        issues_line = m.group(1).strip()
        items = re.split(r"\s*\d+\.\s*|;|\n", issues_line)
        d["issues"] = [i.strip() for i in items if i.strip()][:5]  # Limit to 5

    # Citations
    cfrs = CFR_CITATION_RE.findall(text)
    m21s = M21_RE.findall(text)
    d["citations"] = sorted(set([f"38 CFR § {c}" for c in cfrs[:10]] + m21s[:5]))  # Limit

    # Regional Office
    m = RO_RE.search(text)
    if m:
        d["regional_office"] = m.group(1).strip().rstrip(".")

    # Judge
    m = JUDGE_RE.search(text)
    if m:
        d["judge"] = m.group(2).strip()

    return d

def search_bva_paginated(
    query: str,
    year: Optional[int] = None,
    max_pages: int = 1,
    page_size: int = 20
) -> List[Dict[str, Any]]:
    """
    Search BVA decisions with pagination.
    """
    all_results = []
    current_page = 1

    # Build initial search URL
    search_params = {
        'affiliate': 'bvadecisions',
        'query': f"{query} {year}" if year else query
    }

    base_url = "https://search.usa.gov/search"
    current_url = f"{base_url}?{urlencode(search_params)}"

    session = requests.Session()
    session.headers.update({'User-Agent': USER_AGENT})

    while current_page <= max_pages:
        logger.info(f"Fetching search page {current_page} for query: {query}")

        try:
            resp = session.get(current_url, timeout=REQUEST_TIMEOUT)
            resp.raise_for_status()

            soup = BeautifulSoup(resp.text, 'html.parser')
            results = soup.find_all('div', class_='result')

            for result in results[:page_size]:
                try:
                    # Extract data
                    title_elem = result.find('h4', class_='title')
                    snippet_elem = result.find('span', class_='description')

                    if title_elem:
                        link_elem = title_elem.find('a')
                        if link_elem:
                            url = link_elem.get('href', '')
                            title = link_elem.get_text(strip=True)
                            snippet = snippet_elem.get_text(strip=True) if snippet_elem else ""

                            # Extract case number from URL
                            case_number = url.split('/')[-1].replace('.txt', '') if '.txt' in url else None

                            # Extract year
                            year_match = re.search(r'/(19\d{2}|20\d{2})/', url)
                            extracted_year = int(year_match.group(1)) if year_match else datetime.now().year

                            all_results.append({
                                'url': url,
                                'title': title,
                                'snippet': snippet,
                                'year': extracted_year,
                                'case_number': case_number
                            })

                except Exception as e:
                    logger.debug(f"Error parsing result: {e}")
                    continue

            # Check for next page
            next_link = soup.find('a', string='Next') or soup.find('a', class_='next')
            if next_link and next_link.get('href') and current_page < max_pages:
                next_href = next_link.get('href')
                if next_href.startswith('http'):
                    current_url = next_href
                else:
                    current_url = f"https://search.usa.gov{next_href}"
                current_page += 1
                time.sleep(RATE_LIMIT_DELAY)  # Rate limiting
            else:
                break

        except Exception as e:
            logger.error(f"Error fetching page {current_page}: {e}")
            break

    logger.info(f"Search complete: Found {len(all_results)} results for '{query}'")
    return all_results

def fetch_case_text(url: str) -> Dict[str, Any]:
    """
    Fetch the full text of a BVA decision.
    """
    logger.info(f"Fetching case text from: {url}")

    session = requests.Session()
    session.headers.update({'User-Agent': USER_AGENT})

    try:
        resp = session.get(url, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()

        text = resp.text
        if not text or len(text) < 100:
            raise HTTPException(status_code=422, detail="Invalid or empty case content")

        # Parse the decision
        parsed = parse_decision_text(text)

        # Extract year from URL
        year_match = re.search(r'/(19\d{2}|20\d{2})/', url)
        year = int(year_match.group(1)) if year_match else datetime.now().year

        # Extract case number
        case_number = url.split('/')[-1].replace('.txt', '') if '.txt' in url else None

        return {
            'url': url,
            'year': year,
            'case_number': case_number,
            'raw_text': text,
            'parsed': parsed,
            'text_length': len(text),
            'fetch_timestamp': datetime.now().isoformat()
        }

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail="Case not found")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching case: {str(e)}")

# API Endpoints
@app.get("/")
async def root():
    """API root endpoint with basic info."""
    return {
        "api": "BVA Decision Scraper (No Database)",
        "version": "1.0.0",
        "description": "Search and fetch BVA decisions without database storage",
        "endpoints": {
            "/search": "Search BVA decisions",
            "/case": "Fetch specific case by URL",
            "/case/text": "Get raw text of a case",
            "/batch/search": "Search multiple queries",
            "/docs": "Interactive API documentation"
        }
    }

@app.post("/search", response_model=SearchResponse)
async def search_decisions(request: SearchRequest):
    """
    Search BVA decisions with optional year filter and pagination.
    """
    logger.info(f"Search request: query='{request.query}', year={request.year}, pages={request.max_pages}")

    try:
        # Run search in thread pool
        loop = asyncio.get_event_loop()
        results = await loop.run_in_executor(
            executor,
            search_bva_paginated,
            request.query,
            request.year,
            request.max_pages,
            request.page_size
        )

        # Convert to response model
        search_results = [SearchResult(**r) for r in results]

        return SearchResponse(
            query=request.query,
            total_results=len(search_results),
            pages_searched=request.max_pages,
            results=search_results,
            timestamp=datetime.now().isoformat()
        )

    except Exception as e:
        logger.error(f"Search error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/case", response_model=CaseDetail)
async def get_case(
    url: str = Query(..., description="URL of the BVA decision"),
    full_text: bool = Query(False, description="Include full text in response")
):
    """
    Fetch a specific BVA decision by URL.
    """
    logger.info(f"Case request: url={url}, full_text={full_text}")

    try:
        # Fetch in thread pool
        loop = asyncio.get_event_loop()
        case_data = await loop.run_in_executor(
            executor,
            fetch_case_text,
            url
        )

        parsed = case_data['parsed']
        text = case_data['raw_text']

        return CaseDetail(
            url=url,
            year=case_data['year'],
            case_number=case_data['case_number'],
            docket_no=parsed.get('docket_no'),
            decision_date=parsed.get('decision_date'),
            outcome=parsed.get('outcome'),
            judge=parsed.get('judge'),
            regional_office=parsed.get('regional_office'),
            issues=parsed.get('issues'),
            citations=parsed.get('citations'),
            text_length=len(text),
            text_preview=text[:500] if text else "",
            full_text=text if full_text else None,
            fetch_timestamp=case_data['fetch_timestamp']
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Case fetch error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/case/text")
async def get_case_text(
    url: str = Query(..., description="URL of the BVA decision")
):
    """
    Get the raw text of a BVA decision.
    """
    logger.info(f"Text request: url={url}")

    try:
        loop = asyncio.get_event_loop()
        case_data = await loop.run_in_executor(
            executor,
            fetch_case_text,
            url
        )

        return PlainTextResponse(
            content=case_data['raw_text'],
            media_type="text/plain",
            headers={
                "X-Case-Number": case_data.get('case_number', 'unknown'),
                "X-Year": str(case_data.get('year', 'unknown')),
                "X-Text-Length": str(case_data.get('text_length', 0))
            }
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Text fetch error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/batch/search", response_model=List[BatchSearchResult])
async def batch_search(
    queries: List[str] = Query(..., description="List of search queries"),
    year: Optional[int] = Query(None, description="Year filter for all queries"),
    max_pages: int = Query(1, ge=1, le=5, description="Max pages per query")
):
    """
    Search for multiple queries and return results for each.
    """
    logger.info(f"Batch search: {len(queries)} queries, year={year}")

    results = []

    for query in queries:
        try:
            # Search with limited pages for batch operations
            search_results = search_bva_paginated(query, year, max_pages, 20)

            results.append(BatchSearchResult(
                query=query,
                count=len(search_results),
                urls=[r['url'] for r in search_results[:10]],  # First 10 URLs
                case_numbers=[r['case_number'] for r in search_results[:10] if r.get('case_number')]
            ))

            # Rate limiting between queries
            await asyncio.sleep(RATE_LIMIT_DELAY)

        except Exception as e:
            logger.error(f"Error searching '{query}': {e}")
            results.append(BatchSearchResult(
                query=query,
                count=0,
                urls=[],
                case_numbers=[]
            ))

    return results

@app.get("/analyze/text")
async def analyze_text(
    url: str = Query(..., description="URL of the BVA decision"),
    keywords: List[str] = Query([], description="Keywords to search for in the text")
):
    """
    Analyze a BVA decision text for specific keywords and patterns.
    """
    logger.info(f"Analyze request: url={url}, keywords={keywords}")

    try:
        # Fetch the case
        loop = asyncio.get_event_loop()
        case_data = await loop.run_in_executor(
            executor,
            fetch_case_text,
            url
        )

        text = case_data['raw_text']
        parsed = case_data['parsed']

        # Analyze keywords
        keyword_counts = {}
        for keyword in keywords:
            keyword_counts[keyword] = text.lower().count(keyword.lower())

        # Common VA terms analysis
        va_terms = {
            "TDIU": text.upper().count("TDIU"),
            "PTSD": text.upper().count("PTSD"),
            "service-connected": text.lower().count("service-connected"),
            "disability rating": text.lower().count("disability rating"),
            "effective date": text.lower().count("effective date"),
            "clear and unmistakable error": text.lower().count("clear and unmistakable error"),
            "individual unemployability": text.lower().count("individual unemployability")
        }

        return {
            "url": url,
            "case_number": case_data.get('case_number'),
            "text_length": len(text),
            "parsed_metadata": parsed,
            "keyword_counts": keyword_counts if keywords else None,
            "va_terms_found": va_terms,
            "analysis_timestamp": datetime.now().isoformat()
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Analysis error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "BVA Scraper API (No DB)"
    }

# Run with: uvicorn api_no_db:app --reload --host 0.0.0.0 --port 8001
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)