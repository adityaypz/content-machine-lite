# Sample Run (no API key)

```bash
cd content-machine-lite
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python content_machine.py
```

Output:
- `output/ideas.md`

Sample output excerpt:
```
# Content Ideas (2026-02-22 04:41 UTC)

## Sources
- Japanese Woodblock Print Search — https://ukiyo-e.org/ (Hacker News)
- How I use Claude Code: Separation of planning and execution — https://boristane.com/blog/how-i-use-claude-code/ (Hacker News)
...

## Draft
LLM not configured. Set KIMI_API_KEY to enable drafting.
```
