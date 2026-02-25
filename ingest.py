#!/usr/bin/env python3
"""CLI script to fetch content from BVA API, chunk it, and index into ChromaDB."""

import argparse
import logging
import sys
import time

import requests

import rag
from chunker import Chunk, chunk_cfr_part3, chunk_cfr_part4, chunk_knowva

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

REQUEST_TIMEOUT = 30

# DC_LOOKUP imported from app.py at runtime would create circular deps,
# so we duplicate the section->schedule mapping here for Part 4 chunking
DC_LOOKUP = {
    "9411": {"condition": "PTSD", "section": "130", "part": "4", "schedule": "Mental Disorders"},
    "9434": {"condition": "Major Depressive Disorder", "section": "130", "part": "4", "schedule": "Mental Disorders"},
    "9400": {"condition": "Generalized Anxiety Disorder", "section": "130", "part": "4", "schedule": "Mental Disorders"},
    "9201": {"condition": "Schizophrenia", "section": "130", "part": "4", "schedule": "Mental Disorders"},
    "9432": {"condition": "Bipolar Disorder", "section": "130", "part": "4", "schedule": "Mental Disorders"},
    "9413": {"condition": "Unspecified Anxiety Disorder", "section": "130", "part": "4", "schedule": "Mental Disorders"},
    "9440": {"condition": "Chronic Adjustment Disorder", "section": "130", "part": "4", "schedule": "Mental Disorders"},
    "6602": {"condition": "Asthma (Bronchial)", "section": "97", "part": "4", "schedule": "Respiratory System"},
    "6604": {"condition": "COPD", "section": "97", "part": "4", "schedule": "Respiratory System"},
    "6847": {"condition": "Sleep Apnea (Obstructive)", "section": "97", "part": "4", "schedule": "Respiratory System"},
    "6600": {"condition": "Bronchitis (Chronic)", "section": "97", "part": "4", "schedule": "Respiratory System"},
    "6845": {"condition": "Restrictive Lung Disease", "section": "97", "part": "4", "schedule": "Respiratory System"},
    "5201": {"condition": "Arm (Limitation of Motion)", "section": "71a", "part": "4", "schedule": "Musculoskeletal System"},
    "5003": {"condition": "Arthritis (Degenerative)", "section": "71a", "part": "4", "schedule": "Musculoskeletal System"},
    "5010": {"condition": "Arthritis (Traumatic)", "section": "71a", "part": "4", "schedule": "Musculoskeletal System"},
    "5237": {"condition": "Lumbosacral Strain", "section": "71a", "part": "4", "schedule": "Musculoskeletal System"},
    "5242": {"condition": "Degenerative Arthritis of the Spine", "section": "71a", "part": "4", "schedule": "Musculoskeletal System"},
    "5243": {"condition": "Intervertebral Disc Syndrome (IVDS)", "section": "71a", "part": "4", "schedule": "Musculoskeletal System"},
    "5260": {"condition": "Leg (Limitation of Flexion)", "section": "71a", "part": "4", "schedule": "Musculoskeletal System"},
    "5261": {"condition": "Leg (Limitation of Extension)", "section": "71a", "part": "4", "schedule": "Musculoskeletal System"},
    "5271": {"condition": "Ankle (Limited Motion)", "section": "71a", "part": "4", "schedule": "Musculoskeletal System"},
    "8045": {"condition": "Traumatic Brain Injury (TBI)", "section": "124a", "part": "4", "schedule": "Neurological Conditions"},
    "8100": {"condition": "Migraine Headaches", "section": "124a", "part": "4", "schedule": "Neurological Conditions"},
    "8520": {"condition": "Sciatic Nerve (Paralysis)", "section": "124a", "part": "4", "schedule": "Neurological Conditions"},
    "8515": {"condition": "Median Nerve (Paralysis)", "section": "124a", "part": "4", "schedule": "Neurological Conditions"},
    "8516": {"condition": "Ulnar Nerve (Paralysis)", "section": "124a", "part": "4", "schedule": "Neurological Conditions"},
    "8510": {"condition": "Upper Radicular Group (Paralysis)", "section": "124a", "part": "4", "schedule": "Neurological Conditions"},
    "6100": {"condition": "Hearing Loss (Bilateral)", "section": "85", "part": "4", "schedule": "Ear"},
    "6260": {"condition": "Tinnitus", "section": "87", "part": "4", "schedule": "Ear"},
    "7005": {"condition": "Coronary Artery Disease", "section": "104", "part": "4", "schedule": "Cardiovascular System"},
    "7101": {"condition": "Hypertension", "section": "104", "part": "4", "schedule": "Cardiovascular System"},
    "7110": {"condition": "Aortic Aneurysm", "section": "104", "part": "4", "schedule": "Cardiovascular System"},
    "7806": {"condition": "Dermatitis/Eczema", "section": "118", "part": "4", "schedule": "Skin"},
    "7800": {"condition": "Burn Scars (Head/Face/Neck)", "section": "118", "part": "4", "schedule": "Skin"},
    "7801": {"condition": "Burn Scars (Other)", "section": "118", "part": "4", "schedule": "Skin"},
    "7804": {"condition": "Unstable/Painful Scars", "section": "118", "part": "4", "schedule": "Skin"},
    "7346": {"condition": "GERD (Hiatal Hernia)", "section": "114", "part": "4", "schedule": "Digestive System"},
    "7319": {"condition": "Irritable Bowel Syndrome (IBS)", "section": "114", "part": "4", "schedule": "Digestive System"},
    "7323": {"condition": "Ulcerative Colitis", "section": "114", "part": "4", "schedule": "Digestive System"},
    "7913": {"condition": "Diabetes Mellitus (Type II)", "section": "119", "part": "4", "schedule": "Endocrine System"},
    "7900": {"condition": "Hyperthyroidism", "section": "119", "part": "4", "schedule": "Endocrine System"},
    "7528": {"condition": "Malignant Neoplasms (Genitourinary)", "section": "115a", "part": "4", "schedule": "Genitourinary System"},
    "7522": {"condition": "Erectile Dysfunction", "section": "115a", "part": "4", "schedule": "Genitourinary System"},
    "6066": {"condition": "Visual Acuity Loss", "section": "79", "part": "4", "schedule": "Eye"},
    "9905": {"condition": "TMJ (Temporomandibular)", "section": "150", "part": "4", "schedule": "Dental and Oral Conditions"},
    "7629": {"condition": "Endometriosis", "section": "116", "part": "4", "schedule": "Gynecological Conditions"},
    "6354": {"condition": "Chronic Fatigue Syndrome", "section": "88b", "part": "4", "schedule": "Infectious Diseases"},
    "7702": {"condition": "Agranulocytosis", "section": "117", "part": "4", "schedule": "Hemic and Lymphatic Systems"},
    "8863": {"condition": "Gulf War Undiagnosed Illness", "section": "317", "part": "3", "schedule": "Undiagnosed Illness (38 CFR 3.317)"},
}

# Part 3 key sections to index
PART3_SECTIONS = [
    "102", "103", "156", "159", "303", "304", "307", "309",
    "310", "312", "317", "321", "340", "341", "400",
]

# KnowVA search terms to seed article discovery
KNOWVA_SEARCH_TERMS = [
    "PTSD", "TDIU", "service connection", "rating", "effective date",
    "disability compensation", "presumptive", "secondary condition",
    "individual unemployability", "mental health rating",
    "hearing loss", "sleep apnea", "back pain", "knee",
    "appeal", "supplemental claim", "higher level review",
]


def _api_get(api_url: str, path: str, params: dict = None) -> dict:
    """Make GET request to BVA API."""
    url = f"{api_url}/{path}"
    resp = requests.get(url, params=params or {}, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    return resp.json()


def ingest_cfr_part4(api_url: str) -> list[Chunk]:
    """Fetch and chunk Part 4 rating criteria sections."""
    # Get unique sections from DC_LOOKUP
    sections = set()
    for info in DC_LOOKUP.values():
        if info["part"] == "4":
            sections.add(info["section"])

    all_chunks = []
    for section in sorted(sections):
        logger.info(f"Fetching CFR Part 4 section {section}...")
        try:
            data = _api_get(api_url, "cfr/section", {"part": "4", "section": section})
            markdown = data.get("content_markdown", "")
            chunks = chunk_cfr_part4(markdown, "4", section, DC_LOOKUP)
            all_chunks.extend(chunks)
            logger.info(f"  -> {len(chunks)} chunks from 4.{section}")
            time.sleep(0.5)  # Rate limit eCFR
        except Exception as e:
            logger.error(f"  -> Failed to fetch 4.{section}: {e}")

    return all_chunks


def ingest_cfr_part3(api_url: str) -> list[Chunk]:
    """Fetch and chunk Part 3 adjudication sections."""
    all_chunks = []
    for section in PART3_SECTIONS:
        logger.info(f"Fetching CFR Part 3 section {section}...")
        try:
            data = _api_get(api_url, "cfr/section", {"part": "3", "section": section})
            markdown = data.get("content_markdown", "")
            chunks = chunk_cfr_part3(markdown, "3", section)
            all_chunks.extend(chunks)
            logger.info(f"  -> {len(chunks)} chunks from 3.{section}")
            time.sleep(0.5)
        except Exception as e:
            logger.error(f"  -> Failed to fetch 3.{section}: {e}")

    return all_chunks


def ingest_knowva(api_url: str) -> list[Chunk]:
    """Fetch and chunk KnowVA articles from popular + search results."""
    seen_ids = set()
    articles_to_fetch = []

    # Get popular articles
    logger.info("Fetching popular KnowVA articles...")
    try:
        popular = _api_get(api_url, "knowva/popular", {"pagesize": 20})
        for item in popular:
            if item["id"] not in seen_ids:
                seen_ids.add(item["id"])
                articles_to_fetch.append((item["id"], item.get("name", "")))
    except Exception as e:
        logger.error(f"Failed to fetch popular articles: {e}")

    # Search for key terms
    for term in KNOWVA_SEARCH_TERMS:
        logger.info(f"Searching KnowVA for '{term}'...")
        try:
            data = _api_get(api_url, "knowva/search", {"q": term, "pagesize": 10})
            for item in data.get("results", []):
                if item["id"] not in seen_ids:
                    seen_ids.add(item["id"])
                    articles_to_fetch.append((item["id"], item.get("name", "")))
            time.sleep(0.3)
        except Exception as e:
            logger.error(f"  -> KnowVA search failed for '{term}': {e}")

    logger.info(f"Found {len(articles_to_fetch)} unique KnowVA articles to index")

    # Fetch full content and chunk
    all_chunks = []
    for article_id, article_name in articles_to_fetch:
        logger.info(f"Fetching KnowVA article {article_id}: {article_name[:60]}...")
        try:
            data = _api_get(api_url, f"knowva/article/{article_id}")
            content = data.get("content", "")
            name = data.get("name", article_name)
            if not content:
                logger.warning(f"  -> Empty content for article {article_id}")
                continue
            chunks = chunk_knowva(content, article_id, name)
            all_chunks.extend(chunks)
            logger.info(f"  -> {len(chunks)} chunks")
            time.sleep(0.3)
        except Exception as e:
            logger.error(f"  -> Failed to fetch article {article_id}: {e}")

    return all_chunks


def main():
    parser = argparse.ArgumentParser(description="Ingest content into BVA RAG index")
    parser.add_argument(
        "--source",
        choices=["cfr", "knowva", "all"],
        default="all",
        help="Which content to index (default: all)",
    )
    parser.add_argument(
        "--api-url",
        default="http://localhost:8001",
        help="BVA API base URL (default: http://localhost:8001)",
    )
    parser.add_argument(
        "--clear",
        action="store_true",
        help="Clear existing index before ingesting",
    )
    args = parser.parse_args()

    logger.info(f"Starting ingest: source={args.source}, api={args.api_url}")

    # Verify API is reachable
    try:
        health = _api_get(args.api_url, "health")
        logger.info(f"API health: {health.get('status', 'unknown')}")
    except Exception as e:
        logger.error(f"Cannot reach API at {args.api_url}: {e}")
        sys.exit(1)

    if args.clear:
        cleared = rag.clear_collection()
        logger.info(f"Cleared {cleared} existing chunks")

    all_chunks: list[Chunk] = []

    if args.source in ("cfr", "all"):
        logger.info("=== Ingesting CFR Part 4 (Rating Criteria) ===")
        all_chunks.extend(ingest_cfr_part4(args.api_url))

        logger.info("=== Ingesting CFR Part 3 (Adjudication) ===")
        all_chunks.extend(ingest_cfr_part3(args.api_url))

    if args.source in ("knowva", "all"):
        logger.info("=== Ingesting KnowVA Articles ===")
        all_chunks.extend(ingest_knowva(args.api_url))

    if all_chunks:
        logger.info(f"=== Indexing {len(all_chunks)} total chunks ===")
        indexed = rag.add_chunks(all_chunks)
        logger.info(f"Indexed {indexed} chunks successfully")
    else:
        logger.warning("No chunks to index")

    stats = rag.get_stats()
    logger.info(f"Final index stats: {stats}")


if __name__ == "__main__":
    main()
