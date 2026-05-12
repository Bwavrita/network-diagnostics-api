import platform
import socket

from fastapi import APIRouter, Request
from src.schemas.server import ServerInfoResponse

router = APIRouter()


@router.get("/headers")
async def get_headers(request: Request):
    """Get headers from the incoming request.

    :param request: The incoming HTTP request
    :type request: Request
    :return: Headers from the request
    :rtype: dict
    """
    return {"headers": dict(request.headers)}


@router.get("/server-info", response_model=ServerInfoResponse)
async def server_info() -> ServerInfoResponse:
    """Get server information such as hostname, platform, architecture, etc.

    :return: Server information
    :rtype: ServerInfoResponse
    """

    return ServerInfoResponse(
        hostname=socket.gethostname(),
        # Get the hostname of the server
        platform=platform.system(),
        # Get the platform/OS name (e.g., 'Linux', 'Windows')
        architecture=platform.machine(),
        # Get the machine architecture (e.g., 'x86_64')
    )
