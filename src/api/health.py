from fastapi import APIRouter
from pydantic import BaseModel
import logging

router = APIRouter()


class HealthResponse(BaseModel):
    status: str = "healthy"


@router.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check() -> HealthResponse:
    """Checks the health status of the chatbot service."""
    logging.info("Health check endpoint was accessed.")
    return HealthResponse(status="healthy")
