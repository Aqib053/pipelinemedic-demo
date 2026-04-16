"""Smoke tests for the pipelinemedic-demo service.

`from app import app` triggers the import of `requests`, which is
initially missing from requirements.txt, so this test module fails
to collect until PipelineMedic's auto-fix PR is merged.
"""

from __future__ import annotations

from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_root_returns_service_metadata() -> None:
    response = client.get("/")
    assert response.status_code == 200
    body = response.json()
    assert body["service"] == "pipelinemedic-demo"
    assert body["status"] == "ok"


def test_health_reports_requests_version() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert "requests_version" in body
