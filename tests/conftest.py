from types import ModuleType
from unittest import mock

import fastapi
import pytest


@pytest.fixture
def mock_application() -> mock.Mock:
    return mock.Mock(spec=fastapi.FastAPI())


@pytest.fixture
def mock_router_one():
    mock_router1_module = mock.Mock(spec=ModuleType)
    mock_router1_module.router = mock.Mock(spec=fastapi.APIRouter)
    mock_router1_module.__name__ = "test_app.routers.api.one"

    return mock_router1_module


@pytest.fixture
def mock_router_two():
    mock_router2_module = mock.Mock(spec=ModuleType)
    mock_router2_module.router = mock.Mock(spec=fastapi.APIRouter)
    mock_router2_module.__name__ = "test_app.routers.api.two"

    return mock_router2_module


@pytest.fixture
def mock_routers_module():
    test_routers_module = mock.Mock(spec=ModuleType)
    test_routers_module.__path__ = ["test_app"]
    test_routers_module.__name__ = "test_app"

    return test_routers_module


@pytest.fixture
def mock_module_without_router():
    test_routers_module = mock.Mock(spec=ModuleType)
    test_routers_module.__name__ = "test_app.routers.api.three"

    return test_routers_module


@pytest.fixture
def mock_incorrect_routers_module():
    test_routers_module = mock.Mock(spec=ModuleType)
    test_routers_module.__path__ = ["test_app"]
    test_routers_module.__name__ = "test_app"

    with mock.patch("pkgutil.walk_packages", return_value=[]):
        return test_routers_module
