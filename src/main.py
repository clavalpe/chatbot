from fastapi import FastAPI
import logging
from src.api import health


loggingLevel = logging.INFO
logging.basicConfig(level=loggingLevel, format="%(asctime)s:%(levelname)s:%(message)s")


app = FastAPI(
    title="Chatbot API",
    description="This service permits to interact with a chatbot.",
    version="0.1.0",
    docs_url="/swagger",
)

app.include_router(health.router)
