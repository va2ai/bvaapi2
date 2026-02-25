#!/usr/bin/env python3
"""ChromaDB RAG layer for BVA API - vector search over CFR and KnowVA content."""

import os
import logging
from typing import Any, Dict, List, Optional

import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

from chunker import Chunk

logger = logging.getLogger(__name__)

CHROMA_PATH = os.environ.get("CHROMA_PATH", "./data/chroma")
COLLECTION_NAME = "bva_rag"
EMBEDDING_MODEL = "text-embedding-3-small"

_client: Optional[chromadb.ClientAPI] = None
_collection: Optional[chromadb.Collection] = None


def _get_embedding_fn() -> OpenAIEmbeddingFunction:
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY environment variable is required for RAG")
    return OpenAIEmbeddingFunction(
        api_key=api_key,
        model_name=EMBEDDING_MODEL,
    )


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
    """Upsert chunks into ChromaDB. Returns count added."""
    if not chunks:
        return 0
    collection = get_collection()
    ids = [c.id for c in chunks]
    documents = [c.text for c in chunks]
    metadatas = [c.metadata for c in chunks]
    # Batch in groups of 100 to avoid API limits
    batch_size = 100
    total = 0
    for i in range(0, len(ids), batch_size):
        batch_ids = ids[i:i + batch_size]
        batch_docs = documents[i:i + batch_size]
        batch_meta = metadatas[i:i + batch_size]
        collection.upsert(ids=batch_ids, documents=batch_docs, metadatas=batch_meta)
        total += len(batch_ids)
        logger.info(f"Upserted batch {i // batch_size + 1}: {len(batch_ids)} chunks")
    return total


def get_stats() -> Dict[str, Any]:
    """Return index statistics."""
    collection = get_collection()
    total = collection.count()

    # Sample metadata to get source/type breakdown
    stats: Dict[str, Any] = {
        "total_chunks": total,
        "collection": COLLECTION_NAME,
        "embedding_model": EMBEDDING_MODEL,
        "chroma_path": CHROMA_PATH,
        "by_source": {},
        "by_content_type": {},
    }

    if total > 0:
        # Get all metadata to compute breakdowns
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
        # Get all IDs and delete
        all_ids = collection.get(include=[])["ids"]
        if all_ids:
            collection.delete(ids=all_ids)
    logger.info(f"Cleared {count} chunks from collection")
    return count
