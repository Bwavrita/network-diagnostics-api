import uvicorn

from fastapi import FastAPI
from app.routers import health, network

def main():
    app = FastAPI(title="Network Diagnostics API", version="1.0")

    app.include_router(health.router, prefix="", tags=["health"])
    app.include_router(network.router, prefix="", tags=["network"])
    
    return app

if __name__ == "__main__":
    uvicorn.run(main(), host="0.0.0.0", port=8000)
