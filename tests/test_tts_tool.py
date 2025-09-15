from unittest.mock import Mock, patch

from mcp_tool.tts_tool import TTSTool


def _fake_response(content: bytes) -> Mock:
    resp = Mock()
    resp.content = content
    resp.raise_for_status = Mock()
    return resp


def test_api_backend() -> None:
    tool = TTSTool(backend="api", api_url="http://example.com/tts")
    with patch("mcp_tool.tts_tool.requests.post", return_value=_fake_response(b"api")) as post:
        audio = tool.run("Hello")
    assert audio == b"api"
    post.assert_called_once()


def test_ollama_backend() -> None:
    tool = TTSTool(backend="ollama", model="voice")
    with patch(
        "common.ollama_client.requests.post", return_value=_fake_response(b"ollama")
    ) as post:
        audio = tool.run("Hi")
    assert audio == b"ollama"
    post.assert_called_once()
    assert post.call_args[0][0].endswith("/api/tts")
