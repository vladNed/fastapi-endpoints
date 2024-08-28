from types import ModuleType
from unittest import mock

import fastapi
import pytest

from fastapi_endpoints import constants, exceptions, utils

FORMAT_TEST_CASES = {
    "UNDERSCORE_REPLACE": ("foo_bar", "foo/bar"),
    "MODULE_TO_PATH_REPLACE": ("foo.bar", "foo/bar"),
    "UNDERSCORE_AND_MODULE_REPLACE": ("foo_bar.baz.qux", "foo/bar/baz/qux"),
}


@pytest.mark.parametrize("input, expected", FORMAT_TEST_CASES.values(), ids=FORMAT_TEST_CASES.keys())
def test_format_prefix(input: str, expected: str):
    assert utils.format_prefix(input) == expected


def test_get_module_router():
    mock_router = fastapi.APIRouter()
    mock_module = mock.Mock(spec=ModuleType)
    mock_module.router = mock_router

    assert utils.get_module_router(mock_module) == mock_router


def test_get_module_router_no_router():
    mock_module = mock.Mock(spec=ModuleType)

    assert utils.get_module_router(mock_module) is None


def test_extract_route_path():
    module_name = f"some_module.{constants.DEFAULT_ENDPOINTS_ROOT}.endpoint"
    assert utils.extract_route_path(module_name) == ".endpoint"

    with pytest.raises(exceptions.InitializationError):
        utils.extract_route_path("invalid_module_name")


def test_get_excluded_routers_no_routers(mock_router_one):
    assert utils.fetch_excluded_routers(mock_router_one) == set()


def test_get_excluded_routers(mock_excluded_routers_router):
    assert utils.fetch_excluded_routers(mock_excluded_routers_router) == {"test_app.routers.api.one"}
