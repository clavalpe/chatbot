from fastapi import APIRouter
from pydantic import BaseModel
import logging

router = APIRouter()


class ChatRequest(BaseModel):
    user: str


class ChatResponse(BaseModel):
    assistant: str


@router.post("/chat", response_model=ChatResponse, tags=["Chat"])
async def chat(request: ChatRequest) -> ChatResponse:
    """
    Allows interaction with a chatbot.
    """
    logging.info("Chat endpoint was accessed.")
    response = ChatResponse(
        assistant="Hello! of course, let me know how I can help you!."
    )
    return response
