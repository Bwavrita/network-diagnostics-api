from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    """Router for health check endpoint.

    :return: Health status
    :rtype: dict
    """    
    return {"status": "ok"}