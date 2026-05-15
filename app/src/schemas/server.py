from pydantic import BaseModel


class HealthCheckResponse(BaseModel):
    status: str


class ServerInfoResponse(BaseModel):
    hostname: str
    platform: str
    architecture: str
