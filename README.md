# content-machine-lite

A free‑tier content pipeline for creators. It pulls fresh ideas from RSS sources and generates a weekly draft (no paid APIs required).

## Why it exists
Creators spend more time **finding ideas** than creating. This MVP reduces the blank‑page problem by turning trending sources into a draft you can review.

## What it does
- Fetches latest posts from RSS sources
- Picks top ideas
- Outputs a clean draft in `output/ideas.md`

## Quick start
```bash
cd content-machine-lite
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python content_machine.py
```

## Configure sources
Edit `sources.txt` with any RSS feeds you want (one per line).

## Optional: Kimi (free) for drafting
If you want LLM‑style drafting, set:
```
export KIMI_API_KEY=your_key
export KIMI_BASE_URL=https://integrate.api.nvidia.com/v1
export KIMI_MODEL=moonshotai/kimi-k2.5
```
Then re‑run:
```bash
python content_machine.py
```

## Output
- `output/ideas.md`
- `output/updates.txt` (news bot)

## News bot (macro updates)
```bash
python news_bot.py
```
Edit `news_sources.txt` to customize sources.

## Roadmap (short)
- Add Reddit/YouTube sources
- Add simple scheduling (Buffer/Typefully)
- Add multi‑format drafts (threads, newsletter, scripts)

## Notes
- MVP / demo. Replace RSS with Twitter/Reddit scraping later.
- Manual review is recommended before posting.
