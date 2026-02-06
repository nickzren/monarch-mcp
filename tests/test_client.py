import pytest

from monarch_mcp.client import DEFAULT_MONARCH_API_URL, MonarchClient
from monarch_mcp.client import DEFAULT_MONARCH_TIMEOUT_SECONDS


@pytest.mark.asyncio
async def test_monarch_client_uses_default_base_url_when_env_missing(monkeypatch):
    monkeypatch.delenv("MONARCH_API_URL", raising=False)

    client = MonarchClient()
    try:
        assert client.base_url == DEFAULT_MONARCH_API_URL
    finally:
        await client.close()


@pytest.mark.asyncio
async def test_monarch_client_uses_default_base_url_when_env_blank(monkeypatch):
    monkeypatch.setenv("MONARCH_API_URL", "   ")

    client = MonarchClient()
    try:
        assert client.base_url == DEFAULT_MONARCH_API_URL
    finally:
        await client.close()


@pytest.mark.asyncio
async def test_monarch_client_normalizes_trailing_slash(monkeypatch):
    monkeypatch.setenv("MONARCH_API_URL", "https://api.monarchinitiative.org/v3/api")

    client = MonarchClient()
    try:
        assert client.base_url.endswith("/")
    finally:
        await client.close()


def test_monarch_client_rejects_base_url_without_scheme(monkeypatch):
    monkeypatch.setenv("MONARCH_API_URL", "api.monarchinitiative.org/v3/api")

    with pytest.raises(ValueError, match="MONARCH_API_URL must start with http:// or https://"):
        MonarchClient()


@pytest.mark.asyncio
async def test_monarch_client_sets_default_timeout(monkeypatch):
    monkeypatch.delenv("MONARCH_API_URL", raising=False)

    client = MonarchClient()
    try:
        assert client.client.timeout.connect == DEFAULT_MONARCH_TIMEOUT_SECONDS
        assert client.client.timeout.read == DEFAULT_MONARCH_TIMEOUT_SECONDS
        assert client.client.timeout.write == DEFAULT_MONARCH_TIMEOUT_SECONDS
        assert client.client.timeout.pool == DEFAULT_MONARCH_TIMEOUT_SECONDS
    finally:
        await client.close()
