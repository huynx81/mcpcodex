from __future__ import annotations

from typing import Literal

import requests

from common.ollama_client import OllamaClient


class TTSTool:
    """Tool for converting text to speech audio bytes."""

    def __init__(
        self,
        backend: Literal["api", "ollama"] = "api",
        api_url: str | None = None,
        model: str = "tts",
        host: str = "http://localhost:11434",
    ) -> None:
        self.backend = backend
        self.api_url = api_url or "https://api.example.com/tts"
        self.client: OllamaClient | None = None
        if backend == "ollama":
            self.client = OllamaClient(model=model, host=host)

    def run(self, text: str) -> bytes:
        """Generate speech audio from the provided text."""
        if self.backend == "ollama":
            if self.client is None:
                raise RuntimeError("Ollama backend is not configured")
            return self.client.tts(text)
        resp = requests.post(self.api_url, json={"text": text}, timeout=60)
        resp.raise_for_status()
        return resp.content
