from mcp_tool.tool import ExampleTool


class Agent:
    """Agent that uses an example tool to generate responses."""

    def __init__(self, tool: ExampleTool | None = None) -> None:
        self.tool = tool or ExampleTool()

    def chat(self, prompt: str) -> str:
        return self.tool.run(prompt)
