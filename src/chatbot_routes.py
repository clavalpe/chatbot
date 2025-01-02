from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "healthy"}