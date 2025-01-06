from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import logging

from src.api.chat_open_ai_client import LangChainClient, OpenAIClientError

router = APIRouter()

ai_client = LangChainClient()


class ChatRequest(BaseModel):
    user: str = Field(..., json_schema_extra={"example": "Can you help me?"})


class ChatResponse(BaseModel):
    assistant: str


class AIClientInvocationError(Exception): ...


@router.post("/chat", response_model=ChatResponse, tags=["Chat"])
async def chat(request: ChatRequest) -> ChatResponse:
    """
    Allows interaction with a chatbot.
    """
    logging.info("Chat endpoint was accessed.")

    if not request.user:
        raise HTTPException(status_code=400, detail="The request cannot be empty.")

    if len(request.user) > 500:
        raise HTTPException(status_code=400, detail="The request is too long.")

    try:
        response = ChatResponse(
            assistant=ai_client.invoke("Lance", request.user)
        )  # TODO: add functionality to manage several conversation_id
    except OpenAIClientError:
        raise HTTPException(
            status_code=500,
            detail="The chatbot service is currently unavailable. Please try again later.",
        )

    return response
