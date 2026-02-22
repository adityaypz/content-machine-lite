import os
import feedparser
from datetime import datetime, timezone

OUT_DIR = "output"
OUT_PATH = os.path.join(OUT_DIR, "updates.txt")
SOURCES_PATH = "news_sources.txt"
MAX_ITEMS = 10


def load_sources():
    if not os.path.exists(SOURCES_PATH):
        return []
    with open(SOURCES_PATH, "r") as f:
        return [line.strip() for line in f if line.strip()]


def collect_items(sources, limit=MAX_ITEMS):
    items = []
    for url in sources:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]:
                items.append({
                    "title": entry.get("title", ""),
                    "link": entry.get("link", ""),
                    "source": feed.feed.get("title", url),
                })
        except Exception:
            continue
    # simple de-dup by title
    seen = set()
    uniq = []
    for it in items:
        t = it["title"].strip()
        if t and t not in seen:
            uniq.append(it)
            seen.add(t)
    return uniq[:limit]


def write_updates(items):
    os.makedirs(OUT_DIR, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    with open(OUT_PATH, "w") as f:
        f.write(f"# Automated News Updates ({ts})\n\n")
        for i, it in enumerate(items, 1):
            f.write(f"{i}. {it['title']}\n   {it['link']}\n")


def main():
    sources = load_sources()
    if not sources:
        print("No sources found in news_sources.txt")
        return
    items = collect_items(sources)
    write_updates(items)
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
