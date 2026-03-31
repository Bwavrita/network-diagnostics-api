import pytest


def test_health_check(client):
    """Test the /health endpoint to ensure it returns the expected status.

    :param client: TestClient fixture for making requests to the FastAPI app
    :type client: TestClient
    """    
    response = client.get("/health")
    
    assert response.status_code == 200
    
    data = response.json()
    assert data["status"] == "ok"


def test_health_returns_json(client):
    """Test that the /health endpoint returns a JSON response.

    :param client: TestClient fixture for making requests to the FastAPI app
    :type client: TestClient
    """    
    response = client.get("/health")
    
    assert response.headers["content-type"] == "application/json"
    
    assert isinstance(response.json(), dict)