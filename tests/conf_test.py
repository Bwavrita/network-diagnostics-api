import pytest
from fastapi.testclient import TestClient

from app.__main__ import app


@pytest.fixture
def client():
    """Get the TestClient for the FastAPI app.

    :return: TestClient instance for the FastAPI app
    :rtype: TestClient
    """
    return TestClient(app)
