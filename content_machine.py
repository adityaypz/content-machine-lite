import os
import time
import requests
import feedparser
from datetime import datetime, timezone

OUTPUT_DIR = "output"
IDEAS_PATH = os.path.join(OUTPUT_DIR, "ideas.md")
SOURCES_PATH = "sources.txt"

KIMI_API_KEY = os.getenv("KIMI_API_KEY")
KIMI_BASE_URL = os.getenv("KIMI_BASE_URL", "https://integrate.api.nvidia.com/v1")
KIMI_MODEL = os.getenv("KIMI_MODEL", "moonshotai/kimi-k2.5")


def load_sources():
    if not os.path.exists(SOURCES_PATH):
        return []
    with open(SOURCES_PATH, "r") as f:
        return [line.strip() for line in f if line.strip()]


def fetch_rss(url):
    return feedparser.parse(url)


def collect_items(sources, limit=20):
    items = []
    for url in sources:
        try:
            feed = fetch_rss(url)
            for entry in feed.entries[:10]:
                items.append({
                    "title": entry.get("title", ""),
                    "link": entry.get("link", ""),
                    "source": feed.feed.get("title", url),
                })
        except Exception:
            continue
    return items[:limit]


def draft_with_kimi(items):
    if not KIMI_API_KEY:
        return None
    prompt = """You are a content assistant. Create a weekly content draft from the following links.
Return:
- 10 post ideas
- 3 thread outlines
- 2 newsletter angles
Be concise."""
    body = "\n".join([f"- {i['title']} ({i['link']})" for i in items])
    payload = {
        "model": KIMI_MODEL,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": body},
        ],
        "temperature": 0.6,
    }
    headers = {"Authorization": f"Bearer {KIMI_API_KEY}"}
    r = requests.post(f"{KIMI_BASE_URL}/chat/completions", json=payload, headers=headers, timeout=30)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]


def write_output(items, draft=None):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(IDEAS_PATH, "w") as f:
        f.write(f"# Content Ideas ({datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')})\n\n")
        f.write("## Sources\n")
        for i in items:
            f.write(f"- {i['title']} — {i['link']} ({i['source']})\n")
        f.write("\n## Draft\n")
        if draft:
            f.write(draft)
        else:
            f.write("LLM not configured. Set KIMI_API_KEY to enable drafting.\n")


def main():
    sources = load_sources()
    if not sources:
        print("No sources found in sources.txt")
        return
    items = collect_items(sources)
    draft = None
    try:
        draft = draft_with_kimi(items)
    except Exception:
        draft = None
    write_output(items, draft)
    print(f"Wrote {IDEAS_PATH}")


if __name__ == "__main__":
    main()
