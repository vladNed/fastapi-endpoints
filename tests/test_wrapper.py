import inspect
import pathlib
from unittest import mock

import fastapi
import pytest
from data.wrapper_app import app

import fastapi_endpoints
import fastapi_endpoints.exceptions


def test_wrapper_include_root_file_endpoints():
    tables_routes = []
    for route in app.routes:
        if not isinstance(route, fastapi.routing.APIRoute):
            continue
        if route.path.startswith("/api/v1/tables"):
            tables_routes.append(route.path)

    assert tables_routes == [
        "/api/v1/tables/docs/",
        "/api/v1/tables/docs/create",
        "/api/v1/tables/",
        "/api/v1/tables/create",
    ]


def test_wrapper_no_routers_module():
    with pytest.raises(fastapi_endpoints.exceptions.InitializationError):
        import bad_data.app


def test_caller_root_returns_none_when_no_external_frame():
    lib_dir = pathlib.Path("/fake/lib_dir")

    fake_frame = mock.Mock()
    fake_frame.filename = str(lib_dir / "module_a.py")
    fake_stack = [fake_frame, fake_frame]

    with mock.patch.object(inspect, "stack", return_value=fake_stack):
        result = fastapi_endpoints.FastAPIApp._caller_root(lib_dir)

    assert result is None


def test_import_routers_module_specs_is_none():
    test_path = pathlib.Path(__file__).parent

    result = fastapi_endpoints.FastAPIApp._import_routers_module(test_path)
    assert result is None
