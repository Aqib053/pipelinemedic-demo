"""Tests for the pipelinemedic-demo service."""

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


def test_add_returns_sum_of_two_integers() -> None:
    response = client.get("/add/2/3")
    assert response.status_code == 200
    body = response.json()
    assert body["a"] == 2
    assert body["b"] == 3
    assert body["sum"] == 5, f"expected 2 + 3 = 5, got {body['sum']}"


def test_add_handles_negative_numbers() -> None:
    response = client.get("/add/-4/7")
    assert response.status_code == 200
    assert response.json()["sum"] == 3
