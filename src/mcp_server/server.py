from fastapi import FastAPI
from pydantic import BaseModel

from common.ollama_client import OllamaClient

app = FastAPI(title="MCP Server")
client = OllamaClient()


class Query(BaseModel):
    prompt: str


@app.post("/generate")
def generate(query: Query) -> dict[str, str]:
    """Generate text using the local model."""
    return {"response": client.generate(query.prompt)}
