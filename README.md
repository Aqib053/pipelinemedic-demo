# pipelinemedic-demo

Minimal FastAPI service used to demo
[PipelineMedic](https://hacktofuture4.vercel.app) — an AI copilot
that triages CI failures and opens auto-fix pull requests.

## The intentional bug

`app.py` exposes `GET /add/{a}/{b}` and currently returns `a - b`
instead of `a + b`. `tests/test_app.py` asserts `2 + 3 == 5`, which
fails, so CI goes red with:

```
AssertionError: expected 2 + 3 = 5, got -1
```

The failing log is sent to the PipelineMedic webhook. PipelineMedic
asks on Telegram, and on *Auto fix* it rewrites the buggy line in
`app.py` (the real source file) and opens a PR with that diff. Merge
it and CI goes green.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q                       # will fail until the PR is merged
uvicorn app:app --reload        # GET http://127.0.0.1:8000/add/2/3
```

## Wire CI to PipelineMedic

1. Repo **Settings → Secrets and variables → Actions**.
2. Add secret `PIPELINEMEDIC_WEBHOOK_URL`,
   value `https://hacktofuture4.vercel.app/webhook`.
3. Push any change — CI fails, PipelineMedic takes over in Telegram.
