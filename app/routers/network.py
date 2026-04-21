import platform
import socket

from fastapi import APIRouter, Request

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


@router.get("/server-info")
async def server_info():
    """Get server information such as hostname, platform, architecture, etc.

    :return: Server information
    :rtype: dict
    """

    return {
        "hostname": socket.gethostname(),
        # Get the hostname of the server
        "platform": platform.system(),
        # Get the platform/OS name (e.g., 'Linux', 'Windows')
        "architecture": platform.machine(),
        # Get the machine architecture (e.g., 'x86_64')
    }
