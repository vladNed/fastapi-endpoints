import pytest
import pathlib

from unittest.mock import MagicMock, patch

from fastapi_endpoints.router import _get_router_dir, exceptions, constants, _get_caller_frame


def test_get_caller_frame_success():
    mock_frame = MagicMock()
    mock_module = MagicMock()
    mock_module.__file__ = '/fake/path/to/caller.py'
    with patch('inspect.stack', return_value=[None, None, None, mock_frame]), \
         patch('inspect.getmodule', return_value=mock_module):
        caller_frame = _get_caller_frame()
        assert caller_frame == '/fake/path/to/caller.py'


def test_get_caller_frame_module_none():
    mock_frame = MagicMock()
    with patch('inspect.stack', return_value=[None, None, None, mock_frame]), \
         patch('inspect.getmodule', return_value=None):
        with pytest.raises(exceptions.InitializationError):
            _get_caller_frame()


def test_get_caller_frame_file_none():
    mock_frame = MagicMock()
    mock_module = MagicMock()
    mock_module.__file__ = None
    with patch('inspect.stack', return_value=[None, None, None, mock_frame]), \
         patch('inspect.getmodule', return_value=mock_module):
        with pytest.raises(exceptions.InitializationError):
            _get_caller_frame()


def test_get_router_dir_exists(mock_routers_path_exist):
    router_dir = _get_router_dir()
    assert router_dir == (pathlib.Path('/fake/path/to') / constants.DEFAULT_ENDPOINTS_ROOT)


def test_get_router_dir_not_exists(mock_routers_path_not_exist):
    with pytest.raises(exceptions.RouterDirNotFound):
        _get_router_dir()


def test_get_caller_frame_initialization_error(mock_initialization_error):
    with pytest.raises(exceptions.InitializationError):
        _get_router_dir()
