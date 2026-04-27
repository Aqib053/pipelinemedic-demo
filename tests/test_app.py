import pytest  # noqa: F401

# --- PipelineMedic regression tests (auto-generated) ---

from fastapi.testclient import TestClient
from app import app

def test_add_returns_sum_of_two_integers() -> None:
    """Test that the /add endpoint returns the sum of two integers."""
    client = TestClient(app)
    response = client.get("/add/1/2")
    assert response.status_code == 200
    assert response.json()["result"] == 3


# --- PipelineMedic regression tests (auto-generated) ---

from fastapi.testclient import TestClient
from app import app

def test_add_regression() -> None:
    """Test that the /add endpoint returns the correct sum of two integers."""
    client = TestClient(app)
    response = client.get("/add/5/5")
    assert response.status_code == 200
    assert response.json()["result"] == 10
