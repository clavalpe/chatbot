from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import logging

from src.api.lang_chain_client import (
    LangChainClient,
    OpenAIClientError,
    SendMessage,
    InMemoryConversationRepository,
)

router = APIRouter()

ai_client = LangChainClient()

conversation_repository = InMemoryConversationRepository()

USER = "Lance"


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
        logging.warning("Received empty 'user' field in the request.")
        raise HTTPException(status_code=400, detail="The request cannot be empty.")

    if len(request.user) > 500:
        logging.warning(f"Received a request that exceeds length limit: {len(request.user)} characters")
        raise HTTPException(status_code=400, detail="The request is too long.")

    try:
        logging.info("Sending message to the chatbot for user '%s'.", USER)
        response = ChatResponse(
            assistant=SendMessage(
                conversation_repository=conversation_repository
            ).execute(USER, request.user)
        )
    except OpenAIClientError:
        logging.error("Error occurred while interacting with the chatbot.")
        raise HTTPException(
            status_code=500,
            detail="The chatbot service is currently unavailable. Please try again later.",
        )

    return response
