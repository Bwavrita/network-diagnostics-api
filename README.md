# Network Diagnostics API

FastAPI REST API for simple network and host diagnostics.

## Features

- Health check endpoint
- Request headers inspection endpoint
- Server information endpoint:
  - Hostname
  - Platform/OS
  - CPU architecture

## Quick Start

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
git clone <repository-url>
cd network-diagnostics-api
pip install -r requirements.txt
```

### Run the API

```bash
# Development server (auto-reload)
uvicorn src.__main__:app --reload

# Or run as module
python -m src
```

API base URL: http://localhost:8000

Interactive docs:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Health

`GET /health`

```json
{
  "status": "ok"
}
```

### Headers

`GET /headers`

```json
{
  "headers": {
    "host": "localhost:8000",
    "user-agent": "python-httpx/0.25.2"
  }
}
```

### Server Info

`GET /server-info`

```json
{
  "hostname": "my-server",
  "platform": "Linux",
  "architecture": "x86_64"
}
```

## Testing

```bash
# All tests
pytest -v

# Specific files
pytest -v tests/health_test.py
pytest -v tests/network_test.py
```

## Code Quality and Security

This project uses Ruff, Pytest, Mypy, Bandit, pip-audit, and pre-commit.

### Ruff

```bash
# Lint
ruff check .

# Auto-fix lint issues when possible
ruff check . --fix

# Format
ruff format .
```

### Pytest

```bash
pytest -v
```

### Mypy

```bash
mypy src tests
```

### Bandit

```bash
bandit -c pyproject.toml -r src tests
```

### pip-audit

```bash
pip-audit -r requirements.txt
```

### pre-commit

```bash
# Install hooks
pre-commit install

# Run all hooks manually
pre-commit run --all-files
```

### Run everything (local CI-style)

```bash
ruff check .
ruff format --check .
pytest -v
mypy src tests
bandit -c pyproject.toml -r src tests
pip-audit -r requirements.txt
```

## Project Structure

```text
network-diagnostics-api/
├── src/
│   ├── __init__.py
│   ├── __main__.py
│   ├── args_parser.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── health.py
│   │   └── network.py
│   └── schemas/
│       └── server.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── health_test.py
│   └── network_test.py
├── pyproject.toml
├── requirements.txt
├── Dockerfile
├── Dockerfile.test
└── README.md
```

## Dependencies

- fastapi==0.115.0
- uvicorn[standard]==0.32.1
- pytest==9.0.3
- httpx==0.25.2
- pre-commit==4.5.1
- mypy==1.7.0
- bandit==1.7.6
- pip-audit==2.6.0
