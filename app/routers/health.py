from fastapi import APIRouter

from app.schemas.server import HealthCheckResponse

router = APIRouter()


@router.get("/health", response_model=HealthCheckResponse)
async def health_check() -> HealthCheckResponse:
    """Router for health check endpoint.

    :return: Health status
    :rtype: HealthCheckResponse
    """
    return HealthCheckResponse(status="ok")
