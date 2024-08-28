import inspect
import pathlib

import fastapi

from . import constants, exceptions


def _get_caller_frame() -> str:
    """Get the caller frame to extract the caller module.

    :raises InitializationError: If the caller frame is not found.
    :returns str: The caller frame.
    """
    caller_frame = inspect.stack()[3]
    caller_module = inspect.getmodule(caller_frame[0])
    if caller_module is None:
        raise exceptions.InitializationError()

    caller_file_path = caller_module.__file__
    if not caller_file_path:
        raise exceptions.InitializationError()

    return caller_file_path


def _get_router_dir() -> pathlib.Path:
    """Get the path to the router endpoint directory.

    :raises RouterDirNotFound: If the directory is not found.
    :raises InitializationError: If the caller frame is not found.

    :returns pathlib.Path: The path to the router endpoint directory.
    """
    caller_file_path = _get_caller_frame()
    router_dir = pathlib.Path(caller_file_path).parent / constants.DEFAULT_ENDPOINTS_ROOT
    if not router_dir.exists():
        raise exceptions.RouterDirNotFound()

    return router_dir


def include_routers(application: fastapi.FastAPI) -> None:
    """Include all routers in the router directory.

    :param application fastapi.FastAPI: The FastAPI application.
    """
    _get_router_dir()
    print("Works")
