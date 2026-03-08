import json
import os

def make_post(title, author, url, selftext, score, date, subreddit, comments=None, flair=None):
    return {
        "title": title, "author": author, "url": url, "selftext": selftext,
        "score": score, "created_utc": date, "subreddit": subreddit,
        "flair": flair, "top_comments": comments or []
    }

def make_comment(author, text, score):
    return {"author": author, "body": text, "score": score}

def append_posts(filename, new_posts):
    filepath = os.path.join("C:/Users/ccdmn/code/bvaapi/reddit-data", filename)
    existing = []
    if os.path.exists(filepath):
        with open(filepath, encoding="utf-8") as f:
            existing = json.load(f)
    existing_urls = {p["url"] for p in existing}
    added = 0
    for p in new_posts:
        if p["url"] not in existing_urls:
            existing.append(p)
            existing_urls.add(p["url"])
            added += 1
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
    print(f"  {filename}: +{added} new (total: {len(existing)})")

# ---- Round 3: suicide/mental health crisis + VA healthcare ----

new_vb = [
    make_post(
        "Suicide, what will happen if I'm honest",
        "Old_Statistician4863",
        "https://www.reddit.com/r/VeteransBenefits/comments/1k4yr7z/suicide_what_will_happen_if_im_honest/",
        "I'm finally ready to come clean about what's really happening inside my head. I have spoken with chaplains more times than I can count, and it always ends in them recommending I seek treatment, but I never wanted to jeopardize the mission. I didn't want to burden my team more than they already were.",
        38, "2025-04-22", "VeteransBenefits"
    ),
    make_post(
        "What is it like going to the VA ER for suicidal ideation?",
        "Jeremiah_17_14",
        "https://www.reddit.com/r/VeteransBenefits/comments/1iqmrrd/what_is_it_like_going_to_the_va_er_for_suicidal/",
        "I'm nervous about going, although ideation is rapidly getting worse.",
        35, "2025-02-16", "VeteransBenefits",
        [
            make_comment("HiroshimaBob_4389", "Go, I've been on the cusp of going, but had a failed attempt instead. Don't mess around, go.", 89),
            make_comment("DrowningInFun", "If you have ideation, you are already trapped. Going is how you escape.", 148)
        ]
    ),
]

new_vet = [
    make_post(
        "I need mental help and the VA won't help me that much. What can I do?",
        "veteranthrowaway100",
        "https://www.reddit.com/r/Veterans/comments/1jvlknl/i_need_mental_help_and_the_va_wont_help_me_that/",
        "I got honorably chaptered out of the Army last year due to having suicidal ideations. I was told by my chain of command that the VA was going to help me. When I got out I called the VA and they said since I only did 18 months active duty I wasn't getting any benefits or help.",
        25, "2025-04-10", "Veterans"
    ),
]

new_va_affairs = [
    make_post(
        "House Bill: Veterans' ACCESS Act of 2025",
        "Impressive-Drink-336",
        "https://www.reddit.com/r/VeteransAffairs/comments/1ivobex/house_bill_veterans_access_act_of_2025/",
        "Thoughts on the ACCESS Act?",
        49, "2025-02-22", "VeteransAffairs",
        [
            make_comment("JAAAMBOOO", "This is basically the 'Remove resources from an organization, claim it is inefficient, then repeat' cycle.", 94),
            make_comment("JAAAMBOOO", "Where is the oversight that community care provides better quality at lower cost?", 28)
        ]
    ),
]

print("Appending round 3...")
append_posts("posts_veteransbenefits.json", new_vb)
append_posts("posts_veterans.json", new_vet)
append_posts("posts_veteransaffairs.json", new_va_affairs)

# Final count
total = 0
d = "C:/Users/ccdmn/code/bvaapi/reddit-data"
for f in sorted(os.listdir(d)):
    if f.endswith(".json"):
        with open(os.path.join(d, f), encoding="utf-8") as fp:
            data = json.load(fp)
        print(f"  {f}: {len(data)} posts")
        total += len(data)
print(f"\n  GRAND TOTAL: {total} posts")
