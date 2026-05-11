import uvicorn
from fastapi import FastAPI

from app.args_parser import parse_args
from app.routers import health, network

app = FastAPI(title="Network Diagnostics API", version="1.0")

app.include_router(health.router, prefix="", tags=["health"])
app.include_router(network.router, prefix="", tags=["network"])


if __name__ == "__main__":
    args = parse_args()
    host = args.host
    port = args.port
    log_level = args.log_level
    uvicorn.run(app, host=host, port=port, log_level=log_level)
