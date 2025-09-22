#!/usr/bin/env python3
"""
FastAPI BVA Scraper API – Optimized
Includes:
 • Full Year→dc mapping (1997–2025, linear fill before 2021)
 • Optimized /analyze/text endpoint (single-pass keyword scanning)
"""

from fastapi import FastAPI, HTTPException, Query, Body
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
import logging, requests, time, asyncio, re
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor
from textstat import flesch_kincaid_grade

# -------------------------------------------------------------------
# Logging
# -------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

# -------------------------------------------------------------------
# FastAPI app
# -------------------------------------------------------------------
app = FastAPI(
    title="BVA Decision Scraper API (No DB)",
    description="Search and fetch Board of Veterans' Appeals decisions – no database required",
    version="1.1.0"
)

executor = ThreadPoolExecutor(max_workers=10)

USER_AGENT = "VetAI-API/1.0"
REQUEST_TIMEOUT = 15
RATE_LIMIT_DELAY = 2  # seconds between requests

# -------------------------------------------------------------------
# Year→dc mapping (verified & linear pre-2021)
# -------------------------------------------------------------------
YEAR_DC_MAP: Dict[int, int] = {
    1997: 9138,
    1998: 9139, 1999: 9140, 2000: 9141, 2001: 9142, 2002: 9143,
    2003: 9144, 2004: 9145, 2005: 9146, 2006: 9147, 2007: 9148,
    2008: 9149, 2009: 9150, 2010: 9151, 2011: 9152, 2012: 9153,
    2013: 9154, 2014: 9155, 2015: 9156, 2016: 9157, 2017: 9158,
    2018: 9159, 2019: 9160, 2020: 9161, 2021: 9162,
    2022: 9256, 2023: 9692, 2024: 10080, 2025: 10280,
}

# -------------------------------------------------------------------
# Pydantic models
# -------------------------------------------------------------------
class SearchRequest(BaseModel):
    query: str
    year: Optional[int] = None
    max_pages: int = Field(1, ge=1, le=20)
    page_size: int = Field(20, ge=10, le=50)

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

class BatchSearchPayload(BaseModel):
    queries: List[str] = Field(..., min_items=1, description="List of search queries")
    year: Optional[int] = Field(None, description="Year filter for all queries")
    max_pages: int = Field(1, ge=1, le=5, description="Max pages per query")

class AnalyzeResponse(BaseModel):
    url: str
    case_number: Optional[str]
    text_length: int
    keyword_counts: Optional[Dict[str, int]]
    keyword_contexts: Optional[Dict[str, List[str]]]
    va_terms_found: Dict[str, int]
    readability_grade: Optional[float]
    analysis_timestamp: str

# -------------------------------------------------------------------
# Regex patterns
# -------------------------------------------------------------------
DATE_RE  = re.compile(r"Decision\s*Date\s*[:\-]\s*([A-Za-z]{3,9}\s+\d{1,2},\s+\d{4})", re.I)
DOCKET_RE= re.compile(r"Docket\s*No\.?\s*[:\-]?\s*([\w\-\s\/]+)", re.I)
OUTCOME_PATTERNS = [
    ("Granted",  re.compile(r"\b(ORDER.*?)(GRANTED)\b", re.I | re.S)),
    ("Denied",   re.compile(r"\b(ORDER.*?)(DENIED)\b",  re.I | re.S)),
    ("Remanded", re.compile(r"\b(REMANDED)\b",         re.I)),
]
ISSUES_RE  = re.compile(r"ISSUES?\s*[:\-]?\s*(.*)", re.I)
CFR_CITATION_RE = re.compile(r"38\s*CFR\s*[§\u00A7]\s*([\d\.]+[a-z0-9\(\)]*)", re.I)
M21_RE     = re.compile(r"M21-1[\w\-\.\s]*", re.I)
RO_RE      = re.compile(r"Regional\s+Office\s+in\s+([A-Za-z\s,]+)", re.I)
JUDGE_RE   = re.compile(r"(Veterans\s+Law\s+Judge|Acting\s+Veterans\s+Law\s+Judge)\s*[:\-]?\s*([A-Z][A-Za-z\s\-\.]+)")

# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------
def parse_decision_text(text: str) -> Dict[str, Any]:
    d = {"decision_date": None, "docket_no": None, "outcome": None,
         "issues": [], "citations": [], "regional_office": None, "judge": None}

    if m := DATE_RE.search(text):
        try:
            d["decision_date"] = datetime.strptime(m.group(1), "%B %d, %Y").strftime("%Y-%m-%d")
        except ValueError:
            pass

    if m := DOCKET_RE.search(text):
        d["docket_no"] = re.sub(r"\s+", " ", m.group(1)).strip()

    upper_txt = text.upper()
    if all(x in upper_txt for x in ["REMANDED", "GRANTED", "DENIED"]):
        d["outcome"] = "Mixed"
    else:
        for label, pat in OUTCOME_PATTERNS:
            if pat.search(text):
                d["outcome"] = label
                break

    if m := ISSUES_RE.search(text):
        items = re.split(r"\s*\d+\.\s*|;|\n", m.group(1).strip())
        d["issues"] = [i.strip() for i in items if i.strip()][:5]

    cfrs  = CFR_CITATION_RE.findall(text)
    m21s  = M21_RE.findall(text)
    d["citations"] = sorted(set([f"38 CFR § {c}" for c in cfrs[:10]] + m21s[:5]))

    if m := RO_RE.search(text):
        d["regional_office"] = m.group(1).strip().rstrip(".")

    if m := JUDGE_RE.search(text):
        d["judge"] = m.group(2).strip()
    return d

def build_search_url(query: str, year: Optional[int]) -> str:
    params = {"affiliate": "bvadecisions", "query": query}
    if year and year in YEAR_DC_MAP:
        params["dc"] = YEAR_DC_MAP[year]
    elif year:
        params["query"] = f"{query} {year}"  # fallback
    return f"https://search.usa.gov/search/docs?{urlencode(params)}"

def search_bva_paginated(query: str, year: Optional[int] = None,
                         max_pages: int = 1, page_size: int = 20) -> List[Dict[str, Any]]:
    all_results: List[Dict[str, Any]] = []
    current_page = 1
    current_url = build_search_url(query, year)
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    while current_page <= max_pages:
        logger.info(f"Fetching page {current_page} for '{query}'")
        try:
            resp = session.get(current_url, timeout=REQUEST_TIMEOUT)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")
            results = soup.find_all("div", class_="result")
            for r in results[:page_size]:
                try:
                    t_elem = r.find("h4", class_="title")
                    s_elem = r.find("span", class_="description")
                    if t_elem and (a := t_elem.find("a")):
                        url = a.get("href", "")
                        title = a.get_text(strip=True)
                        snippet = s_elem.get_text(strip=True) if s_elem else ""
                        case_number = url.split("/")[-1].replace(".txt", "") if ".txt" in url else None
                        year_match = re.search(r"/(19\d{2}|20\d{2})/", url)
                        y = int(year_match.group(1)) if year_match else datetime.now().year
                        all_results.append({
                            "url": url, "title": title, "snippet": snippet,
                            "year": y, "case_number": case_number
                        })
                except Exception as e:
                    logger.debug(f"Parse error: {e}")
            next_link = soup.find("a", string="Next") or soup.find("a", class_="next")
            if next_link and next_link.get("href") and current_page < max_pages:
                href = next_link.get("href")
                current_url = href if href.startswith("http") else f"https://search.usa.gov{href}"
                current_page += 1
                time.sleep(RATE_LIMIT_DELAY)
            else:
                break
        except Exception as e:
            logger.error(f"Error fetching page {current_page}: {e}")
            break
    logger.info(f"Search complete: {len(all_results)} results for '{query}'")
    return all_results

def fetch_case_text(url: str) -> Dict[str, Any]:
    logger.info(f"Fetching case text from {url}")
    s = requests.Session(); s.headers.update({"User-Agent": USER_AGENT})
    resp = s.get(url, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    text = resp.text
    if not text or len(text) < 100:
        raise HTTPException(status_code=422, detail="Invalid or empty case content")
    parsed = parse_decision_text(text)
    year_match = re.search(r"/(19\d{2}|20\d{2})/", url)
    year = int(year_match.group(1)) if year_match else datetime.now().year
    case_number = url.split("/")[-1].replace(".txt", "") if ".txt" in url else None
    return {
        "url": url,
        "year": year,
        "case_number": case_number,
        "raw_text": text,
        "parsed": parsed,
        "text_length": len(text),
        "fetch_timestamp": datetime.now().isoformat()
    }

# -------------------------------------------------------------------
# Endpoints
# -------------------------------------------------------------------
@app.get("/")
async def root():
    return {
        "api": "BVA Decision Scraper (No DB)",
        "version": "1.1.0",
        "endpoints": {
            "/search": "POST - Search BVA decisions",
            "/case": "GET - Fetch specific case by URL",
            "/case/text": "GET - Raw text of a case",
            "/batch/search": "POST - Search multiple queries",
            "/analyze/text": "GET - Analyze decision text",
            "/health": "GET - Health check"
        }
    }

@app.post("/search", response_model=SearchResponse)
async def search_decisions(request: SearchRequest):
    loop = asyncio.get_running_loop()
    results = await loop.run_in_executor(
        executor, search_bva_paginated,
        request.query, request.year, request.max_pages, request.page_size
    )
    return SearchResponse(
        query=request.query,
        total_results=len(results),
        pages_searched=request.max_pages,
        results=[SearchResult(**r) for r in results],
        timestamp=datetime.now().isoformat()
    )

@app.get("/case", response_model=CaseDetail)
async def get_case(url: str = Query(...), full_text: bool = Query(False)):
    loop = asyncio.get_running_loop()
    case_data = await loop.run_in_executor(executor, fetch_case_text, url)
    parsed, text = case_data["parsed"], case_data["raw_text"]
    return CaseDetail(
        url=url,
        year=case_data["year"],
        case_number=case_data["case_number"],
        docket_no=parsed.get("docket_no"),
        decision_date=parsed.get("decision_date"),
        outcome=parsed.get("outcome"),
        judge=parsed.get("judge"),
        regional_office=parsed.get("regional_office"),
        issues=parsed.get("issues"),
        citations=parsed.get("citations"),
        text_length=len(text),
        text_preview=text[:500],
        full_text=text if full_text else None,
        fetch_timestamp=case_data["fetch_timestamp"]
    )

@app.get("/case/text")
async def get_case_text(url: str = Query(...)):
    loop = asyncio.get_running_loop()
    case_data = await loop.run_in_executor(executor, fetch_case_text, url)
    return PlainTextResponse(
        content=case_data["raw_text"],
        media_type="text/plain",
        headers={
            "X-Case-Number": case_data.get("case_number", "unknown"),
            "X-Year": str(case_data.get("year", "unknown")),
            "X-Text-Length": str(case_data.get("text_length", 0))
        }
    )

@app.post("/batch/search", response_model=List[BatchSearchResult])
async def batch_search(payload: BatchSearchPayload = Body(...)):
    queries = [q.strip() for q in payload.queries if q.strip()]
    if not queries:
        raise HTTPException(status_code=422, detail="`queries` cannot be empty.")
    results: List[BatchSearchResult] = []
    loop = asyncio.get_running_loop()
    for q in queries:
        try:
            search_results = await loop.run_in_executor(
                executor, search_bva_paginated, q, payload.year, payload.max_pages, 20
            )
            results.append(BatchSearchResult(
                query=q,
                count=len(search_results),
                urls=[r["url"] for r in search_results[:10]],
                case_numbers=[r["case_number"] for r in search_results[:10] if r.get("case_number")]
            ))
            await asyncio.sleep(RATE_LIMIT_DELAY)
        except Exception as e:
            logger.error(f"Error searching '{q}': {e}")
            results.append(BatchSearchResult(query=q, count=0, urls=[], case_numbers=[]))
    return results

@app.get("/analyze/text", response_model=AnalyzeResponse)
async def analyze_text(
    url: str = Query(...),
    keywords: List[str] = Query([]),
    context: bool = Query(False, description="Return keyword context snippets")
):
    """
    Optimized analysis: pre-normalize text once, single-pass regex for each keyword.
    """
    loop = asyncio.get_running_loop()
    case_data = await loop.run_in_executor(executor, fetch_case_text, url)
    text = case_data["raw_text"]
    text_lower, text_upper = text.lower(), text.upper()

    keyword_counts: Dict[str, int] = {}
    keyword_contexts: Dict[str, List[str]] = {}
    if keywords:
        for k in keywords:
            matches = list(re.finditer(re.escape(k), text, re.IGNORECASE))
            keyword_counts[k] = len(matches)
            if context:
                snippets = []
                for m in matches:
                    start = max(m.start() - 40, 0)
                    end = min(m.end() + 40, len(text))
                    snippets.append(text[start:end])
                keyword_contexts[k] = snippets

    va_terms = {
        "TDIU": text_upper.count("TDIU"),
        "PTSD": text_upper.count("PTSD"),
        "service-connected": text_lower.count("service-connected"),
        "disability rating": text_lower.count("disability rating"),
        "effective date": text_lower.count("effective date"),
        "clear and unmistakable error": text_lower.count("clear and unmistakable error"),
        "individual unemployability": text_lower.count("individual unemployability")
    }

    return AnalyzeResponse(
        url=url,
        case_number=case_data.get("case_number"),
        text_length=len(text),
        keyword_counts=keyword_counts or None,
        keyword_contexts=keyword_contexts or None if context else None,
        va_terms_found=va_terms,
        readability_grade=flesch_kincaid_grade(text),
        analysis_timestamp=datetime.now().isoformat()
    )

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "BVA Scraper API (No DB)"
    }

# -------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
