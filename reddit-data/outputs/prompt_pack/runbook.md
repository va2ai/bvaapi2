# Runbook

1. Run Prompt 1 files in `phase2_batches/`.
2. Merge all LLM outputs into `extracted_needs.json`.
3. Run Prompt 2 with `extracted_needs.json` -> `ranked_clusters.json`.
4. Run Prompt 3 with top clusters -> `product_concepts.json`.
5. Run Prompt 4 with concepts -> `validated_opportunities.json`.
6. Use `compile-report` command to generate final markdown.
