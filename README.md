# Network Diagnostics API

A FastAPI-based REST API for diagnosing network and server information. Get details about the host system, request headers, and platform specifications through simple HTTP endpoints.

## 📋 Features

- **Health Check**: Basic endpoint to verify API availability
- **Request Headers**: Inspect request headers sent to the API
- **Server Information**: Retrieve detailed information about the host system
  - Hostname
  - Operating System details
  - CPU architecture

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd network-diagnostics-api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the API

**Option 1: Using Uvicorn directly (recommended for development)**
```bash
uvicorn app.__main__:app --reload
```

**Option 2: Using the Python module**
```bash
python -m app
```

The API will be available at `http://localhost:8000`

### API Documentation

Once the API is running, access the interactive documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📡 API Endpoints

### Health Check
```
GET /health
```
Returns the API status.

**Response:**
```json
{
  "status": "ok"
}
```

### Request Headers
```
GET /headers
```
Returns all headers from the incoming request.

**Response:**
```json
{
  "headers": {
    "host": "localhost:8000",
    "user-agent": "python-httpx/0.25.2",
    ...
  }
}
```

### Server Information
```
GET /server-info
```
Returns detailed information about the server/host system.

**Response:**
```json
{
  "hostname": "my-server",
  "platform": "Linux",
  "architecture": "x86_64",
}
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests with verbose output
pytest -v

# Run tests from a specific file
pytest tests/test_health.py

# Run tests with coverage report
pytest --cov=app
```

### Test Files

- `tests/test_health.py` - Tests for the health check endpoint
- `tests/test_network.py` - Tests for headers and server info endpoints

## 📁 Project Structure

```
network-diagnostics-api/
├── app/
│   ├── __init__.py          # Package initialization
│   ├── __main__.py          # Application entry point
│   └── routers/
│       ├── __init__.py
│       ├── health.py        # Health check router
│       └── network.py       # Network info routers
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Pytest configuration and fixtures
│   ├── test_health.py       # Health endpoint tests
│   └── test_network.py      # Network endpoint tests
├── requirements.txt         # Project dependencies
└── README.md               # This file
```

## 📦 Dependencies

- **fastapi** (0.104.1) - Modern web framework for building APIs with Python
- **uvicorn** (0.24.0) - ASGI web server for serving FastAPI applications
- **pytest** (7.4.3) - Testing framework
- **httpx** (0.25.2) - HTTP client library used by TestClient

## 🛠️ Development

### Installing development dependencies

```bash
pip install -r requirements.txt
```

### Running tests in watch mode

```bash
pytest --watch
```

### Code structure

Each router is located in `app/routers/` and contains FastAPI route handlers. Routes are registered in `app/__main__.py` using `app.include_router()`.
