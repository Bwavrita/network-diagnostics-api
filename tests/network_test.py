import platform
import socket


def test_get_headers(client):
    """Test the /headers endpoint to ensure it returns the expected headers.

    :param client: TestClient fixture for making requests to the FastAPI app
    :type client: TestClient
    """
    response = client.get("/headers")

    assert response.status_code == 200

    data = response.json()
    assert "headers" in data
    assert isinstance(data["headers"], dict)


def test_get_headers_content(client):
    """Test the /headers endpoint to ensure it returns the expected headers content.

    :param client: TestClient fixture for making requests to the FastAPI app
    :type client: TestClient
    """
    response = client.get("/headers")
    data = response.json()
    headers = data["headers"]

    assert "host" in headers
    assert "user-agent" in headers


def test_server_info(client):
    """Test the /server-info endpoint to ensure
    it returns the expected server information.

    :param client: TestClient fixture for making requests to the FastAPI app
    :type client: TestClient
    """
    response = client.get("/server-info")

    assert response.status_code == 200

    data = response.json()
    assert "hostname" in data
    assert "platform" in data
    assert "architecture" in data


def test_server_info_content(client):
    """Test the /server-info endpoint to ensure
    it returns valid server information content.

    :param client: TestClient fixture for making requests to the FastAPI app
    :type client: TestClient
    """

    response = client.get("/server-info")
    data = response.json()

    assert data["hostname"] == socket.gethostname()
    assert data["platform"] == platform.system()
    assert data["architecture"] == platform.machine()
