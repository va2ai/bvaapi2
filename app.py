#!/usr/bin/env python3
"""
FastAPI BVA Search API v2.0
Uses search.usa.gov JSON API (no HTML scraping) for reliable results.
"""

from fastapi import FastAPI, HTTPException, Query, Body
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
import logging, requests, asyncio, re, signal, sys, os
from bs4 import BeautifulSoup
import html2text as _html2text
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor
from textstat import flesch_kincaid_grade

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="BVA Decision Search API",
    description="Search Board of Veterans' Appeals decisions via the search.usa.gov JSON API",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

executor = ThreadPoolExecutor(max_workers=10)

USER_AGENT = "VetAI-BVA-API/2.0"
REQUEST_TIMEOUT = 15
SEARCH_BASE = "https://search.usa.gov/search.json"
RESULTS_PER_PAGE = 20

# KnowVA (Oracle Service Cloud) API constants
KNOWVA_BASE = "https://www.knowva.ebenefits.va.gov/system/ws/v11"
KNOWVA_PORTAL_ID = "554400000001018"
KNOWVA_COMMON = {"$lang": "en-us", "usertype": "customer", "portalId": KNOWVA_PORTAL_ID}
KNOWVA_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://www.knowva.ebenefits.va.gov/",
    "Origin": "https://www.knowva.ebenefits.va.gov",
}

# eCFR API constants
ECFR_VERSIONER_BASE = "https://www.ecfr.gov/api/versioner/v1"
ECFR_SEARCH_BASE    = "https://www.ecfr.gov/api/search/v1/results"
ECFR_HEADERS = {
    "User-Agent": "VetAI-BVA-API/2.0",
    "Accept": "application/json, text/plain, */*",
}

# Full year -> dc collection ID mapping (verified from BVA search dropdown)
YEAR_DC_MAP: Dict[int, int] = {
    1992: 9133, 1993: 9134, 1994: 9135, 1995: 9136, 1996: 9137,
    1997: 9138, 1998: 9139, 1999: 9140, 2000: 9141, 2001: 9142,
    2002: 9143, 2003: 9144, 2004: 9145, 2005: 9146, 2006: 9147,
    2007: 9148, 2008: 9149, 2009: 9150, 2010: 9151, 2011: 9152,
    2012: 9153, 2013: 9154, 2014: 9155, 2015: 9156, 2016: 9157,
    2017: 9158, 2018: 9159, 2019: 9160, 2020: 9161, 2021: 9162,
    2022: 9256, 2023: 9692, 2024: 10080, 2025: 10280,
}

# -------------------------------------------------------------------
# Pydantic models
# -------------------------------------------------------------------
class SearchRequest(BaseModel):
    query: str
    year: Optional[int] = None
    page: int = Field(1, ge=1, le=50)
    per_page: int = Field(20, ge=1, le=20)

class SearchResult(BaseModel):
    url: str
    title: str
    snippet: str
    case_number: Optional[str]
    year: Optional[int]
    publication_date: Optional[str]

class SearchResponse(BaseModel):
    query: str
    total: int
    page: int
    per_page: int
    results: List[SearchResult]
    spelling_correction: Optional[str]
    timestamp: str

class CaseDetail(BaseModel):
    url: str
    year: Optional[int]
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

class BatchSearchPayload(BaseModel):
    queries: List[str] = Field(..., min_length=1)
    year: Optional[int] = None
    page: int = Field(1, ge=1, le=10)

class BatchSearchResult(BaseModel):
    query: str
    total: int
    count: int
    results: List[SearchResult]

class AnalyzeResponse(BaseModel):
    url: str
    case_number: Optional[str]
    text_length: int
    keyword_counts: Optional[Dict[str, int]]
    keyword_contexts: Optional[Dict[str, List[str]]]
    va_terms_found: Dict[str, int]
    readability_grade: Optional[float]
    analysis_timestamp: str

# KnowVA models
class KnowVATopic(BaseModel):
    id: int
    name: str
    parent_topic_id: Optional[int]
    total_article_count: Optional[int]

class KnowVAArticleSummary(BaseModel):
    id: int
    name: str
    snippet: Optional[str]

class KnowVAArticle(BaseModel):
    id: int
    name: str
    last_modified_date: Optional[str]
    content: Optional[str]

class KnowVASearchResponse(BaseModel):
    query: str
    page: int
    pagesize: int
    total: int
    results: List[KnowVAArticleSummary]

# 38 CFR models
class CFRSection(BaseModel):
    identifier: str
    label: str

class CFRPart(BaseModel):
    number: str
    label: str
    sections: List[CFRSection]

class CFRStructureResponse(BaseModel):
    title: int
    date: str
    parts: List[CFRPart]
    retrieved_at: str

class CFRSectionResponse(BaseModel):
    part: str
    section: str
    citation: str
    content_markdown: str
    retrieved_at: str

class CFRSearchResult(BaseModel):
    title: int
    part: Optional[str]
    section: Optional[str]
    label: str
    snippet: Optional[str]
    score: Optional[float]
    hierarchy: Optional[List[str]]

class CFRSearchResponse(BaseModel):
    query: str
    page: int
    per_page: int
    total: int
    results: List[CFRSearchResult]
    retrieved_at: str

# -------------------------------------------------------------------
# Regex patterns for decision parsing
# -------------------------------------------------------------------
DATE_RE     = re.compile(
    r"(?:Decision\s*Date\s*[:\-]\s*)(\d{2}/\d{2}/\d{2,4}|[A-Za-z]{3,9}\s+\d{1,2},\s+\d{4})",
    re.I
)
DOCKET_RE   = re.compile(r"Docket\s*No\.?\s*[:\-]?\s*([\w\-\s\/]+)", re.I)
ISSUES_RE   = re.compile(r"ISSUES?\s*[:\-]?\s*(.*)", re.I)
CFR_RE      = re.compile(r"38\s*CFR\s*[§\u00A7]\s*([\d\.]+[a-z0-9\(\)]*)", re.I)
M21_RE      = re.compile(r"M21-1[\w\-\.\s]*", re.I)
RO_RE       = re.compile(r"Regional\s+Office\s+in\s+([A-Za-z\s,]+)", re.I)
JUDGE_RE    = re.compile(r"(?:Veterans\s+Law\s+Judge|Acting\s+Veterans\s+Law\s+Judge)\s*[:\-]?\s*([A-Z][A-Za-z\s\-\.]+)")
OUTCOME_PATTERNS = [
    ("Granted",  re.compile(r"\bGRANTED\b", re.I)),
    ("Denied",   re.compile(r"\bDENIED\b",  re.I)),
    ("Remanded", re.compile(r"\bREMANDED\b", re.I)),
]

# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------
def extract_year_from_url(url: str) -> Optional[int]:
    m = re.search(r"/vetapp(\d{2})/", url, re.I)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy < 50 else 1900 + yy
    m = re.search(r"/(19\d{2}|20\d{2})/", url)
    return int(m.group(1)) if m else None

def clean_snippet(snippet: str) -> str:
    """Remove search.usa.gov bold-highlight escape chars from snippets."""
    return re.sub(r"[\xee\x80-\x83\xdc\x80-\xbf]|\uE000|\uE001", "", snippet)

def extract_case_number(url: str) -> Optional[str]:
    if ".txt" in url:
        return url.split("/")[-1].replace(".txt", "")
    return None

def parse_decision_text(text: str) -> Dict[str, Any]:
    d = {
        "decision_date": None, "docket_no": None, "outcome": None,
        "issues": [], "citations": [], "regional_office": None, "judge": None
    }
    if m := DATE_RE.search(text):
        raw_date = m.group(1).strip()
        for fmt in ("%m/%d/%y", "%m/%d/%Y", "%B %d, %Y"):
            try:
                d["decision_date"] = datetime.strptime(raw_date, fmt).strftime("%Y-%m-%d")
                break
            except ValueError:
                pass
    if m := DOCKET_RE.search(text):
        d["docket_no"] = re.sub(r"\s+", " ", m.group(1)).strip()

    outcomes_found = [label for label, pat in OUTCOME_PATTERNS if pat.search(text)]
    if len(outcomes_found) > 1:
        d["outcome"] = "Mixed"
    elif outcomes_found:
        d["outcome"] = outcomes_found[0]

    if m := ISSUES_RE.search(text):
        items = re.split(r"\s*\d+\.\s*|;|\n", m.group(1).strip())
        d["issues"] = [i.strip() for i in items if i.strip()][:5]

    cfrs = CFR_RE.findall(text)
    m21s = M21_RE.findall(text)
    d["citations"] = sorted(set([f"38 CFR ss {c}" for c in cfrs[:10]] + m21s[:5]))

    if m := RO_RE.search(text):
        d["regional_office"] = m.group(1).strip().rstrip(".")
    if m := JUDGE_RE.search(text):
        d["judge"] = m.group(1).strip()
    return d

def _search_json(query: str, year: Optional[int], page: int) -> Dict:
    """Call search.usa.gov JSON API and return raw response dict."""
    params: Dict[str, Any] = {
        "affiliate": "bvadecisions",
        "query": query,
    }
    if year and year in YEAR_DC_MAP:
        params["dc"] = YEAR_DC_MAP[year]
    elif year:
        params["query"] = f"{query} {year}"

    offset = (page - 1) * RESULTS_PER_PAGE
    if offset > 0:
        params["offset"] = offset

    url = f"{SEARCH_BASE}?{urlencode(params)}"
    logger.info(f"GET {url}")
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})
    resp = session.get(url, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    return resp.json()

def search_bva(query: str, year: Optional[int], page: int) -> Dict:
    data = _search_json(query, year, page)
    web = data.get("web", {})
    raw_results = web.get("results", [])
    results = []
    for r in raw_results:
        result_url = r.get("url", "")
        results.append(SearchResult(
            url=result_url,
            title=r.get("title", "").replace(".txt", ""),
            snippet=clean_snippet(r.get("snippet", "")),
            case_number=extract_case_number(result_url),
            year=extract_year_from_url(result_url),
            publication_date=r.get("publication_date"),
        ))
    return {
        "total": web.get("total", 0),
        "spelling_correction": web.get("spelling_correction"),
        "results": results,
    }

def fetch_case_text(url: str) -> Dict[str, Any]:
    logger.info(f"Fetching case: {url}")
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})
    resp = session.get(url, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    text = resp.text
    if not text or len(text) < 100:
        raise HTTPException(status_code=422, detail="Invalid or empty case content")
    return {
        "url": url,
        "year": extract_year_from_url(url),
        "case_number": extract_case_number(url),
        "raw_text": text,
        "parsed": parse_decision_text(text),
        "text_length": len(text),
        "fetch_timestamp": datetime.now().isoformat()
    }

# -------------------------------------------------------------------
# Endpoints
# -------------------------------------------------------------------
@app.get("/")
async def root():
    return {
        "api": "BVA Decision Search API",
        "version": "2.0.0",
        "source": "search.usa.gov JSON API (affiliate: bvadecisions)",
        "years_available": f"{min(YEAR_DC_MAP)} - {max(YEAR_DC_MAP)}",
        "endpoints": {
            "GET  /search":                  "Search BVA decisions (query params)",
            "POST /search":                  "Search BVA decisions (JSON body)",
            "POST /batch/search":            "Search multiple queries",
            "GET  /case":                    "Fetch parsed case details by URL",
            "GET  /case/text":               "Fetch raw case text by URL",
            "GET  /analyze/text":            "Analyze decision for keywords & VA terms",
            "GET  /years":                   "List available year->dc collection mappings",
            "GET  /knowva/topics":           "List KnowVA knowledge base topics",
            "GET  /knowva/search?q=":        "Search KnowVA articles (M21-1, policy, etc.)",
            "GET  /knowva/article/{id}":     "Fetch full KnowVA article by ID",
            "GET  /knowva/popular":          "List most popular KnowVA articles",
            "GET  /cfr/structure":              "Title 38 CFR table of contents",
            "GET  /cfr/section?part=&section=": "Fetch 38 CFR section text as markdown",
            "GET  /cfr/search?q=":              "Search within Title 38 CFR",
            "GET  /health":                  "Health check",
        }
    }

@app.get("/search", response_model=SearchResponse)
async def search_get(
    q: str = Query(..., description="Search query"),
    year: Optional[int] = Query(None, ge=1992, le=2025),
    page: int = Query(1, ge=1, le=50),
):
    loop = asyncio.get_running_loop()
    data = await loop.run_in_executor(executor, search_bva, q, year, page)
    return SearchResponse(
        query=q,
        total=data["total"],
        page=page,
        per_page=RESULTS_PER_PAGE,
        results=data["results"],
        spelling_correction=data.get("spelling_correction"),
        timestamp=datetime.now().isoformat(),
    )

@app.post("/search", response_model=SearchResponse)
async def search_post(request: SearchRequest):
    loop = asyncio.get_running_loop()
    data = await loop.run_in_executor(executor, search_bva, request.query, request.year, request.page)
    return SearchResponse(
        query=request.query,
        total=data["total"],
        page=request.page,
        per_page=RESULTS_PER_PAGE,
        results=data["results"],
        spelling_correction=data.get("spelling_correction"),
        timestamp=datetime.now().isoformat(),
    )

@app.post("/batch/search", response_model=List[BatchSearchResult])
async def batch_search(payload: BatchSearchPayload = Body(...)):
    queries = [q.strip() for q in payload.queries if q.strip()]
    if not queries:
        raise HTTPException(status_code=422, detail="`queries` cannot be empty.")
    loop = asyncio.get_running_loop()
    results = []
    for q in queries:
        try:
            data = await loop.run_in_executor(executor, search_bva, q, payload.year, payload.page)
            results.append(BatchSearchResult(
                query=q,
                total=data["total"],
                count=len(data["results"]),
                results=data["results"],
            ))
            await asyncio.sleep(0.5)
        except Exception as e:
            logger.error(f"Batch search error for '{q}': {e}")
            results.append(BatchSearchResult(query=q, total=0, count=0, results=[]))
    return results

@app.get("/case", response_model=CaseDetail)
async def get_case(url: str = Query(...), full_text: bool = Query(False)):
    loop = asyncio.get_running_loop()
    case_data = await loop.run_in_executor(executor, fetch_case_text, url)
    parsed = case_data["parsed"]
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
        text_length=case_data["text_length"],
        text_preview=case_data["raw_text"][:500],
        full_text=case_data["raw_text"] if full_text else None,
        fetch_timestamp=case_data["fetch_timestamp"],
    )

@app.get("/case/text")
async def get_case_text(url: str = Query(...)):
    loop = asyncio.get_running_loop()
    case_data = await loop.run_in_executor(executor, fetch_case_text, url)
    return PlainTextResponse(
        content=case_data["raw_text"],
        media_type="text/plain",
        headers={
            "X-Case-Number": case_data.get("case_number") or "unknown",
            "X-Year": str(case_data.get("year") or "unknown"),
            "X-Text-Length": str(case_data["text_length"]),
        }
    )

@app.get("/analyze/text", response_model=AnalyzeResponse)
async def analyze_text(
    url: str = Query(...),
    keywords: List[str] = Query([]),
    context: bool = Query(False),
):
    loop = asyncio.get_running_loop()
    case_data = await loop.run_in_executor(executor, fetch_case_text, url)
    text = case_data["raw_text"]
    text_lower = text.lower()
    text_upper = text.upper()

    keyword_counts: Dict[str, int] = {}
    keyword_contexts: Dict[str, List[str]] = {}
    for k in keywords:
        matches = list(re.finditer(re.escape(k), text, re.IGNORECASE))
        keyword_counts[k] = len(matches)
        if context:
            keyword_contexts[k] = [
                text[max(m.start() - 40, 0):min(m.end() + 40, len(text))]
                for m in matches
            ]

    va_terms = {
        "TDIU": text_upper.count("TDIU"),
        "PTSD": text_upper.count("PTSD"),
        "service-connected": text_lower.count("service-connected"),
        "disability rating": text_lower.count("disability rating"),
        "effective date": text_lower.count("effective date"),
        "clear and unmistakable error": text_lower.count("clear and unmistakable error"),
        "individual unemployability": text_lower.count("individual unemployability"),
    }

    return AnalyzeResponse(
        url=url,
        case_number=case_data.get("case_number"),
        text_length=len(text),
        keyword_counts=keyword_counts or None,
        keyword_contexts=keyword_contexts if context else None,
        va_terms_found=va_terms,
        readability_grade=flesch_kincaid_grade(text),
        analysis_timestamp=datetime.now().isoformat(),
    )

@app.get("/years")
async def list_years():
    return {
        "years": [
            {"year": y, "dc": dc}
            for y, dc in sorted(YEAR_DC_MAP.items())
        ]
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": "2.0.0",
        "timestamp": datetime.now().isoformat(),
    }

# -------------------------------------------------------------------
# KnowVA helpers
# -------------------------------------------------------------------
def _knowva_get(path: str, params: Dict[str, Any]) -> Dict:
    url = f"{KNOWVA_BASE}/{path}"
    merged = {**KNOWVA_COMMON, **params}
    session = requests.Session()
    session.headers.update(KNOWVA_HEADERS)
    logger.info(f"KnowVA GET {url} params={merged}")
    resp = session.get(url, params=merged, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    return resp.json()

def _knowva_topics_sync() -> List[KnowVATopic]:
    data = _knowva_get("ss/topic", {
        "$attribute": "name,id,parentTopicId,totalArticleCount",
        "$level": 0,
        "$pagenum": 0,
        "$pagesize": 1000,
    })
    # Response shape: {"topicTree": [{"topic": {...}}]}
    raw = data.get("topicTree", [])
    topics = []
    for entry in raw:
        t = entry.get("topic", entry)
        topics.append(KnowVATopic(
            id=t["id"],
            name=t.get("name", ""),
            parent_topic_id=t.get("parentTopicId"),
            total_article_count=t.get("articleTotalCount") or t.get("totalArticleCount"),
        ))
    return topics

def _knowva_search_sync(query: str, page: int, pagesize: int) -> Dict:
    data = _knowva_get("ss/search/kb", {
        "$attribute": "name,id,snippet,availableEditions,articleTypeAttributes",
        "$pagenum": page,
        "$pagesize": pagesize,
        "federated": "true",
        "q": query,
    })
    # Response shape: {"article": [...], "query": "..."}
    raw = data.get("article", data.get("items", []))
    total = data.get("totalCount", len(raw))
    results = [
        KnowVAArticleSummary(
            id=r["id"],
            name=r.get("name", ""),
            snippet=r.get("snippet") or r.get("description"),
        )
        for r in raw
    ]
    return {"total": total, "results": results}

def _clean_html_to_text(html: str) -> str:
    """Convert HTML to clean markdown text."""
    # Fix mojibake before parsing (cp1252 bytes misread as latin-1)
    try:
        html = html.encode("latin-1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        pass
    h = _html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True
    h.ignore_tables = False
    h.body_width = 0          # no line wrapping
    h.unicode_snob = True
    text = h.handle(html)
    # Collapse excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def _ecfr_get(path: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
    url = f"{ECFR_VERSIONER_BASE}/{path}"
    session = requests.Session()
    session.headers.update(ECFR_HEADERS)
    logger.info(f"eCFR GET {url} params={params}")
    resp = session.get(url, params=params or {}, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    return resp

def _ecfr_structure_sync() -> CFRStructureResponse:
    resp = _ecfr_get("structure/current/title-38.json")
    data = resp.json()
    parts: List[CFRPart] = []

    def _collect(node: Dict) -> None:
        if node.get("type") == "part":
            sections = []
            def _secs(n):
                for c in n.get("children", []):
                    if c.get("type") == "section":
                        sections.append(CFRSection(
                            identifier=c.get("identifier", ""),
                            label=c.get("label_level", c.get("identifier", "")),
                        ))
                    else:
                        _secs(c)
            _secs(node)
            parts.append(CFRPart(
                number=node.get("identifier", ""),
                label=node.get("label_level", ""),
                sections=sections,
            ))
        else:
            for child in node.get("children", []):
                _collect(child)

    for child in data.get("children", []):
        _collect(child)

    return CFRStructureResponse(
        title=38, date=data.get("date", "current"),
        parts=parts, retrieved_at=datetime.now().isoformat()
    )

def _ecfr_section_sync(part: str, section: str) -> CFRSectionResponse:
    resp = _ecfr_get("full/current/title-38", params={"part": part, "section": section})
    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup.find_all(["AUTH", "SOURCE", "CITA", "AMDDATE"]):
        tag.decompose()
    markdown = _clean_html_to_text(str(soup))
    return CFRSectionResponse(
        part=part, section=section,
        citation=f"38 CFR \u00a7 {part}.{section}",
        content_markdown=markdown,
        retrieved_at=datetime.now().isoformat(),
    )

def _ecfr_search_sync(query: str, page: int, per_page: int) -> Dict:
    session = requests.Session()
    session.headers.update(ECFR_HEADERS)
    resp = session.get(ECFR_SEARCH_BASE,
                       params={"query": query, "per_page": per_page, "page": page, "title": 38},
                       timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    meta = data.get("meta", {})
    results = []
    for r in data.get("results", []):
        si = r.get("structure_index", {})
        ident = si.get("identifier", "")
        part_num = ident.split(".")[0] if "." in ident else ident
        sec_num  = ident.split(".")[1] if "." in ident else None
        hier = si.get("hierarchy", {})
        results.append(CFRSearchResult(
            title=38, part=part_num or None, section=sec_num,
            label=si.get("label", ""),
            snippet=r.get("content"),
            score=r.get("score"),
            hierarchy=list(hier.values()) if hier else None,
        ))
    return {"total": meta.get("total_count", len(results)), "results": results}

def _knowva_article_sync(article_id: int) -> KnowVAArticle:
    data = _knowva_get(f"ss/article/{article_id}", {
        "$attribute": "name,id,lastModifiedDate,content",
    })
    # Response shape: {"article": [{...}]}
    raw = data.get("article", [data] if "id" in data else [])
    a = raw[0] if raw else {}
    html = a.get("content", "")
    return KnowVAArticle(
        id=a.get("id", article_id),
        name=a.get("name", ""),
        last_modified_date=a.get("lastModifiedDate"),
        content=_clean_html_to_text(html) if html else None,
    )

def _knowva_popular_sync(pagesize: int) -> List[KnowVAArticleSummary]:
    data = _knowva_get("ss/dfaq", {
        "$attribute": "name,id,milestone",
        "$pagenum": 1,
        "$pagesize": pagesize,
    })
    # Response shape: {"article": [...]} or {"items": [...]}
    raw = data.get("article", data.get("items", []))
    return [
        KnowVAArticleSummary(id=r["id"], name=r.get("name", ""), snippet=None)
        for r in raw
    ]

# -------------------------------------------------------------------
# KnowVA endpoints
# -------------------------------------------------------------------
@app.get("/knowva/topics", response_model=List[KnowVATopic], tags=["KnowVA"])
async def knowva_topics():
    """List all KnowVA knowledge base topics/categories."""
    loop = asyncio.get_running_loop()
    try:
        return await loop.run_in_executor(executor, _knowva_topics_sync)
    except Exception as e:
        logger.error(f"KnowVA topics error: {e}")
        raise HTTPException(status_code=502, detail=str(e))

@app.get("/knowva/search", response_model=KnowVASearchResponse, tags=["KnowVA"])
async def knowva_search(
    q: str = Query(..., description="Search query"),
    page: int = Query(1, ge=1, le=100),
    pagesize: int = Query(30, ge=1, le=100),
):
    """Full-text search of KnowVA articles (M21-1, policy memos, etc.)."""
    loop = asyncio.get_running_loop()
    try:
        data = await loop.run_in_executor(executor, _knowva_search_sync, q, page, pagesize)
        return KnowVASearchResponse(
            query=q, page=page, pagesize=pagesize,
            total=data["total"], results=data["results"],
        )
    except Exception as e:
        logger.error(f"KnowVA search error: {e}")
        raise HTTPException(status_code=502, detail=str(e))

@app.get("/knowva/article/{article_id}", response_model=KnowVAArticle, tags=["KnowVA"])
async def knowva_article(article_id: int):
    """Fetch full content of a KnowVA article by its numeric ID."""
    loop = asyncio.get_running_loop()
    try:
        return await loop.run_in_executor(executor, _knowva_article_sync, article_id)
    except Exception as e:
        logger.error(f"KnowVA article error: {e}")
        raise HTTPException(status_code=502, detail=str(e))

@app.get("/knowva/popular", response_model=List[KnowVAArticleSummary], tags=["KnowVA"])
async def knowva_popular(pagesize: int = Query(10, ge=1, le=50)):
    """Return the most popular KnowVA articles."""
    loop = asyncio.get_running_loop()
    try:
        return await loop.run_in_executor(executor, _knowva_popular_sync, pagesize)
    except Exception as e:
        logger.error(f"KnowVA popular error: {e}")
        raise HTTPException(status_code=502, detail=str(e))

# -------------------------------------------------------------------
# 38 CFR endpoints
# -------------------------------------------------------------------
@app.get("/cfr/structure", response_model=CFRStructureResponse, tags=["38 CFR"])
async def cfr_structure():
    """Title 38 CFR table of contents - all parts and sections."""
    loop = asyncio.get_running_loop()
    try:
        return await loop.run_in_executor(executor, _ecfr_structure_sync)
    except Exception as e:
        logger.error(f"eCFR structure error: {e}")
        raise HTTPException(status_code=502, detail=str(e))

@app.get("/cfr/section", response_model=CFRSectionResponse, tags=["38 CFR"])
async def cfr_section(
    part: str = Query(..., example="3"),
    section: str = Query(..., example="102"),
):
    """Fetch 38 CFR section text as clean markdown. e.g. part=3&section=102 -> 38 CFR ss 3.102"""
    loop = asyncio.get_running_loop()
    try:
        return await loop.run_in_executor(executor, _ecfr_section_sync, part, section)
    except Exception as e:
        logger.error(f"eCFR section error part={part} section={section}: {e}")
        raise HTTPException(status_code=502, detail=str(e))

@app.get("/cfr/search", response_model=CFRSearchResponse, tags=["38 CFR"])
async def cfr_search(
    q: str = Query(..., example="PTSD"),
    page: int = Query(1, ge=1, le=100),
    per_page: int = Query(20, ge=1, le=100),
):
    """Full-text search within Title 38 CFR regulations."""
    loop = asyncio.get_running_loop()
    try:
        data = await loop.run_in_executor(executor, _ecfr_search_sync, q, page, per_page)
        return CFRSearchResponse(
            query=q, page=page, per_page=per_page,
            total=data["total"], results=data["results"],
            retrieved_at=datetime.now().isoformat(),
        )
    except Exception as e:
        logger.error(f"eCFR search error q={q}: {e}")
        raise HTTPException(status_code=502, detail=str(e))

def _shutdown(signum, frame):
    logger.info("Shutting down — releasing ports...")
    executor.shutdown(wait=False, cancel_futures=True)
    sys.exit(0)

signal.signal(signal.SIGINT, _shutdown)
signal.signal(signal.SIGTERM, _shutdown)

if __name__ == "__main__":
    import uvicorn
    import socket

    PORT = int(os.environ.get("PORT", 8001))

    # Check if port is free; if not, warn and pick next available
    def _find_free_port(start: int) -> int:
        for p in range(start, start + 10):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                try:
                    s.bind(("0.0.0.0", p))
                    return p
                except OSError:
                    continue
        raise RuntimeError(f"No free port found starting at {start}")

    port = _find_free_port(PORT)
    if port != PORT:
        logger.warning(f"Port {PORT} in use, using {port} instead")

    uvicorn.run(app, host="0.0.0.0", port=port)
