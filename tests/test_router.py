from unittest import mock

import pytest

from fastapi_endpoints import auto_include_routers, exceptions


def test_auto_include_routers_incorrect_module(mock_incorrect_routers_module, mock_application):
    with pytest.raises(exceptions.InitializationError):
        auto_include_routers(mock_application, mock_incorrect_routers_module)


def test_auto_include_routers(mock_routers_module, mock_application, mock_router_one, mock_router_two):
    calls = [
        mock.call(mock_router_one.router, prefix="/api/one"),
        mock.call(mock_router_two.router, prefix="/api/two"),
    ]
    with mock.patch(
        "pkgutil.walk_packages",
        return_value=[
            (None, mock_routers_module.__name__, True),
            (None, mock_router_one.__name__, False),
            (None, mock_router_two.__name__, False),
        ],
    ):
        with mock.patch(
            "importlib.import_module",
            side_effect=[
                mock_routers_module,
                mock_router_one,
                mock_routers_module,
                mock_router_two,
                mock_routers_module,
            ],
        ) as mock_import:
            auto_include_routers(mock_application, mock_routers_module)
            assert mock_import.call_count == 5
            assert mock_application.include_router.call_count == 2
            mock_application.include_router.assert_has_calls(calls)


def test_auto_include_router_module_with_no_router(
    mock_routers_module,
    mock_application,
    mock_module_without_router,
):
    with mock.patch(
        "pkgutil.walk_packages",
        return_value=[
            (None, mock_routers_module.__name__, True),
            (None, mock_module_without_router.__name__, False),
        ],
    ):
        with mock.patch(
            "importlib.import_module",
            side_effect=[mock_routers_module, mock_module_without_router, mock_routers_module],
        ):
            with pytest.raises(exceptions.RouterNotFound):
                auto_include_routers(mock_application, mock_routers_module)
