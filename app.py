"""pipelinemedic-demo service.

A tiny FastAPI microservice used to demo the PipelineMedic flow:
CI runs pytest -> ModuleNotFoundError: No module named 'requests'
-> PipelineMedic receives the log -> asks on Telegram -> Auto-fix PR
adds `requests` to requirements.txt -> Merge -> CI goes green.

The `requests` import below is INTENTIONALLY not declared in
requirements.txt on the first run. Do not "fix" it by hand — that's
what PipelineMedic is for.
"""

from __future__ import annotations

import os
import sys

from fastapi import FastAPI, HTTPException

import requests

app = FastAPI(title="pipelinemedic-demo", version="0.1.0")


@app.get("/")
def root() -> dict[str, str]:
    return {"service": "pipelinemedic-demo", "status": "ok"}


@app.get("/health")
def health() -> dict[str, object]:
    return {
        "status": "ok",
        "python": sys.version.split()[0],
        "requests_version": requests.__version__,
        "env": os.getenv("APP_ENV", "dev"),
    }


@app.get("/weather/{city}")
def weather(city: str) -> dict[str, object]:
    """Return a short weather summary for `city` via wttr.in."""
    url = f"https://wttr.in/{city}"
    try:
        resp = requests.get(url, params={"format": "%C+%t"}, timeout=5)
        resp.raise_for_status()
    except requests.RequestException as exc:
        raise HTTPException(status_code=502, detail=f"upstream error: {exc}") from exc
    return {"city": city, "summary": resp.text.strip()}
