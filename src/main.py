from fastapi import FastAPI
import logging
from src.api import health, chat
import os
from dotenv import load_dotenv


class OpenAIAPIKeyNotFound(Exception): ...


loggingLevel = logging.INFO
logging.basicConfig(level=loggingLevel, format="%(asctime)s:%(levelname)s:%(message)s")


app = FastAPI(
    title="Chatbot API",
    description="This service permits to interact with a chatbot.",
    version="0.1.0",
    docs_url="/swagger",
)

app.include_router(health.router)
app.include_router(chat.router)

load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
    raise OpenAIAPIKeyNotFound("OpenAI API Key not found in environment variables.")
