# Veteran Reddit Market Analysis Pipeline

This folder contains an executable workflow for the March 2026 veteran-market analysis plan.

## What It Does

1. Collects Reddit posts/comments from target veteran subreddits.
2. Builds Phase 2 LLM batch inputs and prompt files.
3. Generates prompt pack files for clustering, ideation, and reality-check phases.
4. Compiles a final markdown report from AI output JSON files.

## Setup

```bash
cd C:\Users\ccdmn\code\bvaapi\reddit-data
pip install -r requirements.txt
```

Set Reddit API credentials:

```bash
set REDDIT_CLIENT_ID=your_client_id
set REDDIT_CLIENT_SECRET=your_client_secret
set REDDIT_USER_AGENT=veteran-market-analysis/1.0
```

## Commands

### 1) Collect raw Reddit data (Phase 1)

```bash
python pipeline.py collect --output-dir outputs/raw
```

Optional examples:

```bash
python pipeline.py collect --subreddits VeteransBenefits Veterans --months 12 --fallback-months 24
python pipeline.py collect --min-score 5 --min-comments 10 --top-comment-limit 20
```

### 2) Build need-extraction batches (Phase 2)

```bash
python pipeline.py build-needs-batches --input-dir outputs/raw --output-dir outputs/phase2_batches --batch-size 75
```

This creates:
- `batch_XXX.json` (input payload)
- `batch_XXX_prompt.md` (Prompt 1 + embedded payload)
- `manifest.json`

### 3) Generate prompt pack for Phases 3-5

```bash
python pipeline.py make-prompt-pack --output-dir outputs/prompt_pack
```

Creates:
- `prompt_2_cluster_and_rank.md`
- `prompt_3_product_ideation.md`
- `prompt_4_reality_check.md`
- `runbook.md`

### 4) Merge Prompt 1 outputs

After you run each `batch_XXX_prompt.md` in your LLM, save each response as:
- `outputs/phase2_batches/batch_001_result.json`
- `outputs/phase2_batches/batch_002_result.json`
- ...

Then merge all available results:

```bash
python pipeline.py merge-needs --input-dir outputs/phase2_batches --output outputs/ai/extracted_needs.json
```

### 5) Compile final report

After you run AI steps and save their outputs as JSON:

```bash
python pipeline.py compile-report \
  --clusters outputs/ai/ranked_clusters.json \
  --concepts outputs/ai/product_concepts.json \
  --validation outputs/ai/validated_opportunities.json \
  --output outputs/final_report.md
```

## Output Layout

```text
outputs/
  raw/
    posts_<subreddit>.json
    collection_summary.csv
  phase2_batches/
    batch_001.json
    batch_001_prompt.md
    batch_001_result.json
    manifest.json
  prompt_pack/
    prompt_2_cluster_and_rank.md
    prompt_3_product_ideation.md
    prompt_4_reality_check.md
    runbook.md
  ai/
    extracted_needs.json
  final_report.md
```

## Notes

- By default, author identities are anonymized (`author_hash`).
- Use `--keep-authors` only if you explicitly need usernames.
- Collection uses `Top (all)`, `Top (year)`, and `New`, then de-duplicates submissions.
- Filters match your plan default: `score >= 5` OR `comments >= 10`.
