from common.ollama_client import OllamaClient


class ExampleTool:
    """Simple tool that forwards prompts to the local model."""

    def __init__(self, model: str = "llama2") -> None:
        self.client = OllamaClient(model=model)

    def run(self, prompt: str) -> str:
        return self.client.generate(prompt)
