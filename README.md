# pipelinemedic-demo

Minimal FastAPI microservice used to demonstrate
[PipelineMedic](https://hacktofuture4.vercel.app) — an AI copilot
that triages CI failures and opens auto-fix pull requests.

## What makes this repo special

`app.py` imports `requests`, but `requests` is deliberately **not**
listed in `requirements.txt`. On every push, the CI workflow runs
`pytest`, fails with

```
ModuleNotFoundError: No module named 'requests'
```

sends the log to the PipelineMedic webhook, and lets PipelineMedic
drive the rest of the loop:

1. Analyse the failure with an LLM (Groq, traced by Langfuse).
2. Send a Telegram message with an **Auto fix / Manual fix** choice.
3. On *Auto fix*: create a branch, add `requests` to
   `requirements.txt`, open a PR.
4. Ask for **Merge to main / Rollback** in Telegram.
5. Merge, or close the PR and delete the AI branch.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install requests   # required only until the auto-fix PR is merged
uvicorn app:app --reload
```

Useful endpoints:

- `GET /` — service metadata
- `GET /health` — runtime info
- `GET /weather/{city}` — short weather summary from wttr.in

## Run tests

```bash
pytest -q
```

## Wire CI to PipelineMedic

1. On the repo: **Settings → Secrets and variables → Actions**.
2. Add secret `PIPELINEMEDIC_WEBHOOK_URL`, value
   `https://hacktofuture4.vercel.app/webhook`.
3. Push any change — CI will fail, PipelineMedic will take over in
   Telegram.
