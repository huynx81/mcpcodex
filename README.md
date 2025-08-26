# mcpcodex

Template for developing Model Context Protocol components with a local [Ollama](https://ollama.com) model.

## Components

- **MCP Server** (`mcp_server`) – FastAPI server exposing a `/generate` endpoint that streams prompts to a local Ollama model.
- **Tool** (`mcp_tool`) – Thin wrapper around the Ollama client for use by agents.
- **Agent** (`mcp_agent`) – Example agent that uses the tool to chat.
- **Client** (`mcp_client`) – Command line utility to send prompts to the server.

## Requirements

- Python 3.12+
- A running [Ollama](https://ollama.com) instance on `localhost:11434`

Install dependencies and run the server:

```bash
pip install -e .
uvicorn mcp_server.server:app --reload
```

Use the client:

```bash
python -m mcp_client.client "Hello"
```

## Releasing

Tag the repository with `vX.Y.Z` and push to GitHub to trigger the release workflow.
