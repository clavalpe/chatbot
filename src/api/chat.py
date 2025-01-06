from fastapi import APIRouter
from pydantic import BaseModel, Field
import logging

from src.api.chat_open_ai_client import ChatOpenAIClient

router = APIRouter()

ai_client = ChatOpenAIClient()
compiled_workflow = ai_client.build_workflow()


class ChatRequest(BaseModel):
    user: str = Field(..., json_schema_extra={'example': "Can you help me?"})


class ChatResponse(BaseModel):
    assistant: str


@router.post("/chat", response_model=ChatResponse, tags=["Chat"])
async def chat(request: ChatRequest) -> ChatResponse:
    """
    Allows interaction with a chatbot.
    """
    logging.info("Chat endpoint was accessed.")
    response = ChatResponse(assistant=ai_client.invoke(compiled_workflow, request.user))
    return response
