"""Veteran Reddit market analysis pipeline.

Implements the workflow from the market-analysis plan:
- Phase 1: Collect Reddit posts/comments into structured JSON.
- Phase 2: Build batch inputs + prompts for need extraction.
- Phase 3-5: Generate prompt packs for clustering, ideation, validation.
- Final: Compile a markdown report from AI output JSON files.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

URL_RE = re.compile(r"https?://[^\s)\]\[\"'>]+")

TARGET_SUBREDDITS: Dict[str, Dict[str, str]] = {
    "VeteransBenefits": {
        "focus": "VA disability claims, ratings, appeals, C&P exams",
        "priority": "Critical",
    },
    "Veterans": {
        "focus": "General veteran life, transition, healthcare, employment",
        "priority": "Critical",
    },
    "VeteranWomen": {
        "focus": "Women-specific VA issues, MST claims, gender-specific care",
        "priority": "High",
    },
    "MilitaryFinance": {
        "focus": "GI Bill, TSP, VA loans, financial planning",
        "priority": "High",
    },
    "Militaryfaq": {
        "focus": "Pre-transition questions, general military info",
        "priority": "Medium",
    },
    "VetTech": {
        "focus": "Vet tech training, career transition into tech",
        "priority": "Medium",
    },
    "PTSD": {
        "focus": "PTSD management, treatment, VA mental health services",
        "priority": "Medium",
    },
    "disability": {
        "focus": "General disability community (veterans subset)",
        "priority": "Low",
    },
}

PHASE1_PROMPT = """You are a market research analyst specializing in the U.S. veteran community.
I’m going to give you a batch of Reddit posts and comments from veteran subreddits.
For each post, identify:
1. PRIMARY NEED: What is the veteran trying to accomplish or solve?
2. PAIN POINTS: What specific frustrations or blockers do they describe?
3. CURRENT SOLUTION: What are they currently doing to solve this? (DIY, paid service, nothing?)
4. EMOTIONAL INTENSITY: Rate 1–5 (1=mild inconvenience, 5=desperate/life-impacting)
5. CATEGORY: Assign one: Claims/Ratings, Appeals, Healthcare, Mental Health,
   Employment/Transition, Education/GI Bill, Housing/VA Loan, Financial, Legal,
   Community/Social, Other.

Output strictly as a JSON array, one object per post.
"""

PHASE2_PROMPT = """You are a market strategist analyzing the U.S. veteran services market.
You are given extracted needs from veteran Reddit communities.

Do the following:
1. Group similar needs into 10–20 distinct opportunity clusters.
2. For each cluster provide:
   - cluster_name
   - post_count
   - average_emotional_intensity (1-5)
   - top_3_pain_points with example quotes
   - current_solutions
   - gap_analysis
3. Rank clusters by monetization_score (1-100), weighted by:
   - frequency 30%
   - intensity 25%
   - willingness_to_pay 25%
   - ai_solvability 20%

Output JSON sorted by monetization_score descending.
"""

PHASE3_PROMPT = """You are an AI product strategist specializing in veteran services.
For each provided opportunity cluster, propose 1-2 AI-powered product concepts.
For each concept include:
1. product_name
2. one_liner
3. ai_capabilities
4. target_user
5. business_model
6. revenue_estimate
7. competitive_landscape
8. build_complexity (Low/Medium/High)
9. quick_win_mvp_2_to_4_weeks

Output JSON.
"""

PHASE4_PROMPT = """Context:
I’m an AI software engineer and former VA disability consultant with 15+ years of experience.
I run Veteran 2 Veteran LLC and build AI tools for VA-accredited legal professionals.
I have an existing BVA research platform (MCP/REST API) and a React Native app in development (Vet Dynamic).

Given product concepts, evaluate each:
1. alignment_with_stack_and_positioning
2. regulatory_or_accreditation_risks (38 CFR, OGC, unauthorized practice risk)
3. realistic_path_to_first_revenue
4. mvp_in_2_weeks_using_claude_bva_mcp_react_native
5. final_verdict: Build Now / Build Next / Shelf It + one-sentence rationale

Output JSON.
"""


@dataclass
class CollectConfig:
    months: int = 12
    fallback_months: int = 24
    min_score: int = 5
    min_comments: int = 10
    top_all_limit: int = 400
    top_year_limit: int = 400
    new_limit: int = 400
    top_comment_limit: int = 20
    anonymize_authors: bool = True


def utc_now() -> dt.datetime:
    return dt.datetime.now(tz=dt.timezone.utc)


def iso_from_utc(ts: float) -> str:
    return dt.datetime.fromtimestamp(ts, tz=dt.timezone.utc).isoformat()


def sha_author(value: Optional[str]) -> Optional[str]:
    if not value:
        return None
    digest = hashlib.sha256(value.encode("utf-8")).hexdigest()
    return digest[:16]


def extract_urls(text: str) -> List[str]:
    if not text:
        return []
    return sorted(set(URL_RE.findall(text)))


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def get_reddit_client() -> Any:
    try:
        import praw
    except ImportError as exc:
        raise RuntimeError(
            "praw is required for collection. Install dependencies with `pip install -r requirements.txt`."
        ) from exc

    missing = [
        name
        for name in ["REDDIT_CLIENT_ID", "REDDIT_CLIENT_SECRET", "REDDIT_USER_AGENT"]
        if not os.getenv(name)
    ]
    if missing:
        raise RuntimeError(
            "Missing Reddit API env vars: " + ", ".join(missing) + ". "
            "Set them before running `collect`."
        )

    return praw.Reddit(
        client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_CLIENT_SECRET"],
        user_agent=os.environ["REDDIT_USER_AGENT"],
        check_for_async=False,
    )


def submission_in_window(submission: Any, earliest: dt.datetime) -> bool:
    created = dt.datetime.fromtimestamp(float(submission.created_utc), tz=dt.timezone.utc)
    return created >= earliest


def iter_candidates(subreddit: Any, cfg: CollectConfig) -> Iterable[Any]:
    seen: set[str] = set()
    iterables = [
        subreddit.top(time_filter="all", limit=cfg.top_all_limit),
        subreddit.top(time_filter="year", limit=cfg.top_year_limit),
        subreddit.new(limit=cfg.new_limit),
    ]
    for stream in iterables:
        for submission in stream:
            sid = str(submission.id)
            if sid in seen:
                continue
            seen.add(sid)
            yield submission


def serialize_submission(
    submission: Any,
    subreddit_name: str,
    comment_limit: int,
    anonymize_authors: bool,
) -> Dict[str, Any]:
    submission.comment_sort = "top"
    submission.comments.replace_more(limit=0)
    all_comments = list(submission.comments.list())
    all_comments.sort(key=lambda c: int(getattr(c, "score", 0)), reverse=True)
    selected_comments = all_comments[:comment_limit]

    comment_rows: List[Dict[str, Any]] = []
    url_bucket: List[str] = []
    for comment in selected_comments:
        body = str(getattr(comment, "body", "") or "")
        url_bucket.extend(extract_urls(body))
        author_name = None
        if getattr(comment, "author", None) is not None:
            author_name = str(comment.author)
        comment_rows.append(
            {
                "id": str(comment.id),
                "score": int(getattr(comment, "score", 0) or 0),
                "body": body,
                "created_at": iso_from_utc(float(getattr(comment, "created_utc", 0))),
                "author_hash": sha_author(author_name) if anonymize_authors else author_name,
                "author_flair": getattr(comment, "author_flair_text", None),
                "permalink": f"https://reddit.com{getattr(comment, 'permalink', '')}",
            }
        )

    selftext = str(getattr(submission, "selftext", "") or "")
    title = str(getattr(submission, "title", "") or "")
    post_urls = extract_urls(selftext)

    author_name = None
    if getattr(submission, "author", None) is not None:
        author_name = str(submission.author)

    return {
        "id": str(submission.id),
        "subreddit": subreddit_name,
        "title": title,
        "body": selftext,
        "flair": getattr(submission, "link_flair_text", None),
        "score": int(getattr(submission, "score", 0) or 0),
        "comment_count": int(getattr(submission, "num_comments", 0) or 0),
        "created_at": iso_from_utc(float(getattr(submission, "created_utc", 0))),
        "author_hash": sha_author(author_name) if anonymize_authors else author_name,
        "author_flair": getattr(submission, "author_flair_text", None),
        "permalink": f"https://reddit.com{getattr(submission, 'permalink', '')}",
        "urls": sorted(set(post_urls + url_bucket)),
        "top_comments": comment_rows,
    }


def serialize_with_retry(
    submission: Any,
    subreddit_name: str,
    comment_limit: int,
    anonymize_authors: bool,
    retries: int = 5,
    initial_backoff_seconds: float = 2.0,
) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    """Serialize a submission with backoff on Reddit rate limits."""
    try:
        from prawcore.exceptions import TooManyRequests
    except Exception:
        TooManyRequests = None  # type: ignore[assignment]

    backoff = initial_backoff_seconds
    for attempt in range(retries):
        try:
            return (
                serialize_submission(
                    submission=submission,
                    subreddit_name=subreddit_name,
                    comment_limit=comment_limit,
                    anonymize_authors=anonymize_authors,
                ),
                None,
            )
        except Exception as exc:
            if TooManyRequests and isinstance(exc, TooManyRequests):
                if attempt == retries - 1:
                    return None, f"rate_limited:{submission.id}"
                time.sleep(backoff)
                backoff = min(backoff * 2.0, 60.0)
                continue
            return None, f"error:{submission.id}:{type(exc).__name__}"
    return None, f"failed:{submission.id}"


def collect_subreddit(
    reddit: Any,
    subreddit_name: str,
    cfg: CollectConfig,
) -> Dict[str, Any]:
    subreddit = reddit.subreddit(subreddit_name)
    now = utc_now()
    earliest_12 = now - dt.timedelta(days=cfg.months * 30)
    earliest_fallback = now - dt.timedelta(days=cfg.fallback_months * 30)

    rows_12: List[Dict[str, Any]] = []
    rows_fallback: List[Dict[str, Any]] = []
    skipped_posts: List[str] = []

    for submission in iter_candidates(subreddit, cfg):
        score = int(getattr(submission, "score", 0) or 0)
        comments = int(getattr(submission, "num_comments", 0) or 0)
        if not (score >= cfg.min_score or comments >= cfg.min_comments):
            continue

        in_12 = submission_in_window(submission, earliest_12)
        in_fallback = submission_in_window(submission, earliest_fallback)
        if not in_fallback:
            continue

        row, err = serialize_with_retry(
            submission=submission,
            subreddit_name=subreddit_name,
            comment_limit=cfg.top_comment_limit,
            anonymize_authors=cfg.anonymize_authors,
        )
        if row is None:
            if err:
                skipped_posts.append(err)
            continue
        if in_12:
            rows_12.append(row)
        else:
            rows_fallback.append(row)

    selected = rows_12 if len(rows_12) >= 1 else rows_12 + rows_fallback
    used_window_months = cfg.months if rows_12 else cfg.fallback_months

    return {
        "subreddit": subreddit_name,
        "focus": TARGET_SUBREDDITS.get(subreddit_name, {}).get("focus"),
        "priority": TARGET_SUBREDDITS.get(subreddit_name, {}).get("priority"),
        "collected_at": utc_now().isoformat(),
        "window_months": used_window_months,
        "filters": {
            "min_score": cfg.min_score,
            "min_comments": cfg.min_comments,
            "top_comment_limit": cfg.top_comment_limit,
        },
        "post_count": len(selected),
        "skipped_posts": skipped_posts[:250],
        "posts": selected,
    }


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=True), encoding="utf-8")


def write_csv(path: Path, rows: List[Dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def command_collect(args: argparse.Namespace) -> int:
    cfg = CollectConfig(
        months=args.months,
        fallback_months=args.fallback_months,
        min_score=args.min_score,
        min_comments=args.min_comments,
        top_all_limit=args.top_all_limit,
        top_year_limit=args.top_year_limit,
        new_limit=args.new_limit,
        top_comment_limit=args.top_comment_limit,
        anonymize_authors=not args.keep_authors,
    )

    reddit = get_reddit_client()
    output_dir = Path(args.output_dir)
    ensure_dir(output_dir)

    subreddits = args.subreddits or list(TARGET_SUBREDDITS.keys())
    summary_rows: List[Dict[str, Any]] = []

    for name in subreddits:
        print(f"[collect] r/{name} ...", file=sys.stderr)
        payload = collect_subreddit(reddit=reddit, subreddit_name=name, cfg=cfg)
        out_file = output_dir / f"posts_{name.lower()}.json"
        write_json(out_file, payload)

        summary_rows.append(
            {
                "subreddit": name,
                "priority": payload.get("priority"),
                "focus": payload.get("focus"),
                "window_months": payload.get("window_months"),
                "post_count": payload.get("post_count"),
                "file": str(out_file),
            }
        )

    write_csv(output_dir / "collection_summary.csv", summary_rows)
    print(json.dumps({"status": "ok", "output_dir": str(output_dir), "subreddits": len(summary_rows)}))
    return 0


def iter_posts_from_raw(input_dir: Path) -> Iterable[Dict[str, Any]]:
    for path in sorted(input_dir.glob("posts_*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        subreddit = payload.get("subreddit")
        for post in payload.get("posts", []):
            yield {
                "subreddit": subreddit,
                "post": post,
            }


def compact_post_for_prompt(entry: Dict[str, Any]) -> Dict[str, Any]:
    post = entry["post"]
    return {
        "subreddit": entry.get("subreddit"),
        "id": post.get("id"),
        "title": post.get("title"),
        "body": post.get("body"),
        "flair": post.get("flair"),
        "score": post.get("score"),
        "comment_count": post.get("comment_count"),
        "created_at": post.get("created_at"),
        "top_comments": [
            {
                "id": c.get("id"),
                "score": c.get("score"),
                "body": c.get("body"),
            }
            for c in post.get("top_comments", [])
        ],
    }


def batch_items(items: List[Dict[str, Any]], batch_size: int) -> Iterable[List[Dict[str, Any]]]:
    for i in range(0, len(items), batch_size):
        yield items[i : i + batch_size]


def command_build_needs_batches(args: argparse.Namespace) -> int:
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    ensure_dir(output_dir)

    items = [compact_post_for_prompt(x) for x in iter_posts_from_raw(input_dir)]
    manifest: Dict[str, Any] = {
        "created_at": utc_now().isoformat(),
        "batch_size": args.batch_size,
        "total_posts": len(items),
        "batches": [],
    }

    for idx, chunk in enumerate(batch_items(items, args.batch_size), start=1):
        batch_id = f"batch_{idx:03d}"
        json_path = output_dir / f"{batch_id}.json"
        prompt_path = output_dir / f"{batch_id}_prompt.md"

        write_json(json_path, chunk)
        prompt_text = (
            f"# Prompt 1: Need Extraction\n\n"
            f"{PHASE1_PROMPT}\n"
            f"## Input JSON\n\n"
            f"```json\n{json.dumps(chunk, ensure_ascii=True, indent=2)}\n```\n"
        )
        prompt_path.write_text(prompt_text, encoding="utf-8")

        manifest["batches"].append(
            {
                "batch_id": batch_id,
                "post_count": len(chunk),
                "json_file": str(json_path),
                "prompt_file": str(prompt_path),
            }
        )

    write_json(output_dir / "manifest.json", manifest)
    print(json.dumps({"status": "ok", "output_dir": str(output_dir), "batches": len(manifest["batches"])}))
    return 0


def command_make_prompt_pack(args: argparse.Namespace) -> int:
    output_dir = Path(args.output_dir)
    ensure_dir(output_dir)

    files = {
        "prompt_2_cluster_and_rank.md": PHASE2_PROMPT,
        "prompt_3_product_ideation.md": PHASE3_PROMPT,
        "prompt_4_reality_check.md": PHASE4_PROMPT,
    }
    for filename, body in files.items():
        (output_dir / filename).write_text(body + "\n", encoding="utf-8")

    runbook = (
        "# Runbook\n\n"
        "1. Run Prompt 1 files in `phase2_batches/`.\n"
        "2. Merge all LLM outputs into `extracted_needs.json`.\n"
        "3. Run Prompt 2 with `extracted_needs.json` -> `ranked_clusters.json`.\n"
        "4. Run Prompt 3 with top clusters -> `product_concepts.json`.\n"
        "5. Run Prompt 4 with concepts -> `validated_opportunities.json`.\n"
        "6. Use `compile-report` command to generate final markdown.\n"
    )
    (output_dir / "runbook.md").write_text(runbook, encoding="utf-8")

    print(json.dumps({"status": "ok", "output_dir": str(output_dir), "files": len(files) + 1}))
    return 0


def _coerce_needs_payload(value: Any) -> List[Dict[str, Any]]:
    if isinstance(value, list):
        return [x for x in value if isinstance(x, dict)]
    if isinstance(value, dict):
        for key in ("results", "needs", "items", "data"):
            nested = value.get(key)
            if isinstance(nested, list):
                return [x for x in nested if isinstance(x, dict)]
        return [value]
    return []


def command_merge_needs(args: argparse.Namespace) -> int:
    input_dir = Path(args.input_dir)
    manifest_path = input_dir / "manifest.json"
    if not manifest_path.exists():
        raise RuntimeError(f"manifest not found: {manifest_path}")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    all_rows: List[Dict[str, Any]] = []
    missing: List[str] = []

    for batch in manifest.get("batches", []):
        batch_id = batch.get("batch_id")
        if not batch_id:
            continue
        result_file = input_dir / f"{batch_id}_result.json"
        if not result_file.exists():
            missing.append(batch_id)
            continue
        parsed = json.loads(result_file.read_text(encoding="utf-8"))
        rows = _coerce_needs_payload(parsed)
        for row in rows:
            if isinstance(row, dict) and "batch_id" not in row:
                row["batch_id"] = batch_id
            all_rows.append(row)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    write_json(output_path, all_rows)

    status = {
        "status": "ok",
        "output": str(output_path),
        "merged_rows": len(all_rows),
        "missing_batches": len(missing),
    }
    if missing:
        missing_path = output_path.with_name(output_path.stem + "_missing_batches.json")
        write_json(missing_path, missing)
        status["missing_file"] = str(missing_path)
    print(json.dumps(status))
    return 0


def command_compile_report(args: argparse.Namespace) -> int:
    clusters = json.loads(Path(args.clusters).read_text(encoding="utf-8"))
    concepts = json.loads(Path(args.concepts).read_text(encoding="utf-8"))
    validation = json.loads(Path(args.validation).read_text(encoding="utf-8"))

    top_n = args.top_n
    selected = clusters[:top_n]

    lines: List[str] = []
    lines.append("# Veteran Reddit Market Analysis - Final Opportunities")
    lines.append("")
    lines.append(f"Generated: {utc_now().isoformat()}")
    lines.append("")
    lines.append(f"Top {top_n} opportunities by adjusted monetization score.")
    lines.append("")

    for i, cluster in enumerate(selected, start=1):
        cname = cluster.get("cluster_name", f"Cluster {i}")
        score = cluster.get("monetization_score", "n/a")
        lines.append(f"## {i}. {cname}")
        lines.append("")
        lines.append(f"- Monetization score: {score}")
        lines.append(f"- Post count: {cluster.get('post_count', 'n/a')}")
        lines.append(f"- Avg emotional intensity: {cluster.get('average_emotional_intensity', 'n/a')}")

        concept_match = next((c for c in concepts if c.get("cluster_name") == cname), None)
        if concept_match:
            lines.append(f"- Product concept: {concept_match.get('product_name', 'n/a')}")
            lines.append(f"- Business model: {concept_match.get('business_model', 'n/a')}")
            lines.append(f"- MVP scope: {concept_match.get('quick_win_mvp_2_to_4_weeks', 'n/a')}")

        validation_match = next((v for v in validation if v.get("cluster_name") == cname), None)
        if validation_match:
            lines.append(f"- Final verdict: {validation_match.get('final_verdict', 'n/a')}")
            lines.append(f"- Revenue path: {validation_match.get('realistic_path_to_first_revenue', 'n/a')}")

        pain_points = cluster.get("top_3_pain_points", [])
        if pain_points:
            lines.append("- Representative pain points:")
            for pp in pain_points[:3]:
                if isinstance(pp, dict):
                    lines.append(f"  - {pp.get('pain_point', pp)}")
                else:
                    lines.append(f"  - {pp}")
        lines.append("")

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    print(json.dumps({"status": "ok", "output": str(out_path)}))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Veteran Reddit market analysis pipeline")
    sub = parser.add_subparsers(dest="command", required=True)

    p_collect = sub.add_parser("collect", help="Collect Phase 1 Reddit data")
    p_collect.add_argument("--subreddits", nargs="+", default=None)
    p_collect.add_argument("--months", type=int, default=12)
    p_collect.add_argument("--fallback-months", type=int, default=24)
    p_collect.add_argument("--min-score", type=int, default=5)
    p_collect.add_argument("--min-comments", type=int, default=10)
    p_collect.add_argument("--top-all-limit", type=int, default=400)
    p_collect.add_argument("--top-year-limit", type=int, default=400)
    p_collect.add_argument("--new-limit", type=int, default=400)
    p_collect.add_argument("--top-comment-limit", type=int, default=20)
    p_collect.add_argument("--keep-authors", action="store_true")
    p_collect.add_argument("--output-dir", default="outputs/raw")
    p_collect.set_defaults(func=command_collect)

    p_batches = sub.add_parser("build-needs-batches", help="Create Phase 2 batches and prompts")
    p_batches.add_argument("--input-dir", default="outputs/raw")
    p_batches.add_argument("--output-dir", default="outputs/phase2_batches")
    p_batches.add_argument("--batch-size", type=int, default=75)
    p_batches.set_defaults(func=command_build_needs_batches)

    p_pack = sub.add_parser("make-prompt-pack", help="Write Prompts 2-4 and runbook")
    p_pack.add_argument("--output-dir", default="outputs/prompt_pack")
    p_pack.set_defaults(func=command_make_prompt_pack)

    p_merge = sub.add_parser("merge-needs", help="Merge Prompt 1 batch outputs into one JSON")
    p_merge.add_argument("--input-dir", default="outputs/phase2_batches")
    p_merge.add_argument(
        "--output",
        default="outputs/ai/extracted_needs.json",
        help="Output JSON path for merged extracted needs",
    )
    p_merge.set_defaults(func=command_merge_needs)

    p_report = sub.add_parser("compile-report", help="Compile final markdown report")
    p_report.add_argument("--clusters", required=True, help="Path to ranked_clusters.json")
    p_report.add_argument("--concepts", required=True, help="Path to product_concepts.json")
    p_report.add_argument("--validation", required=True, help="Path to validated_opportunities.json")
    p_report.add_argument("--top-n", type=int, default=5)
    p_report.add_argument("--output", default="outputs/final_report.md")
    p_report.set_defaults(func=command_compile_report)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
