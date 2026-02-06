import sys
from unittest.mock import AsyncMock

import pytest
from starlette.testclient import TestClient

import monarch_mcp.server as server


class _FakeMonarchClient:
    def __init__(self):
        self.closed = False

    async def close(self):
        self.closed = True


def test_get_client_raises_when_not_initialized(monkeypatch):
    monkeypatch.setattr(server, "_client", None)

    with pytest.raises(RuntimeError, match="MonarchClient not initialised"):
        server.get_client()


@pytest.mark.asyncio
async def test_lifespan_initializes_and_closes_client(monkeypatch):
    created_clients: list[_FakeMonarchClient] = []

    class TrackingClient(_FakeMonarchClient):
        def __init__(self):
            super().__init__()
            created_clients.append(self)

    monkeypatch.setattr(server, "MonarchClient", TrackingClient)
    monkeypatch.setattr(server, "_client", None)

    async with server.lifespan(server.mcp):
        client = server.get_client()
        assert isinstance(client, TrackingClient)
        assert not client.closed

    assert created_clients
    assert created_clients[0].closed
    assert server._client is None


def test_discovery_document_and_health_routes(monkeypatch):
    monkeypatch.setattr(server, "MonarchClient", _FakeMonarchClient)

    with TestClient(server.mcp.http_app()) as client:
        discovery = client.get("/.well-known/mcp.json")
        assert discovery.status_code == 200
        payload = discovery.json()

        assert payload["protocolVersion"] == server.mcp_types.LATEST_PROTOCOL_VERSION
        assert payload["server"]["name"] == server.mcp.name
        assert payload["server"]["version"] == server.mcp.version
        assert payload["transports"]["http"]["url"].endswith(server.fastmcp_settings.streamable_http_path)
        assert payload["transports"]["sse"]["url"].endswith(server.fastmcp_settings.sse_path)
        assert payload["transports"]["sse"]["messageUrl"].endswith(server.fastmcp_settings.message_path)
        assert payload["capabilities"]["tools"]["listChanged"] is False

        health = client.get("/")
        assert health.status_code == 200
        assert health.json() == {"status": "ok"}


def test_sse_message_fallback_route(monkeypatch):
    monkeypatch.setattr(server, "MonarchClient", _FakeMonarchClient)

    with TestClient(server.mcp.http_app()) as client:
        response = client.post(server.fastmcp_settings.sse_path)
        assert response.status_code == 204


def test_main_stdio_uses_stdio_runner(monkeypatch):
    run_stdio_async = AsyncMock()
    run_http_async = AsyncMock()
    monkeypatch.setattr(server.mcp, "run_stdio_async", run_stdio_async)
    monkeypatch.setattr(server.mcp, "run_http_async", run_http_async)
    monkeypatch.setattr(sys, "argv", ["monarch-mcp", "--transport", "stdio"])

    server.main()

    run_stdio_async.assert_awaited_once_with()
    run_http_async.assert_not_called()


@pytest.mark.parametrize("transport", ["http", "sse"])
def test_main_http_transports_use_http_runner(monkeypatch, transport):
    run_stdio_async = AsyncMock()
    run_http_async = AsyncMock()
    monkeypatch.setattr(server.mcp, "run_stdio_async", run_stdio_async)
    monkeypatch.setattr(server.mcp, "run_http_async", run_http_async)
    monkeypatch.setattr(
        sys,
        "argv",
        ["monarch-mcp", "--transport", transport, "--host", "127.0.0.1", "--port", "9191"],
    )

    server.main()

    run_stdio_async.assert_not_called()
    run_http_async.assert_awaited_once_with(
        transport=transport,
        host="127.0.0.1",
        port=9191,
    )
