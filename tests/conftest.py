# tests/conftest.py
from types import SimpleNamespace

import pytest
from unittest.mock import AsyncMock

@pytest.fixture
def mock_client() -> SimpleNamespace:
    return SimpleNamespace(
        get=AsyncMock(),
        post=AsyncMock(),
    )
