#!/usr/bin/env python3
"""ChromaDB RAG layer for BVA API - vector search over CFR and KnowVA content."""

import os
import time
import logging
from typing import Any, Dict, List, Optional

import httpx
import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings

from chunker import Chunk

logger = logging.getLogger(__name__)

CHROMA_PATH = os.environ.get("CHROMA_PATH", "./data/chroma")
COLLECTION_NAME = "bva_rag"
EMBEDDING_MODEL = "text-embedding-004"  # Vertex AI model
VERTEX_BATCH_SIZE = 50  # Vertex AI limit per call is 250, stay conservative


class VertexAIEmbeddingFunction(EmbeddingFunction[Documents]):
    """Custom ChromaDB embedding function using Vertex AI REST API.

    Uses Application Default Credentials (ADC) -- automatic on Cloud Run.
    Falls back gracefully with clear error messages.
    """

    def __init__(
        self,
        project_id: Optional[str] = None,
        location: str = "us-central1",
        model: str = EMBEDDING_MODEL,
    ):
        self._model = model
        self._location = location
        self._project_id = project_id
        self._credentials = None
        self._init_credentials()

    def _init_credentials(self):
        """Initialize Google ADC credentials."""
        try:
            import google.auth
            import google.auth.transport.requests

            self._credentials, detected_project = google.auth.default(
                scopes=["https://www.googleapis.com/auth/cloud-platform"]
            )
            if not self._project_id:
                self._project_id = detected_project
            logger.info(
                f"Vertex AI embeddings initialized: project={self._project_id}, "
                f"model={self._model}"
            )
        except Exception as e:
            logger.warning(f"Google ADC not available: {e}. Vertex AI embeddings will fail.")

    def _get_access_token(self) -> str:
        """Get a fresh access token, refreshing if needed."""
        import google.auth.transport.requests

        if self._credentials is None:
            raise RuntimeError("Google credentials not initialized")
        request = google.auth.transport.requests.Request()
        self._credentials.refresh(request)
        return self._credentials.token

    def _embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Embed a single batch via Vertex AI REST API with retry on 429."""
        token = self._get_access_token()
        url = (
            f"https://{self._location}-aiplatform.googleapis.com/v1/"
            f"projects/{self._project_id}/locations/{self._location}/"
            f"publishers/google/models/{self._model}:predict"
        )
        # Sanitize: replace empty strings, truncate to 10k chars (Vertex AI limit ~20k tokens)
        sanitized = [t[:10000] if t and t.strip() else "empty" for t in texts]
        instances = [{"content": t} for t in sanitized]
        payload = {"instances": instances}

        max_retries = 5
        for attempt in range(1, max_retries + 1):
            with httpx.Client(timeout=60.0) as client:
                resp = client.post(
                    url,
                    json=payload,
                    headers={"Authorization": f"Bearer {token}"},
                )
                if resp.status_code == 429:
                    wait = min(2 ** attempt, 30)
                    logger.warning(f"Vertex AI 429 rate limit, retry {attempt}/{max_retries} in {wait}s")
                    time.sleep(wait)
                    continue
                if resp.status_code == 400:
                    logger.error(f"Vertex AI 400 Bad Request: {resp.text[:500]}")
                resp.raise_for_status()

            predictions = resp.json().get("predictions", [])
            return [p["embeddings"]["values"] for p in predictions]

        raise RuntimeError(f"Vertex AI embedding failed after {max_retries} retries (429 rate limit)")

    def __call__(self, input: Documents) -> Embeddings:
        """Embed documents in batches with delay to avoid rate limits."""
        if not input:
            return []

        all_embeddings: List[List[float]] = []
        for i in range(0, len(input), VERTEX_BATCH_SIZE):
            if i > 0:
                time.sleep(0.5)  # pace requests to avoid 429s
            batch = input[i : i + VERTEX_BATCH_SIZE]
            embeddings = self._embed_batch(batch)
            all_embeddings.extend(embeddings)

        return all_embeddings


class OpenAIFallbackEmbeddingFunction(EmbeddingFunction[Documents]):
    """Fallback to OpenAI embeddings if configured via RAG_EMBEDDINGS=openai."""

    def __init__(self):
        from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

        api_key = os.environ.get("OPENAI_API_KEY", "")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY required when RAG_EMBEDDINGS=openai")
        self._fn = OpenAIEmbeddingFunction(
            api_key=api_key, model_name="text-embedding-3-small"
        )

    def __call__(self, input: Documents) -> Embeddings:
        return self._fn(input)


def _get_embedding_fn() -> EmbeddingFunction:
    """Get the configured embedding function.

    Default: Vertex AI (works on Cloud Run with ADC, no API key needed).
    Override: set RAG_EMBEDDINGS=openai to use OpenAI instead.
    """
    provider = os.environ.get("RAG_EMBEDDINGS", "vertex").lower()
    if provider == "openai":
        logger.info("Using OpenAI embeddings (RAG_EMBEDDINGS=openai)")
        return OpenAIFallbackEmbeddingFunction()
    logger.info("Using Vertex AI embeddings (default)")
    return VertexAIEmbeddingFunction()


_client: Optional[chromadb.ClientAPI] = None
_collection: Optional[chromadb.Collection] = None


def get_collection() -> chromadb.Collection:
    """Get or create the ChromaDB collection (singleton)."""
    global _client, _collection
    if _collection is not None:
        return _collection
    _client = chromadb.PersistentClient(path=CHROMA_PATH)
    _collection = _client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=_get_embedding_fn(),
        metadata={"hnsw:space": "cosine"},
    )
    logger.info(f"ChromaDB collection '{COLLECTION_NAME}' loaded: {_collection.count()} chunks")
    return _collection


def search(
    query: str,
    top_k: int = 5,
    content_type: Optional[str] = None,
    part: Optional[str] = None,
    schedule: Optional[str] = None,
    source: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Embed query and search ChromaDB with optional metadata filters."""
    collection = get_collection()

    where_clauses = []
    if content_type:
        where_clauses.append({"content_type": content_type})
    if part:
        where_clauses.append({"part": part})
    if schedule:
        where_clauses.append({"schedule": schedule})
    if source:
        where_clauses.append({"source": source})

    where = None
    if len(where_clauses) == 1:
        where = where_clauses[0]
    elif len(where_clauses) > 1:
        where = {"$and": where_clauses}

    kwargs: Dict[str, Any] = {
        "query_texts": [query],
        "n_results": min(top_k, collection.count() or 1),
        "include": ["documents", "metadatas", "distances"],
    }
    if where:
        kwargs["where"] = where

    try:
        results = collection.query(**kwargs)
    except Exception as e:
        logger.error(f"ChromaDB query error: {e}")
        return []

    hits = []
    if results and results["ids"] and results["ids"][0]:
        for i, doc_id in enumerate(results["ids"][0]):
            hits.append({
                "id": doc_id,
                "text": results["documents"][0][i] if results["documents"] else "",
                "metadata": results["metadatas"][0][i] if results["metadatas"] else {},
                "distance": results["distances"][0][i] if results["distances"] else None,
                "score": round(1.0 - (results["distances"][0][i] or 0), 4),
            })

    return hits


def add_chunks(chunks: List[Chunk]) -> int:
    """Upsert chunks into ChromaDB with retry logic. Returns count added."""
    if not chunks:
        return 0
    collection = get_collection()
    # Deduplicate by ID (keep last occurrence)
    seen = {}
    for c in chunks:
        seen[c.id] = c
    deduped = list(seen.values())
    if len(deduped) < len(chunks):
        logger.warning(f"Deduplicated {len(chunks) - len(deduped)} duplicate chunk IDs")
    ids = [c.id for c in deduped]
    documents = [c.text for c in deduped]
    metadatas = [c.metadata for c in deduped]
    batch_size = 50  # smaller batches for Vertex AI embedding calls
    total = 0
    max_retries = 3
    for i in range(0, len(ids), batch_size):
        batch_ids = ids[i:i + batch_size]
        batch_docs = documents[i:i + batch_size]
        batch_meta = metadatas[i:i + batch_size]
        for attempt in range(1, max_retries + 1):
            try:
                collection.upsert(ids=batch_ids, documents=batch_docs, metadatas=batch_meta)
                total += len(batch_ids)
                logger.info(f"Upserted batch {i // batch_size + 1}: {len(batch_ids)} chunks")
                break
            except Exception as e:
                if attempt == max_retries:
                    logger.error(f"Upsert failed after {max_retries} attempts: {e}")
                    raise
                wait = 2 ** attempt
                logger.warning(f"Upsert attempt {attempt} failed: {e}. Retrying in {wait}s...")
                time.sleep(wait)
    return total


def get_stats() -> Dict[str, Any]:
    """Return index statistics."""
    collection = get_collection()
    total = collection.count()

    embedding_provider = os.environ.get("RAG_EMBEDDINGS", "vertex").lower()
    stats: Dict[str, Any] = {
        "total_chunks": total,
        "collection": COLLECTION_NAME,
        "embedding_model": EMBEDDING_MODEL if embedding_provider != "openai" else "text-embedding-3-small",
        "embedding_provider": embedding_provider,
        "chroma_path": CHROMA_PATH,
        "by_source": {},
        "by_content_type": {},
    }

    if total > 0:
        try:
            all_data = collection.get(include=["metadatas"], limit=total)
            if all_data and all_data["metadatas"]:
                for meta in all_data["metadatas"]:
                    src = meta.get("source", "unknown")
                    ct = meta.get("content_type", "unknown")
                    stats["by_source"][src] = stats["by_source"].get(src, 0) + 1
                    stats["by_content_type"][ct] = stats["by_content_type"].get(ct, 0) + 1
        except Exception as e:
            logger.warning(f"Could not compute stats breakdown: {e}")

    return stats


def clear_collection() -> int:
    """Delete all chunks. Returns previous count."""
    global _collection
    collection = get_collection()
    count = collection.count()
    if count > 0:
        all_ids = collection.get(include=[])["ids"]
        if all_ids:
            collection.delete(ids=all_ids)
    logger.info(f"Cleared {count} chunks from collection")
    return count
