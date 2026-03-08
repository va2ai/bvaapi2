import json
import os
import glob

# Load existing VAClaims data from researcher directory
existing_dir = "C:/Users/ccdmn/code/researcher/opai/site/reddit-data/subreddits/VAClaims/top_month/post_jsons"
existing_posts = []

for fpath in sorted(glob.glob(os.path.join(existing_dir, "*.json"))):
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Extract post data from Reddit API format
        if isinstance(data, list) and len(data) > 0:
            listing = data[0]
            if isinstance(listing, dict) and "data" in listing:
                children = listing["data"].get("children", [])
                for child in children:
                    if child.get("kind") == "t3":
                        pd = child["data"]
                        post = {
                            "title": pd.get("title", ""),
                            "author": pd.get("author", ""),
                            "url": f"https://www.reddit.com{pd.get('permalink', '')}",
                            "selftext": pd.get("selftext", "")[:2000],
                            "score": pd.get("score", 0),
                            "created_utc": pd.get("created_utc", ""),
                            "subreddit": pd.get("subreddit", "VAClaims"),
                            "flair": pd.get("link_flair_text", None),
                            "top_comments": []
                        }
                        # Get comments from second listing
                        if len(data) > 1 and isinstance(data[1], dict):
                            comment_children = data[1].get("data", {}).get("children", [])
                            for cc in comment_children[:10]:
                                if cc.get("kind") == "t1":
                                    cd = cc["data"]
                                    post["top_comments"].append({
                                        "author": cd.get("author", ""),
                                        "body": cd.get("body", "")[:1000],
                                        "score": cd.get("score", 0)
                                    })
                        existing_posts.append(post)
    except Exception as e:
        print(f"Error reading {fpath}: {e}")

print(f"Loaded {len(existing_posts)} existing VAClaims posts")

# Save as a separate file
output = "C:/Users/ccdmn/code/bvaapi/reddit-data/posts_vaclaims_existing.json"
with open(output, "w", encoding="utf-8") as f:
    json.dump(existing_posts, f, indent=2, ensure_ascii=False)
print(f"Wrote {len(existing_posts)} posts to posts_vaclaims_existing.json")
