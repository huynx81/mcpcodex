import requests


def request_generation(prompt: str, host: str = "http://localhost:8000") -> str:
    """Send a prompt to the MCP server and return the response."""
    resp = requests.post(f"{host}/generate", json={"prompt": prompt}, timeout=60)
    resp.raise_for_status()
    return resp.json()["response"]


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="MCP client")
    parser.add_argument("prompt", nargs="*", help="Prompt to send to the server")
    parser.add_argument("--host", default="http://localhost:8000", help="Server URL")
    args = parser.parse_args()

    prompt = " ".join(args.prompt) or "Hello, world!"
    print(request_generation(prompt, host=args.host))


if __name__ == "__main__":
    main()
