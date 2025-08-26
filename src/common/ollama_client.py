import json
from typing import Any, Dict

import requests


class OllamaClient:
    """Minimal client for a local Ollama server."""

    def __init__(self, model: str = "llama2", host: str = "http://localhost:11434") -> None:
        self.model = model
        self.host = host.rstrip("/")

    def generate(self, prompt: str, **params: Any) -> str:
        """Generate a completion from the local model."""
        payload: Dict[str, Any] = {"model": self.model, "prompt": prompt}
        payload.update(params)
        response = requests.post(f"{self.host}/api/generate", json=payload, timeout=60)
        response.raise_for_status()
        text = ""
        for line in response.iter_lines():
            if line:
                data = json.loads(line)
                text += data.get("response", "")
        return text
