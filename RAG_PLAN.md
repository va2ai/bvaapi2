# BVA API RAG Implementation Plan

## Current State

- **RAG code exists** (`rag.py`, `chunker.py`, `ingest.py`) but is **non-functional**
- **Root cause**: OpenAI API connection timeouts on GCP Cloud Run + ChromaDB PersistentClient uses local disk (ephemeral on Cloud Run)
- **Endpoints exist**: `/rag/search`, `/rag/status`, `/rag/reindex`, `/rag/debug`
- **MCP tools exist**: `bva_rag_search`, `bva_rag_status`
- **VA Research App** already live at `vet-research-*.run.app/bva-explorer.html` with RAG search UI wired up but returning errors

## Architecture Decisions

### Vector DB: Chroma Cloud (Primary) or In-Memory + GCS (Fallback)

**Chroma Cloud** (~$0.35/mo):
- Zero ops, official hosted ChromaDB
- No FUSE hacks, no separate Cloud Run service
- Same API as current code (`chromadb.HttpClient`)
- Persistent across deployments

**Fallback -- In-Memory + GCS Lazy Load** (~$0.50/mo):
- Download ChromaDB snapshot from GCS on cold start (2-5s)
- All queries in-memory (<5ms)
- Zero external dependencies
- Update via reindex endpoint -> upload snapshot to GCS

**Rejected options**: GCS FUSE (fragile), Vertex AI Vector Search ($50+/mo overkill), Pinecone ($50/mo minimum)

### Embeddings: Vertex AI text-embedding-004 (Primary)

**Why Vertex AI over OpenAI**:
- **Eliminates the connection error** -- native GCP, no external API key needed
- Authenticates via Cloud Run's default service account (IAM, no secret mounting)
- Same data center = faster, more reliable
- Supports `RETRIEVAL_DOCUMENT` task type for legal content
- ~$1-2/mo for 2000 chunks

**Migration path**:
```python
# OLD (broken):
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
ef = OpenAIEmbeddingFunction(api_key=os.environ["OPENAI_API_KEY"])

# NEW (no secret needed):
from chromadb.utils.embedding_functions import GoogleVertexEmbeddingFunction
ef = GoogleVertexEmbeddingFunction(
    project_id="vaclaims-194006",
    region="us-central1",
    model_name="text-embedding-004"
)
```

**Fallback**: Keep OpenAI text-embedding-3-small with batch size reduced to 50 + retry logic

### Content to Index (Phase 1)

| Source | Chunks | Strategy |
|--------|--------|----------|
| 38 CFR Part 4 (rating criteria) | ~200 | Split by DC code boundary (existing) |
| 38 CFR Part 3 (adjudication) | ~150 | Split by subsection (a), (b) etc. (existing) |
| KnowVA articles | ~500 | Split by heading (existing) |
| **Total Phase 1** | **~850** | Fits easily in free/cheap tiers |

---

## Implementation Phases

### Phase 1: Fix RAG (Get It Working) -- Priority HIGH

**Goal**: Make `/rag/search` return real results in the BVA Explorer app

1. **Switch embedding function** (`rag.py`)
   - Replace `OpenAIEmbeddingFunction` with `GoogleVertexEmbeddingFunction`
   - Remove `OPENAI_API_KEY` dependency from RAG (keep for other uses)
   - Add `google-cloud-aiplatform` to `requirements.txt`

2. **Switch to Chroma Cloud** (`rag.py`)
   - Replace `PersistentClient(path=CHROMA_PATH)` with `HttpClient(host=CHROMA_CLOUD_HOST, ...)`
   - Store Chroma Cloud API key in GCP Secret Manager
   - OR use in-memory + GCS approach if Chroma Cloud isn't viable

3. **Fix batch upsert** (`rag.py`)
   - Reduce batch size from 100 to 50
   - Add retry logic with exponential backoff
   - Add timeout handling per batch

4. **Test reindex flow** (`ingest.py` via `/rag/reindex`)
   - Hit `/rag/reindex?source=all` on deployed service
   - Verify `/rag/status` shows correct chunk counts
   - Verify `/rag/search?q=ptsd+rating+criteria` returns relevant results

5. **Update BVA Explorer** to show RAG results properly
   - RAG search UI already exists in `bva-explorer.html`
   - Just needs working backend

**Files to modify**: `rag.py`, `requirements.txt`, `cloudbuild.yaml` (secrets)

### Phase 2: Enrich RAG Results -- Priority MEDIUM

**Goal**: Make RAG results useful for the research app

6. **Enrich response format** (`app.py` `/rag/search`)
   - Add `source_url` to each result (already in chunk metadata)
   - Add `related_dc_codes` -- cross-reference chunk metadata with DC_LOOKUP
   - Add `cfr_cross_refs` -- extract CFR citations from chunk text
   - Add `relevance_score` (normalized 0-1, already computed)

7. **Add suggested followups** to RAG response
   ```json
   {
     "suggested_followups": [
       {"tool": "bva_cfr_dc_lookup", "args": {"code": "9411"}, "reason": "PTSD diagnostic code"},
       {"tool": "bva_search", "args": {"q": "ptsd 70 percent"}, "reason": "Find supporting cases"}
     ]
   }
   ```

8. **Enhance `bva_rag_search` MCP tool** (`mcp_server.py`)
   - Add `enrich: bool = True` param
   - Add `followups: bool = True` param
   - Return structured research context for AI agents

**Files to modify**: `app.py`, `mcp_server.py`

### Phase 3: Research Orchestration Endpoint -- Priority MEDIUM

**Goal**: Single endpoint that combines RAG + case search + CFR for comprehensive research

9. **New `POST /research` endpoint** (`app.py`)
   ```
   POST /research
   {
     "query": "secondary service connection sleep apnea PTSD",
     "condition": "sleep apnea",
     "dc_code": "6847",
     "include": ["rag", "cfr", "bva_cases", "federal_register"],
     "top_k": 5
   }
   ```
   Returns bundled results from:
   - RAG semantic search (CFR + KnowVA)
   - DC code lookup (from condition or dc_code)
   - Top BVA cases (keyword search)
   - Recent Federal Register changes
   - Suggested next queries

10. **New `bva_research` MCP meta-tool** (`mcp_server.py`)
    - Wraps `/research` endpoint
    - Best for: "find everything about X condition"
    - Structured output for AI agent consumption

11. **Hybrid search merge** -- Reciprocal Rank Fusion
    ```python
    def rrf_score(rank, k=60):
        return 1.0 / (k + rank)
    ```
    Combine semantic (RAG) + keyword (BVA search) results with RRF scoring

**Files to modify**: `app.py`, `mcp_server.py`

### Phase 4: Content Expansion -- Priority LOW

12. **Index CAVC precedential opinions** (~200/year)
    - Add `chunk_cavc()` to `chunker.py`
    - Split at paragraph level, tag with holding/reasoning/disposition

13. **Index M21-1 Manual sections** (if accessible)
    - Chapter-level chunking, ~1500 chars each
    - Tag with claim_type metadata

14. **BVA decision summaries** (sample, not full corpus)
    - Index outcome summaries only (condition, DC code, outcome, key excerpt)
    - NOT full text of all cases (millions -- won't scale in vector DB)
    - Keep full-text BVA search as keyword-only (existing `/search`)

### Phase 5: Production Polish -- Priority LOW

15. **SSE streaming for `/research`** endpoint
    - Use `sse-starlette` EventSourceResponse
    - Stream step-by-step: "searching RAG..." -> "searching cases..." -> results

16. **Caching** with `cachetools.TTLCache`
    - CFR sections: 24h cache
    - KnowVA articles: 1h cache
    - RAG results: 30min per (query, filters) key

17. **Standardize pagination** across all list endpoints

---

## VA Research App Integration

The BVA Explorer at `vet-research-*.run.app/bva-explorer.html` already has:
- RAG search UI with parameters (query, content_type, part, schedule, source, top_k)
- Result rendering for RAG responses
- Both REST and MCP execution modes
- Citation linking (CFR and CAVC auto-detection)
- Mobile-responsive layout

**What it needs from this plan**:
- Phase 1: Working RAG backend (currently errors)
- Phase 2: Enriched results with source_url, related DC codes, followup suggestions
- Phase 3: New `/research` tab in the explorer for orchestrated queries
- Phase 5: Streaming progress indicators for long research queries

**Use case flows the app should support**:

| Persona | Flow | Endpoints Used |
|---------|------|---------------|
| Veteran | "What rating for PTSD?" | `/rag/search` -> `/cfr/dc/{code}` |
| Attorney | "Sleep apnea secondary to PTSD cases" | `/research` (orchestrated) |
| VSO | "Evidence needed for TDIU claim" | `/rag/search` + `/knowva/search` |
| Researcher | "Grant rates for mental health 2023" | `/search` (BVA) + aggregate |
| AI Agent | Multi-step legal research | `bva_research` MCP tool |

---

## Cost Summary

| Component | Monthly Cost |
|-----------|-------------|
| Chroma Cloud (or GCS snapshot) | $0.35-0.50 |
| Vertex AI embeddings | $1-2 |
| Cloud Run (existing) | $0.40 |
| **Total RAG addition** | **~$2-3/mo** |

## Files to Create/Modify

| File | Changes |
|------|---------|
| `rag.py` | Switch to Vertex AI embeddings + Chroma Cloud client |
| `requirements.txt` | Add `google-cloud-aiplatform`, remove OpenAI dependency from RAG |
| `app.py` | Enrich RAG response, add `/research` endpoint |
| `mcp_server.py` | Enhance `bva_rag_search`, add `bva_research` tool |
| `chunker.py` | Add `chunk_cavc()` (Phase 4) |
| `ingest.py` | Add CAVC ingestion (Phase 4) |
| `cloudbuild.yaml` | Add Chroma Cloud API key secret (if using Chroma Cloud) |
