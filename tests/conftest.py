from typing import Generator
import pytest

from unittest import mock
from fastapi_endpoints import router


FAKE_APP_PATH_MODULE = "/fake/path/to"
FAKE_APP_PATH_FILE = f"{FAKE_APP_PATH_MODULE}/app.py"


@pytest.fixture()
def mock_routers_path_exist() -> Generator[None, None, None]:
    with (
        mock.patch.object(router, '_get_caller_frame', return_value=FAKE_APP_PATH_FILE),
        mock.patch.object(router.pathlib.Path, 'exists', return_value=True)
    ):
        yield


@pytest.fixture()
def mock_routers_path_not_exist() -> Generator[None, None, None]:
    with (
        mock.patch.object(router, '_get_caller_frame', return_value=FAKE_APP_PATH_FILE),
        mock.patch.object(router.pathlib.Path, 'exists', return_value=False)
    ):
        yield


@pytest.fixture()
def mock_initialization_error() -> Generator[None, None, None]:
    with mock.patch.object(router, '_get_caller_frame', side_effect=router.exceptions.InitializationError):
        yield
