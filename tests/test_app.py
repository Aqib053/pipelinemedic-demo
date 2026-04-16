import pytest  # noqa: F401

# --- PipelineMedic regression tests (auto-generated) ---

from fastapi.testclient import TestClient
from app import app

def test_add_endpoint_regression() -> None:
    """Test that the /add endpoint correctly adds two integers."""
    client = TestClient(app)
    response = client.get("/add/2/3")
    assert response.json()["result"] == 5
