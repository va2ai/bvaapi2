#!/usr/bin/env python3
"""
FastAPI BVA Search API v2.0
Uses search.usa.gov JSON API (no HTML scraping) for reliable results.
"""

from fastapi import FastAPI, HTTPException, Query, Body, Request
from fastapi.responses import PlainTextResponse, Response, JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List, Dict, Any
from datetime import datetime
import logging, requests, asyncio, re, signal, sys, os
from bs4 import BeautifulSoup
import html2text as _html2text
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor
from textstat import flesch_kincaid_grade
from cavc_client import CavcClient

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
cavc_client = CavcClient()


@app.on_event("startup")
async def _startup_rag_reindex():
    """Auto-reindex RAG on container startup (background task)."""
    async def _reindex():
        import rag as _rag
        from ingest import ingest_cfr_part3, ingest_cfr_part4, ingest_knowva
        api_url = os.environ.get("BVA_API_URL", "http://localhost:8001")
        loop = asyncio.get_running_loop()
        # Wait for server to be ready
        await asyncio.sleep(5)
        try:
            all_chunks = []
            all_chunks.extend(await loop.run_in_executor(executor, ingest_cfr_part4, api_url))
            all_chunks.extend(await loop.run_in_executor(executor, ingest_cfr_part3, api_url))
            all_chunks.extend(await loop.run_in_executor(executor, ingest_knowva, api_url))
            indexed = _rag.add_chunks(all_chunks)
            logger.info(f"Startup RAG reindex complete: {indexed} chunks indexed")
        except Exception as e:
            logger.error(f"Startup RAG reindex failed: {e}")
    asyncio.create_task(_reindex())

# -------------------------------------------------------------------
# Structured error model + exception classes
# -------------------------------------------------------------------
class APIError(BaseModel):
    code: str
    message: str
    field: Optional[str] = None
    allowed: Optional[Any] = None
    suggested_fix: Optional[str] = None


class BVAAPIError(HTTPException):
    def __init__(self, status_code: int, code: str, message: str,
                 field: str = None, allowed: Any = None, suggested_fix: str = None):
        self.error_code = code
        self.error_message = message
        self.error_field = field
        self.error_allowed = allowed
        self.error_suggested_fix = suggested_fix
        super().__init__(status_code=status_code, detail=message)


@app.exception_handler(BVAAPIError)
async def bva_api_error_handler(request: Request, exc: BVAAPIError):
    body = {
        "code": exc.error_code,
        "message": exc.error_message,
    }
    if exc.error_field:
        body["field"] = exc.error_field
    if exc.error_allowed is not None:
        body["allowed"] = exc.error_allowed
    if exc.error_suggested_fix:
        body["suggested_fix"] = exc.error_suggested_fix
    return JSONResponse(status_code=exc.status_code, content=body)


def _suggest_fix(field: str, err: dict) -> str:
    """Generate a suggested_fix string from a Pydantic validation error."""
    ctx = err.get("ctx", {})
    err_type = err.get("type", "")
    input_val = err.get("input")

    if "ge" in ctx or "le" in ctx:
        lo = ctx.get("ge", ctx.get("gt", "?"))
        hi = ctx.get("le", ctx.get("lt", "?"))
        return f"{field} must be {lo}-{hi}, you sent {input_val}. Try {field}={lo}"

    if "min_length" in ctx:
        return f"{field} requires at least {ctx['min_length']} item(s)"

    if err_type == "missing":
        return f"{field} is required"

    if "int_parsing" in err_type or "int_type" in err_type:
        return f"{field} must be an integer, you sent '{input_val}'"

    if err_type == "extra_forbidden":
        return f"Unknown field '{field}'. Remove it from the request body"

    if err_type == "string_pattern_mismatch":
        pattern = ctx.get("pattern", "")
        return f"{field} must match pattern {pattern}"

    return f"Fix the value for {field}: {err.get('msg', 'invalid')}"


@app.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, exc: RequestValidationError):
    errors = []
    for err in exc.errors():
        field = ".".join(str(loc) for loc in err["loc"] if str(loc) != "body")
        fix = _suggest_fix(field, err)
        errors.append({
            "code": "validation_error",
            "message": err["msg"],
            "field": field,
            "suggested_fix": fix,
        })
    return JSONResponse(status_code=422, content={"errors": errors})


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

# Federal Register API constants
FR_API_BASE = "https://www.federalregister.gov/api/v1"
FR_VA_SLUG = "veterans-affairs-department"
FR_FIELDS = [
    "document_number", "title", "type", "abstract", "citation",
    "publication_date", "agencies", "html_url", "pdf_url",
    "cfr_references", "action", "dates", "effective_on", "comments_close_on",
]

# Part 4 diagnostic code lookup (eCFR search doesn't index rating criteria well)
# Format: DC code -> (condition, CFR section, part, description)
DC_LOOKUP: Dict[str, Dict[str, str]] = {
    # Mental disorders - 4.130
    "9411": {"condition": "PTSD", "section": "130", "part": "4", "schedule": "Mental Disorders"},
    "9434": {"condition": "Major Depressive Disorder", "section": "130", "part": "4", "schedule": "Mental Disorders"},
    "9400": {"condition": "Generalized Anxiety Disorder", "section": "130", "part": "4", "schedule": "Mental Disorders"},
    "9201": {"condition": "Schizophrenia", "section": "130", "part": "4", "schedule": "Mental Disorders"},
    "9432": {"condition": "Bipolar Disorder", "section": "130", "part": "4", "schedule": "Mental Disorders"},
    "9413": {"condition": "Unspecified Anxiety Disorder", "section": "130", "part": "4", "schedule": "Mental Disorders"},
    "9440": {"condition": "Chronic Adjustment Disorder", "section": "130", "part": "4", "schedule": "Mental Disorders"},
    # Respiratory - 4.97
    "6602": {"condition": "Asthma (Bronchial)", "section": "97", "part": "4", "schedule": "Respiratory System"},
    "6604": {"condition": "COPD", "section": "97", "part": "4", "schedule": "Respiratory System"},
    "6847": {"condition": "Sleep Apnea (Obstructive)", "section": "97", "part": "4", "schedule": "Respiratory System"},
    "6600": {"condition": "Bronchitis (Chronic)", "section": "97", "part": "4", "schedule": "Respiratory System"},
    "6845": {"condition": "Restrictive Lung Disease", "section": "97", "part": "4", "schedule": "Respiratory System"},
    # Musculoskeletal - 4.71a
    "5201": {"condition": "Arm (Limitation of Motion)", "section": "71a", "part": "4", "schedule": "Musculoskeletal System"},
    "5003": {"condition": "Arthritis (Degenerative)", "section": "71a", "part": "4", "schedule": "Musculoskeletal System"},
    "5010": {"condition": "Arthritis (Traumatic)", "section": "71a", "part": "4", "schedule": "Musculoskeletal System"},
    "5237": {"condition": "Lumbosacral Strain", "section": "71a", "part": "4", "schedule": "Musculoskeletal System"},
    "5242": {"condition": "Degenerative Arthritis of the Spine", "section": "71a", "part": "4", "schedule": "Musculoskeletal System"},
    "5243": {"condition": "Intervertebral Disc Syndrome (IVDS)", "section": "71a", "part": "4", "schedule": "Musculoskeletal System"},
    "5260": {"condition": "Leg (Limitation of Flexion)", "section": "71a", "part": "4", "schedule": "Musculoskeletal System"},
    "5261": {"condition": "Leg (Limitation of Extension)", "section": "71a", "part": "4", "schedule": "Musculoskeletal System"},
    "5271": {"condition": "Ankle (Limited Motion)", "section": "71a", "part": "4", "schedule": "Musculoskeletal System"},
    # Neurological - 4.124a
    "8045": {"condition": "Traumatic Brain Injury (TBI)", "section": "124a", "part": "4", "schedule": "Neurological Conditions"},
    "8100": {"condition": "Migraine Headaches", "section": "124a", "part": "4", "schedule": "Neurological Conditions"},
    "8520": {"condition": "Sciatic Nerve (Paralysis)", "section": "124a", "part": "4", "schedule": "Neurological Conditions"},
    "8515": {"condition": "Median Nerve (Paralysis)", "section": "124a", "part": "4", "schedule": "Neurological Conditions"},
    "8516": {"condition": "Ulnar Nerve (Paralysis)", "section": "124a", "part": "4", "schedule": "Neurological Conditions"},
    "8510": {"condition": "Upper Radicular Group (Paralysis)", "section": "124a", "part": "4", "schedule": "Neurological Conditions"},
    # Auditory - 4.85/4.87
    "6100": {"condition": "Hearing Loss (Bilateral)", "section": "85", "part": "4", "schedule": "Ear"},
    "6260": {"condition": "Tinnitus", "section": "87", "part": "4", "schedule": "Ear"},
    # Cardiovascular - 4.104
    "7005": {"condition": "Coronary Artery Disease", "section": "104", "part": "4", "schedule": "Cardiovascular System"},
    "7101": {"condition": "Hypertension", "section": "104", "part": "4", "schedule": "Cardiovascular System"},
    "7110": {"condition": "Aortic Aneurysm", "section": "104", "part": "4", "schedule": "Cardiovascular System"},
    # Skin - 4.118
    "7806": {"condition": "Dermatitis/Eczema", "section": "118", "part": "4", "schedule": "Skin"},
    "7800": {"condition": "Burn Scars (Head/Face/Neck)", "section": "118", "part": "4", "schedule": "Skin"},
    "7801": {"condition": "Burn Scars (Other)", "section": "118", "part": "4", "schedule": "Skin"},
    "7804": {"condition": "Unstable/Painful Scars", "section": "118", "part": "4", "schedule": "Skin"},
    # Digestive - 4.114
    "7346": {"condition": "GERD (Hiatal Hernia)", "section": "114", "part": "4", "schedule": "Digestive System"},
    "7319": {"condition": "Irritable Bowel Syndrome (IBS)", "section": "114", "part": "4", "schedule": "Digestive System"},
    "7323": {"condition": "Ulcerative Colitis", "section": "114", "part": "4", "schedule": "Digestive System"},
    # Endocrine - 4.119
    "7913": {"condition": "Diabetes Mellitus (Type II)", "section": "119", "part": "4", "schedule": "Endocrine System"},
    "7900": {"condition": "Hyperthyroidism", "section": "119", "part": "4", "schedule": "Endocrine System"},
    # Genitourinary - 4.115
    "7528": {"condition": "Malignant Neoplasms (Genitourinary)", "section": "115a", "part": "4", "schedule": "Genitourinary System"},
    "7522": {"condition": "Erectile Dysfunction", "section": "115a", "part": "4", "schedule": "Genitourinary System"},
    # Eye - 4.79
    "6066": {"condition": "Visual Acuity Loss", "section": "79", "part": "4", "schedule": "Eye"},
    # Dental/Oral - 4.150
    "9905": {"condition": "TMJ (Temporomandibular)", "section": "150", "part": "4", "schedule": "Dental and Oral Conditions"},
    # Gynecological - 4.116
    "7629": {"condition": "Endometriosis", "section": "116", "part": "4", "schedule": "Gynecological Conditions"},
    # Infectious - 4.88b
    "6354": {"condition": "Chronic Fatigue Syndrome", "section": "88b", "part": "4", "schedule": "Infectious Diseases"},
    # Hematologic - 4.117
    "7702": {"condition": "Agranulocytosis", "section": "117", "part": "4", "schedule": "Hemic and Lymphatic Systems"},
    # Gulf War / Undiagnosed - 3.317
    "8863": {"condition": "Gulf War Undiagnosed Illness", "section": "317", "part": "3", "schedule": "Undiagnosed Illness (38 CFR 3.317)"},
}

# Reverse index: condition name (lowercase) -> list of DC codes
_DC_BY_CONDITION: Dict[str, List[str]] = {}
for _dc, _info in DC_LOOKUP.items():
    for _word in _info["condition"].lower().replace("(", "").replace(")", "").split():
        _DC_BY_CONDITION.setdefault(_word, []).append(_dc)

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
    outcome: Optional[str] = None
    decision_type: Optional[str] = None
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
    model_config = ConfigDict(extra="forbid")
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

class DiagnosticCode(BaseModel):
    dc: str
    condition: str
    cfr_citation: str
    part: str
    section: str
    schedule: str

# Federal Register models
class FederalRegisterDocument(BaseModel):
    document_number: str
    title: str
    type: str  # Rule, Proposed Rule, Notice, Presidential Document
    abstract: Optional[str]
    citation: Optional[str]
    publication_date: str
    agencies: List[str]
    html_url: str
    pdf_url: Optional[str]
    cfr_references: Optional[List[str]]
    action: Optional[str]
    dates: Optional[str]
    effective_on: Optional[str]
    comments_close_on: Optional[str]

class FederalRegisterResponse(BaseModel):
    query: Optional[str]
    total: int
    page: int
    per_page: int
    results: List[FederalRegisterDocument]
    retrieved_at: str

# -------------------------------------------------------------------
# CAVC response models
# -------------------------------------------------------------------
class CavcSearchResult(BaseModel):
    case_number: str
    title: str
    opening_date: str
    last_docket_entry: str
    origin: str

class CavcParty(BaseModel):
    name: str
    role: str
    attorneys: List[str]

class CavcDocketEntry(BaseModel):
    date: str
    text: str
    dls_id: Optional[str] = None
    case_id: Optional[str] = None
    doc_url: Optional[str] = None

class CaseSummaryResponse(BaseModel):
    case_number: str
    title: str
    docketed: str
    appeal_from: str
    fee_status: str
    case_type: str
    parties: List[CavcParty]
    docket_entries: List[CavcDocketEntry]
    internal_case_id: Optional[str] = None

class CaseSummaryBriefResponse(BaseModel):
    case_number: str
    title: str
    docketed: str
    appeal_from: str
    fee_status: str
    case_type: str
    parties: List[CavcParty]
    docket_entries_count: int
    internal_case_id: Optional[str] = None

class CavcDocumentResponse(BaseModel):
    dls_id: str
    case_id: str
    case_number: str
    text: str
    char_count: int

class CaseSearchRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    q: Optional[str] = None
    preset: Optional[str] = None
    section: Optional[str] = None
    before: int = Field(default=400, ge=0, le=2000)
    after: int = Field(default=400, ge=0, le=2000)
    max_matches: int = Field(default=50, ge=1, le=200)
    context_mode: str = Field(default="chars", pattern=r"^(chars|sentences|paragraph)$")

class CaseSearchMatch(BaseModel):
    section: str
    start: int
    end: int
    match_text: str
    snippet: str
    line: int

class CaseSearchResponse(BaseModel):
    url: str
    total_matches: int
    truncated: bool
    preset_used: Optional[str]
    pattern: str
    section_filter: Optional[str]
    sections_found: List[str]
    matches: List[CaseSearchMatch]

# Search extract models
class ExtractRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    queries: List[str] = Field(..., min_length=1, description="Search queries to run")
    keywords: List[str] = Field(..., min_length=1, description="Keywords for proximity matching")
    year: Optional[int] = None
    proximity: int = Field(500, ge=50, le=2000, description="Max chars between keywords to form a cluster")
    context_sentences: int = Field(2, ge=0, le=5, description="Sentences before/after each passage")
    max_cases: int = Field(100, ge=1, le=500, description="Max cases to fetch and scan")
    top_n: int = Field(20, ge=1, le=100, description="Return extracts for top N cases")
    max_passages: int = Field(5, ge=1, le=20, description="Max passages per case")

class Passage(BaseModel):
    text: str
    keywords_matched: List[str]
    keyword_count: int
    min_distance: int
    offset: int

class ExtractCase(BaseModel):
    url: str
    case_number: Optional[str]
    year: Optional[int]
    title: str
    score: float
    keyword_hits: Dict[str, int]
    outcome: Optional[str]
    passages: List[Passage]

class ExtractResponse(BaseModel):
    total_searched: int
    total_matched: int
    cases: List[ExtractCase]
    keywords: List[str]
    timestamp: str

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

def _extract_outcome_from_snippet(snippet: str) -> Optional[str]:
    """Extract outcome from a search snippet using OUTCOME_PATTERNS."""
    found = [label for label, pat in OUTCOME_PATTERNS if pat.search(snippet)]
    if len(found) > 1:
        return "Mixed"
    return found[0] if found else None

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

# -------------------------------------------------------------------
# Section parsing for structured regex search
# -------------------------------------------------------------------

from dataclasses import dataclass, asdict
from functools import lru_cache

@dataclass
class TextSection:
    name: str
    start: int
    end: int

# Headings found in BVA decisions (order roughly matches typical layout)
_SECTION_HEADINGS = [
    re.compile(r"^\s*THE\s+ISSUES?\s*$", re.I | re.M),
    re.compile(r"^\s*REPRESENTATION\s*$", re.I | re.M),
    re.compile(r"^\s*WITNESSES?\s*$", re.I | re.M),
    re.compile(r"^\s*INTRODUCTION\s*$", re.I | re.M),
    re.compile(r"^\s*FINDINGS?\s+OF\s+FACT\s*$", re.I | re.M),
    re.compile(r"^\s*CONCLUSIONS?\s+OF\s+LAW\s*$", re.I | re.M),
    re.compile(r"^\s*REASONS\s+AND\s+BASES\s+FOR\s+FINDINGS?\s+AND\s+CONCLUSIONS?\s*$", re.I | re.M),
    re.compile(r"^\s*ORDER\s*$", re.I | re.M),
    re.compile(r"^\s*REMAND\s*$", re.I | re.M),
]

# Canonical short names for each heading
_SECTION_NAMES = {
    "THE ISSUE": "THE ISSUES",
    "THE ISSUES": "THE ISSUES",
    "REPRESENTATION": "REPRESENTATION",
    "WITNESS": "WITNESSES",
    "WITNESSES": "WITNESSES",
    "INTRODUCTION": "INTRODUCTION",
    "FINDING OF FACT": "FINDINGS OF FACT",
    "FINDINGS OF FACT": "FINDINGS OF FACT",
    "CONCLUSION OF LAW": "CONCLUSIONS OF LAW",
    "CONCLUSIONS OF LAW": "CONCLUSIONS OF LAW",
    "REASONS AND BASES FOR FINDING AND CONCLUSION": "REASONS AND BASES",
    "REASONS AND BASES FOR FINDINGS AND CONCLUSION": "REASONS AND BASES",
    "REASONS AND BASES FOR FINDING AND CONCLUSIONS": "REASONS AND BASES",
    "REASONS AND BASES FOR FINDINGS AND CONCLUSIONS": "REASONS AND BASES",
    "ORDER": "ORDER",
    "REMAND": "REMAND",
}


def parse_sections(text: str) -> list[TextSection]:
    """Scan text for BVA decision headings, return list of sections with char offsets."""
    hits: list[tuple[int, str]] = []
    for pat in _SECTION_HEADINGS:
        for m in pat.finditer(text):
            raw_name = m.group(0).strip().upper()
            canonical = _SECTION_NAMES.get(raw_name, raw_name)
            hits.append((m.start(), canonical))

    hits.sort(key=lambda h: h[0])

    if not hits:
        return [TextSection(name="FULL_TEXT", start=0, end=len(text))]

    sections: list[TextSection] = []
    # Preamble before first heading
    if hits[0][0] > 0:
        sections.append(TextSection(name="PREAMBLE", start=0, end=hits[0][0]))

    for i, (offset, name) in enumerate(hits):
        end = hits[i + 1][0] if i + 1 < len(hits) else len(text)
        sections.append(TextSection(name=name, start=offset, end=end))

    return sections


def _build_newline_offsets(text: str) -> list[int]:
    """Return list of char offsets where each line starts (0-indexed)."""
    offsets = [0]
    for i, ch in enumerate(text):
        if ch == "\n":
            offsets.append(i + 1)
    return offsets


def _offset_to_line(offset: int, newline_offsets: list[int]) -> int:
    """Convert a char offset to a 1-based line number using binary search."""
    import bisect
    return bisect.bisect_right(newline_offsets, offset)


@lru_cache(maxsize=64)
def _fetch_and_parse(url: str) -> tuple[str, tuple, tuple]:
    """Fetch case text and return (raw_text, sections_tuple, newline_offsets_tuple).

    Uses tuples for LRU cache hashability. Caller should convert back to lists.
    """
    data = fetch_case_text(url)
    raw = data["raw_text"]
    sections = parse_sections(raw)
    newline_offsets = _build_newline_offsets(raw)
    return (
        raw,
        tuple((s.name, s.start, s.end) for s in sections),
        tuple(newline_offsets),
    )

# -------------------------------------------------------------------
# BVA-specific regex presets
# -------------------------------------------------------------------

SEARCH_PRESETS: dict[str, tuple[re.Pattern, str]] = {
    "cfr_citation": (
        re.compile(r"\b38\s*C\.?F\.?R\.?\s*§?\s*[\d\.]+[a-z0-9()]*", re.I),
        "38 CFR regulatory citations (e.g., 38 CFR § 3.303)",
    ),
    "diagnostic_code": (
        re.compile(r"\b(?:DC|Diagnostic\s*Code)\s*\d{4}\b", re.I),
        "VA Diagnostic Codes (e.g., DC 9411 for PTSD)",
    ),
    "nexus_opinion": (
        re.compile(
            r"\b(at\s+least\s+as\s+likely\s+as\s+not"
            r"|more\s+likely\s+than\s+not"
            r"|less\s+likely\s+than\s+not)\b", re.I
        ),
        "Nexus opinion probability language",
    ),
    "secondary_sc": (
        re.compile(
            r"\b(secondary\s+service\s+connection"
            r"|proximately\s+due\s+to"
            r"|aggravated\s+by)\b", re.I
        ),
        "Secondary service connection theories",
    ),
    "effective_date": (
        re.compile(r"\b[Ee]ffective\s+[Dd]ate\b"),
        "Effective date references",
    ),
    "cue": (
        re.compile(r"\b[Cc]lear\s+and\s+[Uu]nmistakable\s+[Ee]rror\b"),
        "Clear and Unmistakable Error (CUE) references",
    ),
    "tdiu": (
        re.compile(
            r"\b(TDIU"
            r"|[Tt]otal\s+[Dd]isability\s+.*?[Ii]ndividual\s+[Uu]nemployability)\b"
        ),
        "Total Disability / Individual Unemployability",
    ),
    "imo": (
        re.compile(
            r"\b(IMO|IME"
            r"|[Ii]ndependent\s+[Mm]edical\s+(?:opinion|examination)"
            r"|nexus\s+(?:letter|opinion))\b"
        ),
        "Independent medical opinions/examinations and nexus letters",
    ),
    "buddy_statement": (
        re.compile(
            r"\b([Bb]uddy\s+[Ss]tatement"
            r"|[Ll]ay\s+[Ss]tatement"
            r"|[Ll]ay\s+[Ee]vidence)\b"
        ),
        "Buddy/lay statements and lay evidence references",
    ),
}

# -------------------------------------------------------------------
# Case text regex search engine
# -------------------------------------------------------------------

def _extract_snippet(text: str, start: int, end: int,
                     before: int, after: int,
                     section_start: int, section_end: int,
                     context_mode: str) -> str:
    """Extract context around a match, bounded to section."""
    budget = before + after

    if context_mode == "paragraph":
        # Find paragraph boundaries (double newline)
        para_start = text.rfind("\n\n", section_start, start)
        para_start = para_start + 2 if para_start != -1 else section_start
        para_end = text.find("\n\n", end, section_end)
        para_end = para_end if para_end != -1 else section_end
        snippet = text[para_start:para_end].strip()
        if len(snippet) > budget:
            snippet = snippet[:budget] + "..."
        return snippet

    if context_mode == "sentences":
        # Expand to sentence boundaries (period + space or newline)
        sent_start = max(
            text.rfind(". ", section_start, start),
            text.rfind(".\n", section_start, start),
        )
        sent_start = sent_start + 2 if sent_start != -1 else max(start - before, section_start)
        sent_end = min(
            x for x in [
                text.find(". ", end, section_end),
                text.find(".\n", end, section_end),
            ] if x != -1
        ) if any(
            text.find(p, end, section_end) != -1 for p in [". ", ".\n"]
        ) else min(end + after, section_end)
        sent_end = min(sent_end + 1, section_end)
        snippet = text[sent_start:sent_end].strip()
        if len(snippet) > budget:
            snippet = snippet[:budget] + "..."
        return snippet

    # Default: chars mode
    snip_start = max(start - before, section_start)
    snip_end = min(end + after, section_end)
    return text[snip_start:snip_end]


def search_case_text(
    raw_text: str,
    sections: list[TextSection],
    newline_offsets: list[int],
    pattern: re.Pattern,
    section_filter: str | None,
    before: int,
    after: int,
    max_matches: int,
    context_mode: str,
) -> tuple[list, int, bool]:
    """Run regex over case text, return (matches, total_found, truncated)."""
    # Determine which sections to search
    if section_filter:
        target_sections = [s for s in sections if section_filter.upper() in s.name]
    else:
        target_sections = sections

    all_matches: list = []
    total = 0

    for sec in target_sections:
        region = raw_text[sec.start:sec.end]
        for m in pattern.finditer(region):
            total += 1
            if len(all_matches) >= max_matches:
                continue  # keep counting total but don't add more
            abs_start = sec.start + m.start()
            abs_end = sec.start + m.end()
            snippet = _extract_snippet(
                raw_text, abs_start, abs_end,
                before, after,
                sec.start, sec.end,
                context_mode,
            )
            all_matches.append({
                "section": sec.name,
                "start": abs_start,
                "end": abs_end,
                "match_text": m.group(0),
                "snippet": snippet,
                "line": _offset_to_line(abs_start, newline_offsets),
            })

    return all_matches, total, total > max_matches

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
        snippet = clean_snippet(r.get("snippet", ""))
        results.append(SearchResult(
            url=result_url,
            title=r.get("title", "").replace(".txt", ""),
            snippet=snippet,
            outcome=_extract_outcome_from_snippet(snippet),
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
        raise BVAAPIError(422, "empty_content", "Invalid or empty case content",
                          field="url", suggested_fix="Verify the URL points to a valid BVA decision .txt file")
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
# Extract helpers
# -------------------------------------------------------------------
def _find_keyword_positions(text: str, keywords: List[str]) -> Dict[str, List[int]]:
    """Return sorted char positions for each keyword in text."""
    positions: Dict[str, List[int]] = {}
    text_lower = text.lower()
    for kw in keywords:
        kw_lower = kw.lower()
        positions[kw] = [m.start() for m in re.finditer(re.escape(kw_lower), text_lower)]
    return positions

def _cluster_positions(positions_by_kw: Dict[str, List[int]], proximity: int):
    """Group keyword positions into clusters where keywords are within proximity chars."""
    # Collect all positions with their keyword
    all_pos = []
    for kw, positions in positions_by_kw.items():
        for pos in positions:
            all_pos.append((pos, kw))
    if not all_pos:
        return []
    all_pos.sort(key=lambda x: x[0])

    # Greedy clustering: merge positions within proximity
    clusters = []
    current_start = all_pos[0][0]
    current_end = all_pos[0][0]
    current_kws = {all_pos[0][1]}
    current_positions = [all_pos[0]]

    for pos, kw in all_pos[1:]:
        if pos - current_start <= proximity:
            current_end = max(current_end, pos)
            current_kws.add(kw)
            current_positions.append((pos, kw))
        else:
            # Calculate min distance between any two different keywords
            min_dist = _min_inter_keyword_dist(current_positions)
            clusters.append((current_start, current_end, list(current_kws), min_dist))
            current_start = pos
            current_end = pos
            current_kws = {kw}
            current_positions = [(pos, kw)]

    min_dist = _min_inter_keyword_dist(current_positions)
    clusters.append((current_start, current_end, list(current_kws), min_dist))
    return clusters

def _min_inter_keyword_dist(positions):
    """Min distance between positions of different keywords."""
    if len(set(kw for _, kw in positions)) < 2:
        return -1
    min_d = float('inf')
    for i, (p1, k1) in enumerate(positions):
        for p2, k2 in positions[i+1:]:
            if k1 != k2:
                min_d = min(min_d, abs(p2 - p1))
    return int(min_d)

def _expand_to_sentences(text: str, start: int, end: int, context_sentences: int) -> tuple:
    """Expand char range to sentence boundaries with context. Returns (expanded_start, expanded_end)."""
    # Find sentence boundaries using period/exclamation/question followed by whitespace
    sentence_ends = [m.end() for m in re.finditer(r'[.!?]\s+', text)]
    if not sentence_ends:
        # No sentence boundaries found, use paragraph-ish boundaries
        return max(0, start - 200), min(len(text), end + 200)

    # Find the sentence boundary before start
    exp_start = 0
    for i, se in enumerate(sentence_ends):
        if se <= start:
            exp_start = se
        else:
            break
    # Go back N more sentences for context
    idx = sentence_ends.index(exp_start) if exp_start in sentence_ends else -1
    if idx >= 0 and context_sentences > 0:
        target_idx = max(0, idx - context_sentences)
        exp_start = sentence_ends[target_idx] if target_idx > 0 else 0
    elif exp_start > 0 and context_sentences == 0:
        pass  # keep exp_start as is
    else:
        exp_start = 0

    # Find the sentence boundary after end
    exp_end = len(text)
    for se in sentence_ends:
        if se >= end:
            exp_end = se
            break
    # Go forward N more sentences for context
    if exp_end in sentence_ends:
        idx = sentence_ends.index(exp_end)
        target_idx = min(len(sentence_ends) - 1, idx + context_sentences)
        exp_end = sentence_ends[target_idx]

    return exp_start, exp_end

def _score_case(clusters, num_keywords: int) -> float:
    """Score 0-1 based on keyword coverage and proximity in best cluster."""
    if not clusters or num_keywords == 0:
        return 0.0
    # Find best cluster by keyword coverage then proximity
    best = max(clusters, key=lambda c: (len(c[2]), -c[3] if c[3] >= 0 else float('inf')))
    coverage = len(best[2]) / num_keywords
    # Proximity bonus: closer is better, normalize against 2000 char max
    if best[3] > 0:
        prox_bonus = max(0, 1.0 - best[3] / 2000.0)
    else:
        prox_bonus = 0.0
    return round(coverage * 0.7 + prox_bonus * 0.3, 4)

def _extract_passages(text: str, keywords: List[str], proximity: int,
                      context_sentences: int, max_passages: int) -> List[dict]:
    """Find keyword clusters, expand to sentences, return top passages."""
    positions_by_kw = _find_keyword_positions(text, keywords)
    if not any(positions_by_kw.values()):
        return []

    clusters = _cluster_positions(positions_by_kw, proximity)
    if not clusters:
        return []

    # Sort: more keywords matched first, then closer proximity
    clusters.sort(key=lambda c: (-len(c[2]), c[3] if c[3] >= 0 else float('inf')))

    passages = []
    seen_ranges = []
    for start, end, matched_kws, min_dist in clusters[:max_passages * 2]:
        exp_start, exp_end = _expand_to_sentences(text, start, end, context_sentences)
        # Skip if overlaps significantly with an existing passage
        overlap = False
        for s, e in seen_ranges:
            overlap_start = max(s, exp_start)
            overlap_end = min(e, exp_end)
            if overlap_end > overlap_start and (overlap_end - overlap_start) > (exp_end - exp_start) * 0.5:
                overlap = True
                break
        if overlap:
            continue
        seen_ranges.append((exp_start, exp_end))
        passages.append({
            "text": text[exp_start:exp_end].strip(),
            "keywords_matched": sorted(matched_kws),
            "keyword_count": len(matched_kws),
            "min_distance": min_dist,
            "offset": exp_start,
        })
        if len(passages) >= max_passages:
            break
    return passages

def _fetch_and_extract(url: str, title: str, keywords: List[str], proximity: int,
                       context_sentences: int, max_passages: int) -> Optional[dict]:
    """Fetch case text and extract keyword passages. Returns dict or None on failure."""
    try:
        session = requests.Session()
        session.headers.update({"User-Agent": USER_AGENT})
        resp = session.get(url, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        text = resp.text
        if not text or len(text) < 100:
            return None

        passages = _extract_passages(text, keywords, proximity, context_sentences, max_passages)
        if not passages:
            return None

        parsed = parse_decision_text(text)
        positions_by_kw = _find_keyword_positions(text, keywords)
        keyword_hits = {kw: len(pos) for kw, pos in positions_by_kw.items() if pos}

        clusters = _cluster_positions(positions_by_kw, proximity)
        score = _score_case(clusters, len(keywords))

        return {
            "url": url,
            "case_number": extract_case_number(url),
            "year": extract_year_from_url(url),
            "title": title,
            "score": score,
            "keyword_hits": keyword_hits,
            "outcome": parsed.get("outcome"),
            "passages": passages,
        }
    except Exception as e:
        logger.warning(f"Extract failed for {url}: {e}")
        return None

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
            "POST /search/extract":          "Search + extract keyword passages from cases",
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
            "GET  /federal-register/va":     "Recent VA Federal Register documents (rules, notices)",
            "GET  /federal-register/search?q=": "Search VA Federal Register documents",
            "GET  /rag/search?q=":           "Semantic search over indexed CFR/KnowVA content",
            "GET  /rag/status":              "RAG index statistics",
            "POST /rag/reindex?source=":     "Re-index content into RAG",
            "POST /case/search":             "Regex search within case text (presets or custom)",
            "GET  /case/search/presets":     "List available search presets",
            "GET  /health":                  "Health check",
        }
    }

@app.get("/search", response_model=SearchResponse, tags=["Search"],
    summary="Search BVA decisions by keyword",
    description="Search BVA decisions by keyword. For multiple queries, use POST /batch/search instead. "
                "Do NOT paginate beyond page=5 unless you need exhaustive results.",
)
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
        raise BVAAPIError(422, "empty_field", "queries list is empty after trimming whitespace",
                          field="queries", suggested_fix="Provide at least one non-empty query string")
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

@app.post("/search/extract", response_model=ExtractResponse, tags=["Search"],
    summary="Search + extract keyword passages from BVA decisions",
    description="Searches BVA decisions and extracts only passages where keywords appear near each other. "
                "Use this BEFORE downloading full case text. Do NOT set max_cases above 100 unless you need "
                "exhaustive coverage. Start with top_n=10 and increase only if needed.",
    responses={422: {"model": APIError, "description": "Validation error with suggested fix"}},
)
async def search_extract(req: ExtractRequest = Body(...)):
    """Search BVA decisions and extract passages where keywords appear near each other."""
    queries = [q.strip() for q in req.queries if q.strip()]
    keywords = [k.strip() for k in req.keywords if k.strip()]
    if not queries:
        raise BVAAPIError(422, "empty_field", "queries list is empty after trimming whitespace",
                          field="queries", suggested_fix="Provide at least one non-empty query string")
    if not keywords:
        raise BVAAPIError(422, "empty_field", "keywords list is empty after trimming whitespace",
                          field="keywords", suggested_fix="Provide at least one keyword for proximity matching")

    loop = asyncio.get_running_loop()

    # 1. Collect unique case URLs from search queries
    seen_urls = set()
    case_items = []  # (url, title)
    for q in queries:
        try:
            data = await loop.run_in_executor(executor, search_bva, q, req.year, 1)
            for r in data["results"]:
                if r.url not in seen_urls and len(case_items) < req.max_cases:
                    seen_urls.add(r.url)
                    case_items.append((r.url, r.title))
            await asyncio.sleep(0.5)
        except Exception as e:
            logger.error(f"Extract search error for '{q}': {e}")

    if not case_items:
        return ExtractResponse(
            total_searched=0, total_matched=0, cases=[],
            keywords=keywords, timestamp=datetime.now().isoformat(),
        )

    # 2. Fetch + extract in parallel
    tasks = [
        loop.run_in_executor(
            executor, _fetch_and_extract,
            url, title, keywords, req.proximity, req.context_sentences, req.max_passages,
        )
        for url, title in case_items
    ]
    results = await asyncio.gather(*tasks)

    # 3. Filter and sort
    matched = [r for r in results if r is not None]
    matched.sort(key=lambda c: c["score"], reverse=True)
    top = matched[:req.top_n]

    # 4. Build response
    cases = [
        ExtractCase(
            url=c["url"],
            case_number=c["case_number"],
            year=c["year"],
            title=c["title"],
            score=c["score"],
            keyword_hits=c["keyword_hits"],
            outcome=c["outcome"],
            passages=[Passage(**p) for p in c["passages"]],
        )
        for c in top
    ]

    return ExtractResponse(
        total_searched=len(case_items),
        total_matched=len(matched),
        cases=cases,
        keywords=keywords,
        timestamp=datetime.now().isoformat(),
    )

@app.get("/case", response_model=CaseDetail, tags=["Case"],
    summary="Fetch parsed case details",
    description="Fetch parsed case details. Do NOT set full_text=true unless you need the complete "
                "decision text -- use /search/extract or /case/search for targeted extraction.",
)
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

@app.get("/case/text", tags=["Case"],
    summary="Fetch raw case text",
    description="Returns the FULL raw decision text (10-40 pages). Do NOT use this for keyword searching -- "
                "use POST /search/extract or POST /case/search instead. Only use when you need the complete document.",
)
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

@app.get("/case/search/presets")
async def list_search_presets():
    """List available BVA-specific regex search presets."""
    return {
        name: desc for name, (_, desc) in SEARCH_PRESETS.items()
    }


@app.post("/case/search", response_model=CaseSearchResponse, tags=["Case"],
    summary="Regex or preset search within a BVA case",
    description="Regex or preset search within a single BVA case. Do NOT use custom regex unless presets "
                "are insufficient -- presets are faster and safer. Call GET /case/search/presets first.",
    responses={422: {"model": APIError, "description": "Validation error with suggested fix"}},
)
async def case_search(req: CaseSearchRequest):
    """Search BVA case text with regex or preset, scoped to decision sections."""
    # Validate: exactly one of q or preset
    if not req.q and not req.preset:
        raise BVAAPIError(400, "missing_param", "Provide either q (regex) or preset",
                          field="q/preset", allowed=["q", "preset"],
                          suggested_fix="Use preset='nexus_opinion' OR q='your regex'")
    if req.q and req.preset:
        raise BVAAPIError(400, "exclusive_params", "q and preset are mutually exclusive",
                          field="q/preset", allowed=["q", "preset"],
                          suggested_fix="Use preset='nexus_opinion' OR q='your regex', not both")

    # Resolve pattern
    if req.preset:
        entry = SEARCH_PRESETS.get(req.preset)
        if not entry:
            raise BVAAPIError(400, "invalid_preset", f"Unknown preset '{req.preset}'",
                              field="preset", allowed=list(SEARCH_PRESETS.keys()),
                              suggested_fix=f"Use one of: {', '.join(SEARCH_PRESETS.keys())}")
        pattern, _ = entry
        pattern_str = pattern.pattern
    else:
        # User-supplied regex with timeout protection
        pattern_str = req.q
        try:
            pattern = re.compile(req.q, re.IGNORECASE)
        except re.error as e:
            raise BVAAPIError(400, "invalid_regex", str(e), field="q",
                              suggested_fix="Use a simpler pattern or try a preset: cfr_citation, nexus_opinion, tdiu")

    # Fetch + parse case text (LRU cached)
    loop = asyncio.get_running_loop()
    try:
        raw_text, sections_tuple, nl_offsets_tuple = await loop.run_in_executor(
            executor, _fetch_and_parse, req.url
        )
    except HTTPException:
        raise
    except Exception as e:
        raise BVAAPIError(404, "fetch_failed", f"Could not fetch case text: {e}",
                          field="url", suggested_fix="Verify the URL is a valid BVA decision URL from search results")

    sections = [TextSection(name=s[0], start=s[1], end=s[2]) for s in sections_tuple]
    newline_offsets = list(nl_offsets_tuple)

    # Validate section filter
    section_names = [s.name for s in sections]
    if req.section:
        matching = [s for s in sections if req.section.upper() in s.name]
        if not matching:
            raise BVAAPIError(400, "invalid_section", f"Section '{req.section}' not found",
                              field="section", allowed=section_names,
                              suggested_fix=f"Use one of: {', '.join(section_names)}")

    # Run search with timeout for user-supplied patterns
    from concurrent.futures import TimeoutError as FuturesTimeout

    def _do_search():
        return search_case_text(
            raw_text, sections, newline_offsets,
            pattern, req.section,
            req.before, req.after,
            req.max_matches, req.context_mode,
        )

    if req.q:
        # User-supplied regex gets a 2-second timeout
        future = executor.submit(_do_search)
        try:
            matches, total, truncated = future.result(timeout=2.0)
        except FuturesTimeout:
            future.cancel()
            raise BVAAPIError(408, "regex_timeout", "Pattern took >2s",
                              field="q", suggested_fix="Use a preset instead of custom regex, or simplify your pattern")
    else:
        matches, total, truncated = _do_search()

    return CaseSearchResponse(
        url=req.url,
        total_matches=total,
        truncated=truncated,
        preset_used=req.preset,
        pattern=pattern_str,
        section_filter=req.section,
        sections_found=section_names,
        matches=[CaseSearchMatch(**m) for m in matches],
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
    # Renderer API returns enhanced HTML with redirects; section param needs full "part.section" form
    url = "https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-38"
    session = requests.Session()
    session.headers.update(ECFR_HEADERS)
    resp = session.get(url, params={"part": part, "section": f"{part}.{section}"},
                       timeout=REQUEST_TIMEOUT, allow_redirects=True)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    # Remove metadata noise
    for tag in soup.find_all(["script", "style"]):
        tag.decompose()
    markdown = _clean_html_to_text(str(soup))
    return CFRSectionResponse(
        part=part, section=section,
        citation=f"38 CFR \u00a7 {part}.{section}",
        content_markdown=markdown,
        retrieved_at=datetime.now().isoformat(),
    )

def _ecfr_search_sync(query: str, page: int, per_page: int,
                      part: Optional[str] = None) -> Dict:
    """Search eCFR, filter to Title 38, deduplicate by section, strip HTML."""
    session = requests.Session()
    session.headers.update(ECFR_HEADERS)
    results = []
    seen_sections = set()
    api_page = 1
    max_api_pages = 10

    while len(results) < per_page and api_page <= max_api_pages:
        resp = session.get(ECFR_SEARCH_BASE,
                           params={"query": query, "per_page": 100, "page": api_page},
                           timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        raw = data.get("results", [])
        if not raw:
            break

        for r in raw:
            hier = r.get("hierarchy", {})
            if hier.get("title") != "38":
                continue
            part_num = hier.get("part") or None
            if part and part_num != part:
                continue
            sec_num = hier.get("section") or None
            dedup_key = f"{part_num}:{sec_num}"
            if dedup_key in seen_sections:
                continue
            seen_sections.add(dedup_key)
            headings = r.get("headings", {})
            hier_hdrs = r.get("hierarchy_headings", {})
            label = headings.get("section") or headings.get("part") or ""
            label = re.sub(r"<[^>]+>", "", label)
            snippet = r.get("full_text_excerpt") or ""
            snippet = re.sub(r"<[^>]+>", "", snippet)
            hier_list = [v for v in hier_hdrs.values() if v] if hier_hdrs else None
            results.append(CFRSearchResult(
                title=38, part=part_num, section=sec_num,
                label=label,
                snippet=snippet or None,
                score=r.get("score"),
                hierarchy=hier_list,
            ))
            if len(results) >= per_page:
                break

        total_pages = data.get("meta", {}).get("total_pages", 0)
        if api_page >= total_pages:
            break
        api_page += 1

    # Skip results for pagination
    start = (page - 1) * per_page
    paged = results[start:start + per_page]
    return {"total": len(results), "results": paged}

def _fr_parse_doc(doc: dict) -> FederalRegisterDocument:
    """Parse a Federal Register API document into our model."""
    agencies = [a.get("name", "") for a in doc.get("agencies", []) if a.get("name")]
    cfr_refs = []
    for ref in doc.get("cfr_references", []) or []:
        title = ref.get("title")
        parts = ref.get("parts", [])
        for p in parts:
            cfr_refs.append(f"{title} CFR Part {p.get('part', '?')}")
        if not parts and title:
            cfr_refs.append(f"{title} CFR")
    return FederalRegisterDocument(
        document_number=doc.get("document_number", ""),
        title=doc.get("title", ""),
        type=doc.get("type", ""),
        abstract=doc.get("abstract"),
        citation=doc.get("citation"),
        publication_date=doc.get("publication_date", ""),
        agencies=agencies,
        html_url=doc.get("html_url", ""),
        pdf_url=doc.get("pdf_url"),
        cfr_references=cfr_refs or None,
        action=doc.get("action"),
        dates=doc.get("dates"),
        effective_on=doc.get("effective_on"),
        comments_close_on=doc.get("comments_close_on"),
    )

def _fr_va_documents_sync(
    doc_type: Optional[str] = None,
    page: int = 1,
    per_page: int = 20,
) -> Dict:
    """Fetch recent VA documents from the Federal Register."""
    params = {
        "conditions[agencies][]": FR_VA_SLUG,
        "fields[]": FR_FIELDS,
        "per_page": per_page,
        "page": page,
        "order": "newest",
    }
    if doc_type:
        params["conditions[type][]"] = doc_type
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})
    resp = session.get(f"{FR_API_BASE}/documents.json", params=params, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    results = [_fr_parse_doc(d) for d in data.get("results", [])]
    return {"total": data.get("count", 0), "results": results}

def _fr_search_sync(
    query: str,
    doc_type: Optional[str] = None,
    cfr_title: Optional[int] = None,
    cfr_part: Optional[str] = None,
    page: int = 1,
    per_page: int = 20,
) -> Dict:
    """Search VA documents in the Federal Register."""
    params = {
        "conditions[agencies][]": FR_VA_SLUG,
        "conditions[term]": query,
        "fields[]": FR_FIELDS,
        "per_page": per_page,
        "page": page,
        "order": "relevance",
    }
    if doc_type:
        params["conditions[type][]"] = doc_type
    if cfr_title and cfr_part:
        params["conditions[cfr][title]"] = cfr_title
        params["conditions[cfr][part]"] = cfr_part
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})
    resp = session.get(f"{FR_API_BASE}/documents.json", params=params, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    results = [_fr_parse_doc(d) for d in data.get("results", [])]
    return {"total": data.get("count", 0), "results": results}

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
        raise BVAAPIError(502, "upstream_error", str(e),
                          suggested_fix="Upstream service unavailable. Retry in a few seconds")

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
        raise BVAAPIError(502, "upstream_error", str(e),
                          suggested_fix="Upstream service unavailable. Retry in a few seconds")

@app.get("/knowva/article/{article_id}", response_model=KnowVAArticle, tags=["KnowVA"])
async def knowva_article(article_id: int):
    """Fetch full content of a KnowVA article by its numeric ID."""
    loop = asyncio.get_running_loop()
    try:
        return await loop.run_in_executor(executor, _knowva_article_sync, article_id)
    except Exception as e:
        logger.error(f"KnowVA article error: {e}")
        raise BVAAPIError(502, "upstream_error", str(e),
                          suggested_fix="Upstream service unavailable. Retry in a few seconds")

@app.get("/knowva/popular", response_model=List[KnowVAArticleSummary], tags=["KnowVA"])
async def knowva_popular(pagesize: int = Query(10, ge=1, le=50)):
    """Return the most popular KnowVA articles."""
    loop = asyncio.get_running_loop()
    try:
        return await loop.run_in_executor(executor, _knowva_popular_sync, pagesize)
    except Exception as e:
        logger.error(f"KnowVA popular error: {e}")
        raise BVAAPIError(502, "upstream_error", str(e),
                          suggested_fix="Upstream service unavailable. Retry in a few seconds")

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
        raise BVAAPIError(502, "upstream_error", str(e),
                          suggested_fix="Upstream service unavailable. Retry in a few seconds")

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
        raise BVAAPIError(502, "upstream_error", str(e),
                          suggested_fix="Upstream service unavailable. Retry in a few seconds")

@app.get("/cfr/search", response_model=CFRSearchResponse, tags=["38 CFR"])
async def cfr_search(
    q: str = Query(..., example="PTSD"),
    page: int = Query(1, ge=1, le=100),
    per_page: int = Query(20, ge=1, le=100),
    part: Optional[str] = Query(None, example="3", description="Filter to specific CFR part (e.g. 3, 4, 19)"),
):
    """Full-text search within Title 38 CFR regulations. Optionally scope to a specific part."""
    loop = asyncio.get_running_loop()
    try:
        data = await loop.run_in_executor(executor, _ecfr_search_sync, q, page, per_page, part)
        return CFRSearchResponse(
            query=q, page=page, per_page=per_page,
            total=data["total"], results=data["results"],
            retrieved_at=datetime.now().isoformat(),
        )
    except Exception as e:
        logger.error(f"eCFR search error q={q}: {e}")
        raise BVAAPIError(502, "upstream_error", str(e),
                          suggested_fix="Upstream service unavailable. Retry in a few seconds")

def _dc_to_model(dc: str, info: Dict[str, str]) -> DiagnosticCode:
    return DiagnosticCode(
        dc=dc, condition=info["condition"],
        cfr_citation=f"38 CFR \u00a7 {info['part']}.{info['section']}",
        part=info["part"], section=info["section"], schedule=info["schedule"],
    )

@app.get("/cfr/dc/{code}", response_model=DiagnosticCode, tags=["38 CFR"])
async def cfr_diagnostic_code(code: str):
    """Look up a VA diagnostic code (e.g. 9411 for PTSD). Returns CFR citation and schedule."""
    info = DC_LOOKUP.get(code)
    if not info:
        raise BVAAPIError(404, "not_found", f"Diagnostic code {code} not found in lookup table",
                          field="code", suggested_fix="Use bva_cfr_dc_search to search by condition name, e.g. 'PTSD' or 'sleep apnea'")
    return _dc_to_model(code, info)

@app.get("/cfr/dc", response_model=List[DiagnosticCode], tags=["38 CFR"])
async def cfr_diagnostic_search(
    q: str = Query(..., description="Condition name to search (e.g. PTSD, sleep apnea, tinnitus)"),
):
    """Search diagnostic codes by condition name. Returns matching DC codes with CFR citations."""
    q_lower = q.lower()
    matched_dcs = set()
    # Search by keyword overlap
    for word in q_lower.replace("(", "").replace(")", "").split():
        if len(word) < 2:
            continue
        for dc, info in DC_LOOKUP.items():
            if word in info["condition"].lower():
                matched_dcs.add(dc)
    # Also match against schedule name
    for dc, info in DC_LOOKUP.items():
        if q_lower in info["condition"].lower() or q_lower in info["schedule"].lower():
            matched_dcs.add(dc)
    if not matched_dcs:
        raise BVAAPIError(404, "not_found", f"No diagnostic codes matching '{q}'",
                          field="q", suggested_fix="Try broader terms like 'knee', 'back', 'anxiety'. Use bva_cfr_dc_lookup if you know the DC number")
    results = [_dc_to_model(dc, DC_LOOKUP[dc]) for dc in sorted(matched_dcs)]
    return results

# -------------------------------------------------------------------
# Federal Register endpoints
# -------------------------------------------------------------------
@app.get("/federal-register/va", response_model=FederalRegisterResponse, tags=["Federal Register"])
async def fr_va_documents(
    type: Optional[str] = Query(None, description="Document type: Rule, Proposed Rule, Notice"),
    page: int = Query(1, ge=1, le=100),
    per_page: int = Query(20, ge=1, le=100),
):
    """Get recent VA documents from the Federal Register (rules, proposed rules, notices)."""
    loop = asyncio.get_running_loop()
    try:
        data = await loop.run_in_executor(executor, _fr_va_documents_sync, type, page, per_page)
        return FederalRegisterResponse(
            query=None, total=data["total"], page=page, per_page=per_page,
            results=data["results"], retrieved_at=datetime.now().isoformat(),
        )
    except Exception as e:
        logger.error(f"Federal Register VA docs error: {e}")
        raise BVAAPIError(502, "upstream_error", str(e),
                          suggested_fix="Upstream service unavailable. Retry in a few seconds")

@app.get("/federal-register/search", response_model=FederalRegisterResponse, tags=["Federal Register"])
async def fr_search(
    q: str = Query(..., description="Search query"),
    type: Optional[str] = Query(None, description="Document type: Rule, Proposed Rule, Notice"),
    cfr_title: Optional[int] = Query(None, description="CFR title number (e.g. 38)"),
    cfr_part: Optional[str] = Query(None, description="CFR part number (e.g. 3, 4)"),
    page: int = Query(1, ge=1, le=100),
    per_page: int = Query(20, ge=1, le=100),
):
    """Search VA-related Federal Register documents. Filter by type and CFR reference."""
    loop = asyncio.get_running_loop()
    try:
        data = await loop.run_in_executor(
            executor, _fr_search_sync, q, type, cfr_title, cfr_part, page, per_page,
        )
        return FederalRegisterResponse(
            query=q, total=data["total"], page=page, per_page=per_page,
            results=data["results"], retrieved_at=datetime.now().isoformat(),
        )
    except Exception as e:
        logger.error(f"Federal Register search error: {e}")
        raise BVAAPIError(502, "upstream_error", str(e),
                          suggested_fix="Upstream service unavailable. Retry in a few seconds")

# -------------------------------------------------------------------
# RAG endpoints
# -------------------------------------------------------------------
import rag as _rag
from chunker import Chunk

class RAGSearchResponse(BaseModel):
    query: str
    top_k: int
    results: List[Dict[str, Any]]
    total_indexed: int

class RAGStatusResponse(BaseModel):
    total_chunks: int
    collection: str
    embedding_model: str
    by_source: Dict[str, int]
    by_content_type: Dict[str, int]

@app.get("/rag/search", response_model=RAGSearchResponse, tags=["RAG"],
    summary="Semantic search over CFR and KnowVA content",
    description="Semantic search over CFR and KnowVA content. Do NOT use for BVA case search -- "
                "use GET /search for that. This searches regulations and VA policy guidance only.",
)
async def rag_search(
    q: str = Query(..., description="Semantic search query"),
    content_type: Optional[str] = Query(None, description="Filter: rating_criteria, adjudication, guidance"),
    part: Optional[str] = Query(None, description="Filter: CFR part number (3, 4)"),
    schedule: Optional[str] = Query(None, description="Filter: rating schedule name"),
    source: Optional[str] = Query(None, description="Filter: cfr, knowva"),
    top_k: int = Query(5, ge=1, le=20, description="Number of results"),
):
    """Semantic search over indexed CFR sections and KnowVA articles."""
    try:
        results = _rag.search(
            query=q, top_k=top_k,
            content_type=content_type, part=part,
            schedule=schedule, source=source,
        )
        stats = _rag.get_stats()
        return RAGSearchResponse(
            query=q, top_k=top_k,
            results=results,
            total_indexed=stats["total_chunks"],
        )
    except Exception as e:
        logger.error(f"RAG search error: {e}")
        raise BVAAPIError(500, "internal_error", str(e),
                          suggested_fix="Internal error. Retry or try a different query")

@app.get("/rag/status", response_model=RAGStatusResponse, tags=["RAG"])
async def rag_status():
    """Return RAG index statistics."""
    try:
        stats = _rag.get_stats()
        return RAGStatusResponse(
            total_chunks=stats["total_chunks"],
            collection=stats["collection"],
            embedding_model=stats["embedding_model"],
            by_source=stats.get("by_source", {}),
            by_content_type=stats.get("by_content_type", {}),
        )
    except Exception as e:
        logger.error(f"RAG status error: {e}")
        raise BVAAPIError(500, "internal_error", str(e),
                          suggested_fix="Internal error. Retry or try a different query")

@app.post("/rag/reindex", tags=["RAG"])
async def rag_reindex(
    source: str = Query("all", description="Source to reindex: cfr, knowva, all"),
):
    """Trigger re-indexing of content into the RAG index."""
    from ingest import ingest_cfr_part3, ingest_cfr_part4, ingest_knowva
    api_url = os.environ.get("BVA_API_URL", "http://localhost:8001")
    loop = asyncio.get_running_loop()
    try:
        all_chunks: List[Chunk] = []
        if source in ("cfr", "all"):
            all_chunks.extend(await loop.run_in_executor(executor, ingest_cfr_part4, api_url))
            all_chunks.extend(await loop.run_in_executor(executor, ingest_cfr_part3, api_url))
        if source in ("knowva", "all"):
            all_chunks.extend(await loop.run_in_executor(executor, ingest_knowva, api_url))
        indexed = _rag.add_chunks(all_chunks)
        stats = _rag.get_stats()
        return {
            "status": "ok",
            "source": source,
            "chunks_indexed": indexed,
            "total_chunks": stats["total_chunks"],
        }
    except Exception as e:
        import traceback
        logger.error(f"RAG reindex error: {traceback.format_exc()}")
        raise BVAAPIError(500, "internal_error", f"{type(e).__name__}: {e}",
                          suggested_fix="Internal error. Retry or try a different query")

@app.get("/rag/debug", tags=["RAG"])
async def rag_debug():
    """Debug RAG configuration."""
    provider = os.environ.get("RAG_EMBEDDINGS", "vertex").lower()
    openai_key = os.environ.get("OPENAI_API_KEY", "")
    debug_info = {
        "embedding_provider": provider,
        "embedding_model": "text-embedding-004" if provider != "openai" else "text-embedding-3-small",
        "chroma_path": os.environ.get("CHROMA_PATH", "./data/chroma"),
        "bva_api_url": os.environ.get("BVA_API_URL", "http://localhost:8001"),
        "openai_key_set": bool(openai_key),
    }
    if provider == "vertex":
        try:
            import google.auth
            _, project = google.auth.default()
            debug_info["gcp_project"] = project
            debug_info["vertex_status"] = "credentials_ok"
        except Exception as e:
            debug_info["vertex_status"] = f"error: {e}"
    return debug_info

import dataclasses as _dc

def _dc_to_dict(obj):
    """Recursively convert a dataclass instance to a plain dict."""
    if _dc.is_dataclass(obj) and not isinstance(obj, type):
        return {k: _dc_to_dict(v) for k, v in _dc.asdict(obj).items()}
    if isinstance(obj, list):
        return [_dc_to_dict(i) for i in obj]
    return obj

# ---------------------------------------------------------------------------
# CAVC endpoints
# ---------------------------------------------------------------------------

@app.get("/cavc/search", response_model=List[CavcSearchResult], tags=["CAVC"],
         summary="Search CAVC cases by case number or party name",
         description="Search the CAVC eFiling portal. Returns matching cases with case numbers, titles, and dates.")
async def cavc_search(
    case_number: str = Query(""),
    party_name: str = Query(""),
    open_closed: str = Query("both"),
):
    """Search CAVC cases by case number or party name."""
    loop = asyncio.get_running_loop()
    results = await loop.run_in_executor(
        executor, lambda: cavc_client.search_cases(case_number, party_name, open_closed)
    )
    return [_dc_to_dict(r) for r in results]

@app.get("/cavc/case/{case_number}", response_model=CaseSummaryBriefResponse, tags=["CAVC"],
         summary="Fetch CAVC case summary",
         description="Returns parties, counsel, case metadata, and docket entry count. Use /docket for full entries.")
async def cavc_case(case_number: str):
    """Fetch CAVC case summary (parties, counsel, case info)."""
    loop = asyncio.get_running_loop()
    summary = await loop.run_in_executor(
        executor, lambda: cavc_client.get_case_summary(case_number)
    )
    if not summary:
        raise BVAAPIError(404, "not_found", f"Case {case_number} not found",
                          field="case_number", suggested_fix="Use bva_cavc_search to find valid case numbers first")
    d = _dc_to_dict(summary)
    d["docket_entries_count"] = len(summary.docket_entries)
    d.pop("docket_entries", None)
    return d

@app.get("/cavc/case/{case_number}/docket", response_model=CaseSummaryResponse, tags=["CAVC"],
         summary="Fetch full CAVC docket",
         description="Returns all docket entries with dates, text, and document link IDs (dls_id) for PDF fetching.")
async def cavc_docket(case_number: str):
    """Fetch full CAVC docket report with all entries and document links."""
    loop = asyncio.get_running_loop()
    summary = await loop.run_in_executor(
        executor, lambda: cavc_client.get_full_docket(case_number)
    )
    if not summary:
        raise BVAAPIError(404, "not_found", f"Case {case_number} not found",
                          field="case_number", suggested_fix="Use bva_cavc_search to find valid case numbers first")
    return _dc_to_dict(summary)

@app.get("/cavc/case/{case_number}/document", tags=["CAVC"],
         summary="Fetch a CAVC docket document",
         description="as_text=true returns JSON with extracted text. as_text=false returns raw PDF bytes.")
async def cavc_document(
    case_number: str,
    dls_id: str = Query(...),
    case_id: str = Query(...),
    as_text: bool = Query(False),
):
    """Fetch a CAVC docket document (PDF or extracted text)."""
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(
        executor, lambda: cavc_client.get_document(dls_id, case_id, as_text)
    )
    if result is None:
        raise BVAAPIError(404, "not_found", f"Document dls_id={dls_id} not found or restricted",
                          field="dls_id", suggested_fix="Get dls_id from docket entries via bva_cavc_case. Some documents may be sealed")
    if as_text and isinstance(result, str):
        return CavcDocumentResponse(
            dls_id=dls_id,
            case_id=case_id,
            case_number=case_number,
            text=result,
            char_count=len(result),
        )
    return Response(content=result, media_type="application/pdf")

@app.get("/cavc/case/{case_number}/find", response_model=CavcDocketEntry, tags=["CAVC"],
         summary="Find docket entry by keyword",
         description="Returns the first docket entry whose text contains the keyword. Use the returned dls_id and case_id to fetch the document.")
async def cavc_find_entry(
    case_number: str,
    keyword: str = Query(...),
):
    """Search docket entries for a keyword, return first match."""
    loop = asyncio.get_running_loop()
    entry = await loop.run_in_executor(
        executor, lambda: cavc_client.find_entry(case_number, keyword)
    )
    if not entry:
        raise BVAAPIError(404, "not_found", f"No docket entry matching '{keyword}' in case {case_number}",
                          field="keyword", suggested_fix="Try broader terms like 'brief', 'motion', 'order', 'mandate', or 'remand'")
    return _dc_to_dict(entry)

def _shutdown(signum, frame):
    logger.info("Shutting down -- releasing ports...")
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
