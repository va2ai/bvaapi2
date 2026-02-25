#!/usr/bin/env python3
"""BVA Decision Search MCP Server - wraps the BVA API for LLM tool use."""

import json
import os
from typing import Optional, List

import httpx
import uvicorn
from mcp.server.fastmcp import FastMCP
from starlette.middleware.cors import CORSMiddleware

_transport = os.environ.get("MCP_TRANSPORT", "stdio")
_host = "0.0.0.0" if _transport == "http" else "127.0.0.1"
_port = int(os.environ.get("PORT", 8080)) if _transport == "http" else 8000

mcp = FastMCP("bva_mcp", host=_host, port=_port)
API_BASE = os.environ.get("BVA_API_URL", "http://localhost:8001")
TIMEOUT = 30.0


# --- shared helpers ---

async def _get(path: str, **params) -> dict:
    filtered = {k: v for k, v in params.items() if v is not None}
    async with httpx.AsyncClient() as c:
        r = await c.get(f"{API_BASE}/{path}", params=filtered, timeout=TIMEOUT)
        r.raise_for_status()
        return r.json()


async def _post(path: str, body: dict) -> dict:
    async with httpx.AsyncClient() as c:
        r = await c.post(f"{API_BASE}/{path}", json=body, timeout=TIMEOUT)
        r.raise_for_status()
        return r.json()


def _err(e: Exception) -> str:
    if isinstance(e, httpx.HTTPStatusError):
        return f"HTTP {e.response.status_code}: {e.response.text[:300]}"
    if isinstance(e, httpx.TimeoutException):
        return "Request timed out after 30 seconds"
    if isinstance(e, httpx.ConnectError):
        return f"Could not connect to BVA API at {API_BASE}"
    return str(e)


# --- BVA Search tools ---

@mcp.tool(
    description=(
        "Search Board of Veterans' Appeals (BVA) decisions by keyword. "
        "Returns case URLs, titles, snippets, case numbers, and years. "
        "Filter by year (1992-2025) or paginate with page param."
    )
)
async def bva_search(
    q: str,
    year: Optional[int] = None,
    page: int = 1,
) -> str:
    """Search BVA decisions. q=search query, year=optional year filter (1992-2025), page=page number."""
    try:
        data = await _get("search", q=q, year=year, page=page)
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: {_err(e)}"


@mcp.tool(
    description=(
        "Run multiple BVA decision searches in a single call. "
        "Accepts a list of query strings and returns results for each. "
        "Useful for comparing outcomes across different conditions or topics."
    )
)
async def bva_batch_search(
    queries: List[str],
    year: Optional[int] = None,
    page: int = 1,
) -> str:
    """Batch search BVA decisions. queries=list of search strings, year=optional filter, page=page number."""
    try:
        body = {"queries": queries, "page": page}
        if year is not None:
            body["year"] = year
        data = await _post("batch/search", body)
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: {_err(e)}"


@mcp.tool(
    description=(
        "List all available BVA decision years and their search collection IDs. "
        "Use this to see which years have indexed decisions (1992-2025)."
    )
)
async def bva_list_years() -> str:
    """List available BVA decision years with their internal collection IDs."""
    try:
        data = await _get("years")
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: {_err(e)}"


# --- BVA Case tools ---

@mcp.tool(
    description=(
        "Fetch parsed details of a BVA decision by its URL. "
        "Returns structured data: case number, docket, decision date, outcome, "
        "judge, regional office, issues, citations, and a text preview. "
        "Use bva_search first to find case URLs."
    )
)
async def bva_get_case(
    url: str,
    full_text: bool = False,
) -> str:
    """Get parsed BVA case details. url=case URL from search results, full_text=include full decision text."""
    try:
        data = await _get("case", url=url, full_text=full_text)
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: {_err(e)}"


@mcp.tool(
    description=(
        "Fetch the raw plain text of a BVA decision. "
        "Returns the complete decision text as written. "
        "Use this when you need the full document for analysis."
    )
)
async def bva_get_case_text(url: str) -> str:
    """Get raw text of a BVA decision. url=case URL from search results."""
    try:
        async with httpx.AsyncClient() as c:
            r = await c.get(f"{API_BASE}/case/text", params={"url": url}, timeout=TIMEOUT)
            r.raise_for_status()
            return r.text
    except Exception as e:
        return f"Error: {_err(e)}"


@mcp.tool(
    description=(
        "Analyze a BVA decision for keyword frequency and VA-specific terms. "
        "Automatically counts TDIU, PTSD, service-connected, disability rating, "
        "effective date, clear and unmistakable error, and individual unemployability. "
        "Optionally pass keywords for custom term counts."
    )
)
async def bva_analyze_case(
    url: str,
    keywords: Optional[List[str]] = None,
) -> str:
    """Analyze a BVA decision for keyword frequency. url=case URL, keywords=optional list of terms to count."""
    try:
        params: dict = {"url": url}
        if keywords:
            # httpx accepts list params as repeated keys
            async with httpx.AsyncClient() as c:
                r = await c.get(
                    f"{API_BASE}/analyze/text",
                    params=[("url", url)] + [("keywords", k) for k in keywords],
                    timeout=TIMEOUT,
                )
                r.raise_for_status()
                return json.dumps(r.json(), indent=2)
        data = await _get("analyze/text", url=url)
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: {_err(e)}"


# --- KnowVA tools ---

@mcp.tool(
    description=(
        "Search KnowVA, the VA's official knowledge base. "
        "Returns articles about VA policy, M21-1 manual guidance, benefits procedures, "
        "and regulations. Results include article IDs for fetching full content."
    )
)
async def bva_knowva_search(
    q: str,
    page: int = 1,
    pagesize: int = 30,
) -> str:
    """Search the VA KnowVA knowledge base. q=search query, page=page number, pagesize=results per page."""
    try:
        data = await _get("knowva/search", q=q, page=page, pagesize=pagesize)
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: {_err(e)}"


@mcp.tool(
    description=(
        "Fetch the full text of a KnowVA article by its numeric ID. "
        "Returns the article name, last modified date, and full content as clean markdown. "
        "Get article IDs from bva_knowva_search or bva_knowva_popular."
    )
)
async def bva_knowva_article(article_id: int) -> str:
    """Fetch a KnowVA article by ID. article_id=numeric article ID from search results."""
    try:
        data = await _get(f"knowva/article/{article_id}")
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: {_err(e)}"


@mcp.tool(
    description=(
        "List all KnowVA knowledge base topics and categories. "
        "Returns topic IDs, names, parent topic IDs, and article counts. "
        "Use to browse the VA knowledge base hierarchy."
    )
)
async def bva_knowva_topics() -> str:
    """List all KnowVA topics and categories."""
    try:
        data = await _get("knowva/topics")
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: {_err(e)}"


@mcp.tool(
    description=(
        "List the most popular articles in the VA KnowVA knowledge base. "
        "Returns article IDs and names ranked by popularity. "
        "Use bva_knowva_article to fetch full content."
    )
)
async def bva_knowva_popular(pagesize: int = 10) -> str:
    """Get most popular KnowVA articles. pagesize=number of articles to return (1-50)."""
    try:
        data = await _get("knowva/popular", pagesize=pagesize)
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: {_err(e)}"


# --- 38 CFR tools ---

@mcp.tool(
    description=(
        "Search within Title 38 Code of Federal Regulations (VA regulations). "
        "Results are filtered to Title 38 only. Optionally scope to a specific part: "
        "Part 3 (Adjudication), Part 4 (Rating Disabilities), Part 19/20 (BVA Appeals). "
        "Returns matching sections with labels, snippets, and relevance scores."
    )
)
async def bva_cfr_search(
    q: str,
    part: Optional[str] = None,
    page: int = 1,
    per_page: int = 20,
) -> str:
    """Search 38 CFR regulations. q=search query, part=optional part filter (e.g. '3','4','19'), page=page number."""
    try:
        data = await _get("cfr/search", q=q, part=part, page=page, per_page=per_page)
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: {_err(e)}"


@mcp.tool(
    description=(
        "Fetch the full text of a 38 CFR section as clean markdown. "
        "Example: part='3', section='102' fetches 38 CFR ss 3.102 (benefit of the doubt). "
        "Common parts: 3=Adjudication, 4=Schedule for Rating Disabilities, 19=Board of Veterans' Appeals."
    )
)
async def bva_cfr_section(part: str, section: str) -> str:
    """Fetch a 38 CFR section. part=CFR part number (e.g. '3'), section=section number (e.g. '102')."""
    try:
        data = await _get("cfr/section", part=part, section=section)
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: {_err(e)}"


@mcp.tool(
    description=(
        "Get the full table of contents for Title 38 CFR (VA regulations). "
        "Returns all parts and sections with identifiers and labels. "
        "Use to discover regulation structure before fetching specific sections."
    )
)
async def bva_cfr_structure() -> str:
    """Get Title 38 CFR table of contents - all parts and sections."""
    try:
        data = await _get("cfr/structure")
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: {_err(e)}"


# --- Diagnostic Code tools ---

@mcp.tool(
    description=(
        "Look up a VA diagnostic code by number. Returns the condition name, "
        "38 CFR citation, and rating schedule. Example: code='9411' returns "
        "PTSD at 38 CFR 4.130. Covers 50+ common conditions across all body systems."
    )
)
async def bva_cfr_dc_lookup(code: str) -> str:
    """Look up a diagnostic code. code=DC number (e.g. '9411' for PTSD, '6847' for sleep apnea)."""
    try:
        data = await _get(f"cfr/dc/{code}")
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: {_err(e)}"


@mcp.tool(
    description=(
        "Search VA diagnostic codes by condition name. Returns matching DC codes "
        "with their 38 CFR citations. Use when you know the condition but not the "
        "DC number. Examples: 'PTSD', 'sleep apnea', 'knee', 'hearing loss', 'migraine'."
    )
)
async def bva_cfr_dc_search(q: str) -> str:
    """Search diagnostic codes by condition name. q=condition name (e.g. 'PTSD', 'back pain', 'tinnitus')."""
    try:
        data = await _get("cfr/dc", q=q)
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: {_err(e)}"


# --- RAG tools ---

@mcp.tool(
    description=(
        "Semantic search over indexed VA regulations (38 CFR Parts 3 & 4) and KnowVA articles. "
        "Use for discovery queries like 'what conditions qualify for presumptive service connection', "
        "cross-reference questions like 'how does 3.102 interact with 4.3', or explanation requests "
        "like 'what does occupational impairment mean'. Filters: content_type (rating_criteria, "
        "adjudication, guidance), part (3, 4), schedule (Mental Disorders, etc.), source (cfr, knowva)."
    )
)
async def bva_rag_search(
    q: str,
    content_type: Optional[str] = None,
    part: Optional[str] = None,
    schedule: Optional[str] = None,
    source: Optional[str] = None,
    top_k: int = 5,
) -> str:
    """Semantic search over CFR and KnowVA content. q=search query, top_k=number of results (1-20)."""
    try:
        data = await _get(
            "rag/search", q=q, content_type=content_type,
            part=part, schedule=schedule, source=source, top_k=top_k,
        )
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: {_err(e)}"


@mcp.tool(
    description=(
        "Check the status of the RAG index. Returns total chunk count, "
        "breakdown by source (cfr, knowva) and content type (rating_criteria, "
        "adjudication, guidance), and embedding model info."
    )
)
async def bva_rag_status() -> str:
    """Get RAG index statistics - chunk counts by source and content type."""
    try:
        data = await _get("rag/status")
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: {_err(e)}"


# --- Health tool ---

@mcp.tool(
    description="Check that the BVA API is running and healthy. Returns status and version."
)
async def bva_health() -> str:
    """Check BVA API health status."""
    try:
        data = await _get("health")
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: {_err(e)}"


if __name__ == "__main__":
    if _transport == "http":
        asgi_app = mcp.streamable_http_app()
        cors_app = CORSMiddleware(
            asgi_app,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
        )
        uvicorn.run(cors_app, host=_host, port=_port)
    else:
        mcp.run()  # stdio transport (default)
