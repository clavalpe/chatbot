from fastapi import FastAPI
from typing import Dict
from pydantic import BaseModel

app = FastAPI(
    title="Chatbot API",
    description="This service permits to interact with a chatbot.",
    version="0.1.0",
    docs_url="/swagger",  
)

class HealthResponse(BaseModel):
    status: str = "healthy"

@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check() -> HealthResponse:
    '''Checks the health status of the chatbot.'''
    return HealthResponse(status="healthy")