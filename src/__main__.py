import uvicorn
from fastapi import FastAPI

from src.routers import health, network

app = FastAPI(title="Network Diagnostics API", version="1.0")

app.include_router(health.router, prefix="", tags=["health"])
app.include_router(network.router, prefix="", tags=["network"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
