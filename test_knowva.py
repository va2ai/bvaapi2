"""Quick smoke test for KnowVA API endpoints."""
import requests, json

KNOWVA_BASE = "https://www.knowva.ebenefits.va.gov/system/ws/v11"
PORTAL_ID = "554400000001018"
COMMON = {"$lang": "en-us", "usertype": "customer", "portalId": PORTAL_ID}
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://www.knowva.ebenefits.va.gov/",
    "Origin": "https://www.knowva.ebenefits.va.gov",
}


def get(path, extra={}):
    resp = requests.get(f"{KNOWVA_BASE}/{path}", params={**COMMON, **extra},
                        headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return resp.json()


def test_topics():
    data = get("ss/topic", {"$attribute": "name,id,parentTopicId,totalArticleCount",
                             "$level": 0, "$pagenum": 0, "$pagesize": 1000})
    raw = data.get("topicTree", [])
    print(f"Topics: {len(raw)}")
    for entry in raw[:5]:
        t = entry.get("topic", entry)
        print(f"  [{t['id']}] {t['name']} ({t.get('articleTotalCount', 0)} articles)")
    return raw


def test_search(q="PTSD"):
    data = get("ss/search/kb", {"$attribute": "name,id,snippet", "$pagenum": 1,
                                 "$pagesize": 5, "federated": "true", "q": q})
    top_keys = list(data.keys())[:5]
    raw = data.get("article", data.get("items", []))
    total = data.get("totalCount", data.get("count", len(raw)))
    print(f"\nSearch '{q}': total={total}, keys={top_keys}, results={len(raw)}")
    for r in raw[:3]:
        print(f"  [{r['id']}] {r['name'][:80]}")
    return data


def test_article(article_id=554400000073398):
    data = get(f"ss/article/{article_id}", {"$attribute": "name,id,lastModifiedDate,contentText"})
    raw = data.get("article", [data])
    a = raw[0] if raw else {}
    text = a.get("contentText", "")
    print(f"\nArticle {article_id}: {a.get('name', '')[:80]}")
    print(f"  Content: {len(text)} chars  |  preview: {text[:150]}")
    return a


def test_popular():
    data = get("ss/dfaq", {"$attribute": "name,id,milestone", "$pagenum": 1, "$pagesize": 5})
    raw = data.get("article", data.get("items", []))
    print(f"\nPopular: {len(raw)} articles")
    for r in raw:
        print(f"  [{r['id']}] {r['name'][:80]}")
    return raw


if __name__ == "__main__":
    test_topics()
    test_search("PTSD")
    test_article()
    test_popular()
    print("\nAll OK.")
