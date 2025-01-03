from fastapi import FastAPI
from typing import Dict
from pydantic import BaseModel

app = FastAPI()

@app.get("/health")
async def health_check() -> Dict[str, str]:
    return {"status": "healthy"}