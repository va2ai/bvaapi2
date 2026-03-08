#!/usr/bin/env python3
"""Reddit Market Analysis Phases 2-5 using Gemini 2.5 Pro via Vertex AI."""

import json, os, glob, time

from google import genai
from google.genai import types

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
CLIENT = genai.Client(vertexai=True, project="vaclaims-194006", location="us-central1")
MODEL = "gemini-2.5-pro"


def load_all_posts():
    posts = []
    for f in sorted(glob.glob(os.path.join(DATA_DIR, "posts_*.json"))):
        with open(f, "r", encoding="utf-8") as fh:
            data = json.load(fh)
            sub = os.path.basename(f).replace("posts_", "").replace(".json", "")
            for p in data:
                p.setdefault("subreddit", sub)
            posts.extend(data)
    print(f"Loaded {len(posts)} posts from {len(glob.glob(os.path.join(DATA_DIR, 'posts_*.json')))} files")
    return posts


def call_gemini(prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            resp = CLIENT.models.generate_content(
                model=MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.3,
                    max_output_tokens=65536,
                    response_mime_type="application/json",
                ),
            )
            text = resp.text.strip()
            return json.loads(text)
        except json.JSONDecodeError:
            # Try to extract JSON from markdown fences
            import re
            m = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
            if m:
                return json.loads(m.group(1).strip())
            print(f"  JSON parse failed (attempt {attempt+1}), retrying...")
        except Exception as e:
            print(f"  API error (attempt {attempt+1}): {e}")
            if attempt < max_retries - 1:
                time.sleep(5 * (attempt + 1))
    raise RuntimeError("Gemini call failed after retries")


def save(filename, data):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Wrote {path} ({len(data)} items)")


# ── Phase 2: Need Extraction ──────────────────────────────────────

def phase2(posts):
    print("\n=== PHASE 2: Need Extraction ===")
    all_needs = []
    batch_size = 30
    for i in range(0, len(posts), batch_size):
        batch = posts[i:i+batch_size]
        print(f"  Processing batch {i//batch_size + 1} ({len(batch)} posts)...")
        prompt = f"""You are a market research analyst specializing in the U.S. veteran community.
Analyze these Reddit posts and for EACH post extract:

1. title: the original post title
2. subreddit: the source subreddit
3. primary_need: What is the veteran trying to accomplish or solve?
4. pain_points: Array of specific frustrations or blockers
5. current_solution: What are they currently doing? (DIY, paid service, VSO, nothing, etc.)
6. emotional_intensity: Rate 1-5 (1=mild inconvenience, 5=desperate/life-impacting)
7. category: One of: Claims/Ratings, Appeals, Healthcare, Mental Health, Employment/Transition, Education/GI Bill, Housing/VA Loan, Financial, Legal, Community/Social, Policy/DOGE, Other

VA Jargon: C&P=Compensation & Pension exam, HLR=Higher Level Review, TDIU=Total Disability Individual Unemployability, P&T=Permanent & Total, SMC=Special Monthly Compensation, ITF=Intent to File, BDD=Benefits Delivery at Discharge, DBQ=Disability Benefits Questionnaire, VSO=Veterans Service Organization, MST=Military Sexual Trauma, nexus=medical opinion linking condition to service.

Return a JSON array with one object per post.

POSTS:
{json.dumps(batch, indent=1, ensure_ascii=False)[:80000]}"""

        needs = call_gemini(prompt)
        all_needs.extend(needs)
        save("needs_extracted.json", all_needs)
        time.sleep(2)

    print(f"Phase 2 complete: {len(all_needs)} needs extracted")
    return all_needs


# ── Phase 3: Cluster & Rank ───────────────────────────────────────

def phase3(needs):
    print("\n=== PHASE 3: Cluster & Rank ===")
    prompt = f"""You are a market strategist analyzing the U.S. veteran services market.
Here is a dataset of {len(needs)} extracted needs from veteran Reddit communities.

Do the following:
1. GROUP similar needs into 10-20 distinct opportunity clusters
2. For each cluster provide:
   - cluster_name: clear, descriptive
   - post_count: number of posts in this cluster
   - avg_emotional_intensity: average 1-5
   - top_pain_points: top 3 specific pain points with example quotes from the data
   - current_solutions: what people are currently using
   - gap_analysis: what's missing from current solutions
3. RANK all clusters by monetization_score (1-100) based on:
   - Frequency (how many people have this need)
   - Intensity (how painful is this problem)
   - Willingness to pay (are people already paying for partial solutions?)
   - AI solvability (can AI meaningfully improve this?)

Return a JSON array sorted by monetization_score descending.

NEEDS DATA:
{json.dumps(needs, indent=1, ensure_ascii=False)[:120000]}"""

    clusters = call_gemini(prompt)
    save("clusters_ranked.json", clusters)
    print(f"Phase 3 complete: {len(clusters)} clusters")
    return clusters


# ── Phase 4: Product Ideation ─────────────────────────────────────

def phase4(clusters):
    print("\n=== PHASE 4: Product Ideation ===")
    top = clusters[:10]
    prompt = f"""You are an AI product strategist specializing in veteran services.
For each of the top {len(top)} opportunity clusters below, propose 1-2 AI-powered product concepts.

For each concept provide:
- product_name: catchy, veteran-friendly
- one_liner: what it does in one sentence
- cluster_name: which cluster it addresses
- ai_capabilities: which AI tech powers it (LLM, RAG, NLP, computer vision, etc.)
- target_user: who buys/uses (veteran, VSO, attorney, VA employee)
- business_model: SaaS, per-use, freemium, B2B license, marketplace
- revenue_estimate: rough TAM and pricing logic
- competitive_landscape: what exists today, what's the moat
- build_complexity: Low/Medium/High and why
- mvp_potential: could MVP be built in 2-4 weeks? what would it look like?

Filter through these business lenses:
- B2B to VA-accredited professionals (attorneys, claims agents, VSOs) -- primary channel
- Direct-to-veteran SaaS -- lower price, massive TAM (~18M veterans)
- Hybrid marketplace -- AI-powered matching veterans to professionals
- Data/intelligence products -- aggregated insights for law firms, VSOs, policy orgs

Return a JSON array of product concept objects.

CLUSTERS:
{json.dumps(top, indent=1, ensure_ascii=False)}"""

    products = call_gemini(prompt)
    save("product_concepts.json", products)
    print(f"Phase 4 complete: {len(products)} product concepts")
    return products


# ── Phase 5: Validation & Final Report ────────────────────────────

def phase5(clusters, products):
    print("\n=== PHASE 5: Validation & Final Report ===")
    prompt = f"""You are validating AI product concepts for the veteran services market.

CONTEXT about the builder:
- AI software engineer and former VA disability consultant, 15+ years experience
- Runs Veteran 2 Veteran LLC building AI tools for VA-accredited legal professionals
- Has existing BVA research platform with MCP/REST API (23 endpoints on GCP Cloud Run)
  - BVA decision search, case parsing, CAVC precedent lookup
  - 38 CFR navigator with diagnostic code lookup (49 codes)
  - Federal Register VA document search
  - KnowVA knowledge base search
  - RAG search with ChromaDB + Vertex AI embeddings
- React Native app in development (Vet Dynamic) for accredited professionals
- V2V website with blog, guides, news section
- MCP server with 23 tools, deployed on GCP as streamable-http
- Tech stack: Python/FastAPI, React Native, GCP Cloud Run, ChromaDB, Vertex AI

For each product concept below, assess:
1. alignment: Does this align with or extend current tech stack and positioning?
2. regulatory_risks: 38 CFR, OGC accreditation rules, unauthorized practice risks
3. path_to_revenue: Realistic path to first dollar
4. two_week_mvp: What can be built as MVP in 2 weeks using Claude, BVA MCP server, React Native?
5. verdict: "Build Now" / "Build Next" / "Shelf It" with one-sentence rationale

Then compile a final report with:
- top_5_opportunities: ranked by adjusted score post-validation
- For each: problem_statement, product_concept, business_model, mvp_scope, timeline
- evidence_quotes: 3-5 representative Reddit quotes per opportunity
- competitive_landscape: summary per opportunity
- recommended_build_order: considering existing Vet Dynamic roadmap

Return as a JSON object with keys: validated_products (array), top_5_opportunities (array), recommended_build_order (array of product names in order).

CLUSTERS:
{json.dumps(clusters[:10], indent=1, ensure_ascii=False)}

PRODUCT CONCEPTS:
{json.dumps(products, indent=1, ensure_ascii=False)}"""

    report = call_gemini(prompt)
    path = os.path.join(DATA_DIR, "final_report.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"Wrote {path}")
    print("Phase 5 complete!")
    return report


# ── Main ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    posts = load_all_posts()
    needs = phase2(posts)
    clusters = phase3(needs)
    products = phase4(clusters)
    report = phase5(clusters, products)
    print("\n=== ALL PHASES COMPLETE ===")
    if "top_5_opportunities" in report:
        print(f"\nTop 5 Opportunities:")
        for i, opp in enumerate(report["top_5_opportunities"], 1):
            name = opp.get("product_concept", opp.get("product_name", "unnamed"))
            verdict = opp.get("verdict", "")
            print(f"  {i}. {name} -- {verdict}")
