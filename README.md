# content-machine-lite

Free‑tier content pipeline for creators. Pulls fresh ideas from RSS sources and generates a weekly content draft (no paid APIs required).

## What it does
- Fetches latest posts from RSS sources
- Picks top ideas
- Outputs a simple content draft in `output/ideas.md`

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

## Notes
- This is an MVP / demo. You can replace RSS with Twitter/Reddit scraping later.
- Manual review is recommended before posting.
