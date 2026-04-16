import pytest  # noqa: F401

# --- PipelineMedic regression tests (auto-generated) ---

from fastapi.testclient import TestClient
from app import app

def test_add_returns_sum_of_two_integers() -> None:
    """Test that the /add endpoint correctly adds two integers."""
    client = TestClient(app)
    response = client.get("/add/2/3")
    assert response.status_code == 200
    assert response.json()["result"] == 5


# --- PipelineMedic regression tests (auto-generated) ---

from fastapi.testclient import TestClient
from app import app

def test_add_regression() -> None:
    """Test that the /add endpoint correctly adds two integers."""
    client = TestClient(app)
    response = client.get("/add/1/2")
    assert response.status_code == 200
    assert response.json()["result"] == 3


# --- PipelineMedic regression tests (auto-generated) ---

from fastapi.testclient import TestClient
from app import app

def test_add_endpoint_regression() -> None:
    """Test that the /add endpoint correctly adds two integers."""
    client = TestClient(app)
    response = client.get("/add/4/5")
    assert response.status_code == 200
    assert response.json()["result"] == 9
