import os
from typing import Any

import httpx
from dotenv import load_dotenv

load_dotenv()

DEFAULT_MONARCH_API_URL = "https://api.monarchinitiative.org/v3/api/"
DEFAULT_MONARCH_TIMEOUT_SECONDS = 30.0


class MonarchClient:
    def __init__(self):
        configured_base_url = os.getenv("MONARCH_API_URL", DEFAULT_MONARCH_API_URL).strip()
        if not configured_base_url:
            configured_base_url = DEFAULT_MONARCH_API_URL
        if not configured_base_url.startswith(("http://", "https://")):
            raise ValueError(
                "MONARCH_API_URL must start with http:// or https:// "
                f"(received: {configured_base_url!r})"
            )

        self.base_url = configured_base_url.rstrip("/") + "/"
        self.client = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=httpx.Timeout(DEFAULT_MONARCH_TIMEOUT_SECONDS),
        )

    async def get(self, endpoint: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        try:
            response = await self.client.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as exc:
            raise RuntimeError(
                f"Monarch API HTTP error ({exc.response.status_code}) for {exc.request.url}: "
                f"{exc.response.text}"
            ) from exc
        except httpx.RequestError as exc:
            raise RuntimeError(f"Monarch API request error for {exc.request.url}: {exc}") from exc

    async def post(self, endpoint: str, data: dict[str, Any] | None = None) -> dict[str, Any]:
        try:
            response = await self.client.post(endpoint, json=data)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as exc:
            raise RuntimeError(
                f"Monarch API HTTP error ({exc.response.status_code}) for {exc.request.url}: "
                f"{exc.response.text}"
            ) from exc
        except httpx.RequestError as exc:
            raise RuntimeError(f"Monarch API request error for {exc.request.url}: {exc}") from exc

    async def close(self):
        await self.client.aclose()
