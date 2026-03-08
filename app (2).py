#!/usr/bin/env python3
"""
FastAPI BVA Scraper API – Optimized
Includes:
 • Full Year→dc mapping (1997–2025, linear fill before 2021)
 • Optimized /analyze/text endpoint (single-pass keyword scanning)
 • Improved parsing for dates, citations, judges, and issues
"""

from fastapi import FastAPI, HTTPException, Query, Body
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator
from typing import Optional, List, Dict, Any
from datetime import datetime
import logging, requests, time, asyncio, re
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor
from textstat import flesch_kincaid_grade
from requests.exceptions import RequestException, Timeout, HTTPError

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
    version="1.3.0"
)

# Add CORS middleware to allow browser access to API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
    query: str = Field(..., min_length=1, description="Search query (supports AND/OR/NOT operators and quoted phrases)")
    year: Optional[int] = Field(None, ge=1997, le=2025, description="Filter by single year (1997-2025)")
    year_start: Optional[int] = Field(None, ge=1997, le=2025, description="Filter by year range start (1997-2025)")
    year_end: Optional[int] = Field(None, ge=1997, le=2025, description="Filter by year range end (1997-2025)")
    max_pages: int = Field(1, ge=1, le=20)
    page_size: int = Field(20, ge=10, le=50)

    # Filtering parameters
    filter_outcome: Optional[str] = Field(None, description="Filter by outcome: granted, denied, remanded, mixed")
    filter_judge: Optional[str] = Field(None, description="Filter by judge name (partial match)")
    filter_regional_office: Optional[str] = Field(None, description="Filter by regional office (partial match)")
    filter_date_start: Optional[str] = Field(None, description="Filter by decision date >= this (YYYY-MM-DD)")
    filter_date_end: Optional[str] = Field(None, description="Filter by decision date <= this (YYYY-MM-DD)")

    # Sorting parameters
    sort_by: Optional[str] = Field(None, description="Sort by: date, relevance, case_number, text_length, year")
    sort_order: Optional[str] = Field("desc", description="Sort order: asc or desc")

    # Enhancement flags
    highlight_keywords: bool = Field(False, description="Highlight search keywords in snippets")
    include_facets: bool = Field(False, description="Include faceted counts in response")

    @field_validator('query')
    @classmethod
    def query_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError('Query cannot be empty or whitespace only')
        return v.strip()

    @field_validator('filter_outcome')
    @classmethod
    def validate_outcome(cls, v: Optional[str]) -> Optional[str]:
        if v and v.lower() not in ['granted', 'denied', 'remanded', 'mixed']:
            raise ValueError('outcome must be one of: granted, denied, remanded, mixed')
        return v.lower() if v else None

    @field_validator('sort_by')
    @classmethod
    def validate_sort_by(cls, v: Optional[str]) -> Optional[str]:
        if v and v.lower() not in ['date', 'relevance', 'case_number', 'text_length', 'year']:
            raise ValueError('sort_by must be one of: date, relevance, case_number, text_length, year')
        return v.lower() if v else None

    @field_validator('sort_order')
    @classmethod
    def validate_sort_order(cls, v: Optional[str]) -> str:
        if v and v.lower() not in ['asc', 'desc']:
            raise ValueError('sort_order must be asc or desc')
        return v.lower() if v else 'desc'

class SearchResult(BaseModel):
    url: str
    title: str
    snippet: str
    year: int
    case_number: Optional[str]
    highlighted_snippet: Optional[str] = None
    # Metadata fields (populated when filtering is enabled)
    outcome: Optional[str] = None
    judge: Optional[str] = None
    regional_office: Optional[str] = None
    decision_date: Optional[str] = None
    docket_no: Optional[str] = None
    issues: Optional[List[str]] = None
    citations: Optional[List[str]] = None
    text_length: Optional[int] = None

class SearchFacets(BaseModel):
    outcomes: Dict[str, int]
    years: Dict[int, int]
    judges: Dict[str, int]
    regional_offices: Dict[str, int]

class SearchResponse(BaseModel):
    query: str
    processed_query: Optional[str] = None
    total_results: int
    pages_searched: int
    results: List[SearchResult]
    facets: Optional[SearchFacets] = None
    filters_applied: Optional[Dict[str, Any]] = None
    sort_applied: Optional[Dict[str, str]] = None
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
    queries: List[str] = Field(..., min_length=1, description="List of search queries")
    year: Optional[int] = Field(None, ge=1997, le=2025, description="Year filter for all queries (1997-2025)")
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
# Multiple date formats: "December 19, 2024", "12/19/24", "12/19/2024"
DATE_PATTERNS = [
    re.compile(r"Decision\s*Date\s*[:\-]\s*([A-Za-z]{3,9}\s+\d{1,2},\s+\d{4})", re.I),
    re.compile(r"DATE:\s*([A-Za-z]{3,9}\s+\d{1,2},\s+\d{4})", re.I),
    re.compile(r"Decision\s*Date\s*[:\-]\s*(\d{1,2}/\d{1,2}/\d{2,4})", re.I),
]
# Stop docket at DATE, newline, or non-docket chars
DOCKET_RE = re.compile(r"DOCKET\s*NO\.?\s*[:\-]?\s*([\d\-]+)", re.I)
OUTCOME_PATTERNS = [
    ("Granted",  re.compile(r"\bORDER\b.*?\b(is\s+)?GRANTED\b", re.I | re.S)),
    ("Denied",   re.compile(r"\bORDER\b.*?\b(is\s+)?DENIED\b",  re.I | re.S)),
    ("Remanded", re.compile(r"\b(is\s+)?REMANDED\b", re.I)),
]
# Issues: capture lines after ISSUE(S) header until next section
ISSUES_RE = re.compile(r"ISSUES?\s*\n+(.*?)(?=\n\s*(?:FINDING|REPRESENTATION|WITNESS|ATTORNEY|CONCLUSION|\Z))", re.I | re.S)
# CFR: support both "38 CFR" and "38 C.F.R." formats
CFR_CITATION_RE = re.compile(r"38\s*C?\.?F?\.?R?\.?\s*[§\u00A7§]?\s*[§\u00A7]?\s*([\d]+\.[\d]+[a-z0-9\(\)]*)", re.I)
M21_RE = re.compile(r"M21-1[\w\-\.\s]*", re.I)
RO_RE = re.compile(r"Regional\s+Office\s+in\s+([A-Za-z\s,]+?)(?:\.|,?\s*(?:in|has|the|$))", re.I)
# Judge: capture name after title, stop at newline or common endings
JUDGE_RE = re.compile(r"(?:Veterans\s+Law\s+Judge|Acting\s+Veterans\s+Law\s+Judge)[,:\s]+([A-Z][a-zA-Z\.\s\-]+?)(?:\n|,\s*(?:Chair|Member)|$)", re.I)

# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------
def parse_decision_text(text: str) -> Dict[str, Any]:
    """Parse BVA decision text to extract structured metadata."""
    d = {"decision_date": None, "docket_no": None, "outcome": None,
         "issues": [], "citations": [], "regional_office": None, "judge": None}

    # Try multiple date formats
    for date_pattern in DATE_PATTERNS:
        if m := date_pattern.search(text):
            date_str = m.group(1)
            try:
                # Try full month format: "December 19, 2024"
                d["decision_date"] = datetime.strptime(date_str, "%B %d, %Y").strftime("%Y-%m-%d")
                break
            except ValueError:
                try:
                    # Try MM/DD/YYYY format
                    d["decision_date"] = datetime.strptime(date_str, "%m/%d/%Y").strftime("%Y-%m-%d")
                    break
                except ValueError:
                    try:
                        # Try MM/DD/YY format
                        d["decision_date"] = datetime.strptime(date_str, "%m/%d/%y").strftime("%Y-%m-%d")
                        break
                    except ValueError:
                        continue

    # Extract docket number (just the number part)
    if m := DOCKET_RE.search(text):
        d["docket_no"] = m.group(1).strip()

    # Determine outcome from ORDER section
    upper_txt = text.upper()
    # Check the ORDER section specifically for more accurate outcome detection
    order_section = re.search(r"ORDER\s*(.*?)(?=FINDING|REMAND|CONCLUSION|\Z)", text, re.I | re.S)
    if order_section:
        order_text = order_section.group(1).upper()
        has_granted = "GRANTED" in order_text
        has_denied = "DENIED" in order_text
        has_remanded = "REMANDED" in order_text or "REMANDED" in upper_txt[:2000]

        if sum([has_granted, has_denied, has_remanded]) > 1:
            d["outcome"] = "Mixed"
        elif has_granted:
            d["outcome"] = "Granted"
        elif has_denied:
            d["outcome"] = "Denied"
        elif has_remanded:
            d["outcome"] = "Remanded"
    else:
        # Fallback to simple pattern matching
        for label, pat in OUTCOME_PATTERNS:
            if pat.search(text):
                d["outcome"] = label
                break

    # Extract issues - look for "Entitlement to..." patterns
    issue_patterns = re.findall(r"(Entitlement\s+to\s+[^\.]+\.)", text, re.I)
    if issue_patterns:
        # Clean and deduplicate
        seen = set()
        issues = []
        for issue in issue_patterns[:10]:
            clean = re.sub(r"\s+", " ", issue).strip()
            if clean not in seen and len(clean) > 20:
                seen.add(clean)
                issues.append(clean)
        d["issues"] = issues[:5]
    elif m := ISSUES_RE.search(text):
        # Fallback to ISSUES section parsing
        items = re.split(r"\s*\d+\.\s*|\n", m.group(1).strip())
        d["issues"] = [re.sub(r"\s+", " ", i).strip() for i in items if i.strip() and len(i.strip()) > 10][:5]

    # Extract citations - support both "38 CFR" and "38 C.F.R."
    cfrs = CFR_CITATION_RE.findall(text)
    m21s = M21_RE.findall(text)
    d["citations"] = sorted(set([f"38 C.F.R. § {c}" for c in cfrs[:10]] + [m.strip() for m in m21s[:5]]))

    # Extract regional office
    if m := RO_RE.search(text):
        ro = m.group(1).strip().rstrip(".,")
        # Clean up common suffixes
        ro = re.sub(r"\s+(in|has|the)$", "", ro, flags=re.I)
        if len(ro) > 3:
            d["regional_office"] = ro

    # Extract judge name
    if m := JUDGE_RE.search(text):
        judge = m.group(1).strip().rstrip(".,")
        # Filter out non-name captures
        if judge and not judge.upper().startswith("BOARD") and len(judge) > 3:
            d["judge"] = judge

    return d

def extract_year_from_url(url: str) -> int:
    """Extract year from BVA decision URL.

    URLs follow pattern: https://www.va.gov/vetapp{YY}/Files{N}/{case}.txt
    e.g., https://www.va.gov/vetapp24/Files12/A24085357.txt -> 2024
    """
    # Try vetapp{YY} format first (most common)
    vetapp_match = re.search(r"/vetapp(\d{2})/", url)
    if vetapp_match:
        yy = int(vetapp_match.group(1))
        return 2000 + yy if yy < 50 else 1900 + yy

    # Fallback: try to find 4-digit year in path
    year_match = re.search(r"/(19\d{2}|20\d{2})/", url)
    if year_match:
        return int(year_match.group(1))

    # Last resort: try to extract from case number (e.g., A24085357 -> 2024)
    case_match = re.search(r"/[A-Za-z]?(\d{2})\d+\.txt", url)
    if case_match:
        yy = int(case_match.group(1))
        return 2000 + yy if yy < 50 else 1900 + yy

    return datetime.now().year


def normalize_snippet(text: str) -> str:
    """Normalize snippet text by fixing whitespace issues from HTML parsing."""
    if not text:
        return ""
    # Replace multiple whitespace with single space
    text = re.sub(r"\s+", " ", text)
    # Fix common concatenation issues from HTML parsing
    # Pattern: common words followed directly by capitalized word
    # e.g., "TheVeteran" -> "The Veteran", "forPTSD" -> "for PTSD"
    text = re.sub(r"([Tt]he|[Ff]or|[Aa]nd|[Oo]r|[Tt]o|[Oo]f|[Ii]n|[Ii]s|[Aa]s|[Bb]y|[Oo]n|[Aa]t|[Aa]n?)([A-Z][a-z]+)", r"\1 \2", text)
    # Fix acronym concatenation: "forPTSD" -> "for PTSD"
    text = re.sub(r"([a-z])([A-Z]{2,})", r"\1 \2", text)
    # Fix "PTSDis" -> "PTSD is", "Veteranis" -> "Veteran is" patterns
    text = re.sub(r"([A-Za-z]{3,})(is|are|was|were|has|have|had|from|with|and|or|not)\b", r"\1 \2", text)
    # Fix "percent for" -> "percent for" (lowercase after number words)
    text = re.sub(r"(percent|rating|granted|denied|remanded)([a-z])", r"\1 \2", text)
    return text.strip()


def preprocess_query(query: str) -> str:
    """
    Translate boolean operators to USA.gov search syntax.

    Supports:
    - AND (implicit in USA.gov, removed)
    - OR (kept as-is, supported by USA.gov)
    - NOT (converted to - prefix)
    - Quoted phrases (preserved for exact matching)

    Args:
        query: User query with optional AND/OR/NOT operators

    Returns:
        Preprocessed query for USA.gov search

    Examples:
        "PTSD AND combat" -> "PTSD combat"
        "PTSD OR depression" -> "PTSD OR depression"
        "PTSD NOT TBI" -> "PTSD -TBI"
        '"service connected"' -> '"service connected"'
    """
    if not query:
        return query

    # Step 1: Extract and protect quoted phrases
    quoted_phrases = []
    phrase_pattern = re.compile(r'"([^"]+)"')

    def save_phrase(match):
        quoted_phrases.append(match.group(0))  # Keep quotes
        return f"__PHRASE_{len(quoted_phrases)-1}__"

    processed = phrase_pattern.sub(save_phrase, query)

    # Step 2: Handle NOT operator (convert to - prefix)
    # Match "NOT word" and convert to "-word"
    # Handle both standalone NOT and within parentheses
    processed = re.sub(r'\bNOT\s+(\S+)', r'-\1', processed, flags=re.IGNORECASE)

    # Step 3: Remove AND operator (implicit in USA.gov)
    # Replace " AND " with just a space
    processed = re.sub(r'\s+AND\s+', ' ', processed, flags=re.IGNORECASE)

    # Step 4: Keep OR as-is (supported by USA.gov)
    # Normalize OR to uppercase for consistency
    processed = re.sub(r'\bor\b', 'OR', processed, flags=re.IGNORECASE)

    # Step 5: Restore quoted phrases
    for i, phrase in enumerate(quoted_phrases):
        processed = processed.replace(f"__PHRASE_{i}__", phrase)

    # Step 6: Clean up extra whitespace
    processed = re.sub(r'\s+', ' ', processed).strip()

    return processed


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
                        snippet = normalize_snippet(s_elem.get_text(strip=True) if s_elem else "")
                        case_number = url.split("/")[-1].replace(".txt", "") if ".txt" in url else None
                        # Use improved year extraction
                        y = extract_year_from_url(url)
                        # Improve title: use case number if title is just filename
                        if title.endswith(".txt") and case_number:
                            title = f"Citation Nr: {case_number}"
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
        except Timeout:
            logger.error(f"Timeout fetching page {current_page}")
            break
        except RequestException as e:
            logger.error(f"Network error fetching page {current_page}: {e}")
            break
        except Exception as e:
            logger.error(f"Error fetching page {current_page}: {e}")
            break
    logger.info(f"Search complete: {len(all_results)} results for '{query}'")
    return all_results

def search_multi_year(query: str, year_start: int, year_end: int,
                      max_pages: int = 1, page_size: int = 20) -> List[Dict[str, Any]]:
    """
    Search across multiple years and aggregate results.

    Args:
        query: Search query
        year_start: Start year (inclusive)
        year_end: End year (inclusive)
        max_pages: Max pages total (distributed across years)
        page_size: Results per page

    Returns:
        Deduplicated list of search results from all years
    """
    if year_start > year_end:
        year_start, year_end = year_end, year_start

    # Limit year range to 5 years max
    if year_end - year_start + 1 > 5:
        logger.warning(f"Year range too large ({year_start}-{year_end}), limiting to 5 years")
        year_end = year_start + 4

    years = list(range(year_start, year_end + 1))
    num_years = len(years)

    # Distribute page limit across years
    pages_per_year = max(1, max_pages // num_years)
    logger.info(f"Searching {num_years} years ({year_start}-{year_end}), {pages_per_year} pages per year")

    all_results = []
    seen_urls = set()

    for year in years:
        try:
            results = search_bva_paginated(query, year, pages_per_year, page_size)
            # Deduplicate by URL
            for r in results:
                if r["url"] not in seen_urls:
                    seen_urls.add(r["url"])
                    all_results.append(r)
        except Exception as e:
            logger.error(f"Error searching year {year}: {e}")
            continue

    logger.info(f"Multi-year search complete: {len(all_results)} unique results")
    return all_results

def sort_results(results: List[Dict[str, Any]], sort_by: Optional[str] = None,
                 order: str = "desc") -> List[Dict[str, Any]]:
    """
    Sort search results by specified field.

    Args:
        results: List of search results
        sort_by: Field to sort by (date|relevance|case_number|text_length)
        order: Sort order (asc|desc)

    Returns:
        Sorted list of results
    """
    if not sort_by or sort_by == "relevance":
        return results  # Preserve USA.gov order

    reverse = (order == "desc")

    if sort_by == "date":
        # Sort by decision_date if available, otherwise by year
        return sorted(results,
                     key=lambda x: x.get("decision_date") or f"{x.get('year', 0):04d}-01-01",
                     reverse=reverse)
    elif sort_by == "case_number":
        return sorted(results,
                     key=lambda x: x.get("case_number") or "",
                     reverse=reverse)
    elif sort_by == "text_length":
        return sorted(results,
                     key=lambda x: x.get("text_length") or 0,
                     reverse=reverse)
    elif sort_by == "year":
        return sorted(results,
                     key=lambda x: x.get("year") or 0,
                     reverse=reverse)

    return results

def apply_filters(results: List[Dict[str, Any]],
                  outcome: Optional[str] = None,
                  judge: Optional[str] = None,
                  regional_office: Optional[str] = None,
                  date_start: Optional[str] = None,
                  date_end: Optional[str] = None,
                  executor_pool=None) -> List[Dict[str, Any]]:
    """
    Filter search results by metadata.

    Requires fetching full case text for each result to extract metadata.
    Uses parallel fetching for performance.

    Args:
        results: List of search results
        outcome: Filter by outcome (granted|denied|remanded|mixed)
        judge: Filter by judge name (partial match, case-insensitive)
        regional_office: Filter by regional office (partial match, case-insensitive)
        date_start: Filter by decision date >= this (YYYY-MM-DD)
        date_end: Filter by decision date <= this (YYYY-MM-DD)
        executor_pool: ThreadPoolExecutor for parallel fetching

    Returns:
        Filtered list of results with metadata populated
    """
    if not any([outcome, judge, regional_office, date_start, date_end]):
        return results  # No filters applied

    # Warn if too many results
    if len(results) > 50:
        logger.warning(f"Filtering {len(results)} results may be slow. Consider narrowing search first.")

    # Limit to first 50 results for filtering to prevent excessive fetching
    results_to_filter = results[:50]

    filtered = []

    # Fetch case details for all results (in parallel if executor provided)
    def fetch_and_filter(result):
        try:
            case_data = fetch_case_text(result["url"])
            parsed = case_data["parsed"]

            # Create enriched result with metadata
            enriched = {**result}
            enriched["outcome"] = parsed.get("outcome")
            enriched["judge"] = parsed.get("judge")
            enriched["regional_office"] = parsed.get("regional_office")
            enriched["decision_date"] = parsed.get("decision_date")
            enriched["docket_no"] = parsed.get("docket_no")
            enriched["issues"] = parsed.get("issues")
            enriched["citations"] = parsed.get("citations")
            enriched["text_length"] = case_data.get("text_length")

            # Apply filters
            if outcome and (not enriched.get("outcome") or enriched["outcome"].lower() != outcome.lower()):
                return None
            if judge and (not enriched.get("judge") or judge.lower() not in enriched["judge"].lower()):
                return None
            if regional_office and (not enriched.get("regional_office") or
                                   regional_office.lower() not in enriched["regional_office"].lower()):
                return None
            if date_start and (not enriched.get("decision_date") or enriched["decision_date"] < date_start):
                return None
            if date_end and (not enriched.get("decision_date") or enriched["decision_date"] > date_end):
                return None

            return enriched

        except Exception as e:
            logger.debug(f"Error filtering {result.get('url')}: {e}")
            return None

    # Use parallel fetching if executor provided
    if executor_pool:
        from concurrent.futures import as_completed
        futures = [executor_pool.submit(fetch_and_filter, r) for r in results_to_filter]
        for future in as_completed(futures):
            result = future.result()
            if result:
                filtered.append(result)
    else:
        # Sequential fetching (fallback)
        for result in results_to_filter:
            enriched = fetch_and_filter(result)
            if enriched:
                filtered.append(enriched)

    logger.info(f"Filtering complete: {len(filtered)}/{len(results_to_filter)} results matched filters")
    return filtered

def highlight_keywords(snippet: str, query: str) -> str:
    """
    Highlight search keywords in snippet using markdown bold.

    Args:
        snippet: Text snippet to highlight
        query: Original search query

    Returns:
        Snippet with keywords wrapped in **bold**

    Example:
        "The Veteran has PTSD" -> "The Veteran has **PTSD**"
    """
    if not snippet or not query:
        return snippet

    # Extract keywords from query (remove boolean operators and quotes)
    keywords = query
    # Remove boolean operators
    keywords = re.sub(r'\b(AND|OR|NOT)\b', ' ', keywords, flags=re.IGNORECASE)
    # Remove quotes
    keywords = keywords.replace('"', '')
    # Remove minus signs
    keywords = keywords.replace('-', ' ')
    # Split into words
    words = [w.strip() for w in keywords.split() if w.strip() and len(w.strip()) > 2]

    highlighted = snippet
    for word in words:
        # Use word boundary matching for whole words only
        pattern = re.compile(r'\b(' + re.escape(word) + r')\b', re.IGNORECASE)
        # Replace with markdown bold (avoid double-highlighting)
        highlighted = pattern.sub(r'**\1**', highlighted)

    # Clean up any double-bold patterns
    highlighted = re.sub(r'\*\*(\*\*)+', '**', highlighted)
    highlighted = re.sub(r'(\*\*)+', '**', highlighted)

    return highlighted

def compute_facets(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Aggregate result counts by metadata fields.

    Args:
        results: List of search results (may have metadata populated if filters were applied)

    Returns:
        Dictionary with facet counts for outcomes, years, judges, regional offices
        Note: Only includes fields that are populated in the results
    """
    facets = {
        "outcomes": {},
        "years": {},
        "judges": {},
        "regional_offices": {}
    }

    for result in results:
        # Count outcomes (only if populated)
        outcome = result.get("outcome")
        if outcome:  # Skip if None or empty
            facets["outcomes"][outcome] = facets["outcomes"].get(outcome, 0) + 1

        # Count years (always available)
        year = result.get("year")
        if year:
            facets["years"][year] = facets["years"].get(year, 0) + 1

        # Count judges (only if populated)
        judge = result.get("judge")
        if judge:  # Skip if None or empty
            facets["judges"][judge] = facets["judges"].get(judge, 0) + 1

        # Count regional offices (only if populated)
        ro = result.get("regional_office")
        if ro:  # Skip if None or empty
            facets["regional_offices"][ro] = facets["regional_offices"].get(ro, 0) + 1

    # Limit to top 20 for judges and ROs
    if facets["judges"]:
        facets["judges"] = dict(sorted(facets["judges"].items(),
                                      key=lambda x: x[1], reverse=True)[:20])
    if facets["regional_offices"]:
        facets["regional_offices"] = dict(sorted(facets["regional_offices"].items(),
                                                key=lambda x: x[1], reverse=True)[:20])

    return facets

def fetch_case_text(url: str) -> Dict[str, Any]:
    """Fetch and parse BVA decision text from URL."""
    logger.info(f"Fetching case text from {url}")

    # Validate URL domain
    if not url.startswith("https://www.va.gov/"):
        raise HTTPException(status_code=400, detail="URL must be from va.gov domain")

    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT})

    try:
        resp = s.get(url, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
    except Timeout:
        raise HTTPException(status_code=504, detail="Request timed out while fetching case")
    except HTTPError as e:
        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail="Case not found")
        raise HTTPException(status_code=502, detail=f"Failed to fetch case: {e}")
    except RequestException as e:
        raise HTTPException(status_code=502, detail=f"Network error: {str(e)}")

    text = resp.text
    if not text or len(text) < 100:
        raise HTTPException(status_code=422, detail="Invalid or empty case content")

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    parsed = parse_decision_text(text)
    year = extract_year_from_url(url)
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
        "version": "1.3.0",
        "new_features": [
            "Boolean query support (AND/OR/NOT)",
            "Phrase matching with quotes",
            "Multi-year search (year_start to year_end)",
            "Post-search filtering (outcome, judge, regional office, date range)",
            "Sorting options (date, relevance, case_number, text_length, year)",
            "Keyword highlighting in snippets",
            "Faceted search results"
        ],
        "endpoints": {
            "/search": "POST - Search BVA decisions (enhanced with filters, sorting, facets)",
            "/case": "GET - Fetch specific case by URL",
            "/case/text": "GET - Raw text of a case",
            "/batch/search": "POST - Search multiple queries",
            "/analyze/text": "GET - Analyze decision text",
            "/health": "GET - Health check",
            "/test": "GET - Interactive testing GUI (v1.3.0)"
        }
    }

@app.post("/search", response_model=SearchResponse)
async def search_decisions(request: SearchRequest):
    loop = asyncio.get_running_loop()

    # Step 1: Preprocess query (boolean operators and phrase matching)
    processed_query = preprocess_query(request.query)
    logger.info(f"Original query: '{request.query}' -> Processed: '{processed_query}'")

    # Step 2: Execute search (single year, year range, or no year filter)
    if request.year_start and request.year_end:
        # Multi-year search
        results = await loop.run_in_executor(
            executor, search_multi_year,
            processed_query, request.year_start, request.year_end,
            request.max_pages, request.page_size
        )
    elif request.year:
        # Single year search (backward compatible)
        results = await loop.run_in_executor(
            executor, search_bva_paginated,
            processed_query, request.year, request.max_pages, request.page_size
        )
    else:
        # No year filter
        results = await loop.run_in_executor(
            executor, search_bva_paginated,
            processed_query, None, request.max_pages, request.page_size
        )

    # Step 3: Apply filters if requested
    filters_applied = {}
    if any([request.filter_outcome, request.filter_judge, request.filter_regional_office,
            request.filter_date_start, request.filter_date_end]):
        results = await loop.run_in_executor(
            executor, apply_filters,
            results, request.filter_outcome, request.filter_judge,
            request.filter_regional_office, request.filter_date_start,
            request.filter_date_end, executor
        )
        # Track which filters were applied
        if request.filter_outcome:
            filters_applied["outcome"] = request.filter_outcome
        if request.filter_judge:
            filters_applied["judge"] = request.filter_judge
        if request.filter_regional_office:
            filters_applied["regional_office"] = request.filter_regional_office
        if request.filter_date_start:
            filters_applied["date_start"] = request.filter_date_start
        if request.filter_date_end:
            filters_applied["date_end"] = request.filter_date_end

    # Step 4: Sort results if requested
    sort_applied = None
    if request.sort_by:
        results = sort_results(results, request.sort_by, request.sort_order)
        sort_applied = {"by": request.sort_by, "order": request.sort_order}

    # Step 5: Highlight keywords if requested
    if request.highlight_keywords:
        for result in results:
            result["highlighted_snippet"] = highlight_keywords(
                result.get("snippet", ""), request.query
            )

    # Step 6: Compute facets if requested
    facets = None
    if request.include_facets:
        facet_data = compute_facets(results)
        facets = SearchFacets(**facet_data)

    # Step 7: Build response
    return SearchResponse(
        query=request.query,
        processed_query=processed_query if processed_query != request.query else None,
        total_results=len(results),
        pages_searched=request.max_pages,
        results=[SearchResult(**r) for r in results],
        facets=facets,
        filters_applied=filters_applied if filters_applied else None,
        sort_applied=sort_applied,
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
                for m in matches[:20]:  # Limit to 20 contexts per keyword
                    start = max(m.start() - 40, 0)
                    end = min(m.end() + 40, len(text))
                    # Normalize the context snippet (remove control chars, normalize whitespace)
                    snippet = text[start:end]
                    snippet = re.sub(r"[\r\n\t]+", " ", snippet)
                    snippet = re.sub(r"\s+", " ", snippet)
                    snippets.append(snippet.strip())
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

@app.get("/test", response_class=HTMLResponse)
async def test_gui():
    """Serve the interactive testing GUI"""
    try:
        with open("test-gui.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Test GUI not found. Make sure test-gui.html is in the same directory as app.py")

# -------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
