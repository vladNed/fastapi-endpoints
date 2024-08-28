# fastapi-endpoints
# Copyright (c) 2024 Vlad Nedelcu
# Licensed under the MIT License

import importlib
import pkgutil

from typing import Set
from types import ModuleType

import fastapi

from . import exceptions, utils


Excluded = Set[ModuleType]


def _handle_package_module(module: ModuleType, excluded_routers: Excluded) -> None:
    """Handles the packages modules.

    It scans the `__init__.py` file of the package and fetches the excluded
    routers.

    If the module is in the excluded routers, it will not be included in the
    application. This means that the excluded routers will also not be included.
    """
    if module in excluded_routers:
        return

    excluded_routers.update(utils.fetch_excluded_routers(module))


def _handle_non_package_module(module: ModuleType, excluded_routers: Excluded, application: fastapi.FastAPI) -> None:
    """Handles the non-package modules and files.

    The function scans the module for an `fastapi.APIRouter` instance. If it
    finds one, it includes it in the application.

    If the module is in the excluded routers, it will not be included in the
    application.

    :raises RouterNotFound: If the module does not contain an `APIRouter`
    :raises InitializationError: If the module is not defined correctly within
    the `routers` module.
    """
    package = importlib.import_module(module.__package__)  # type: ignore
    if module in excluded_routers or package in excluded_routers:
        return

    route_path = utils.extract_route_path(module.__name__)
    route_prefix = utils.format_prefix(route_path)
    module_router = utils.get_module_router(module)
    if module_router is None:
        raise exceptions.RouterNotFound()

    application.include_router(module_router, prefix=route_prefix)


def _process_module(module: ModuleType, is_pkg: bool, excluded_routers: Excluded, application: fastapi.FastAPI) -> None:
    """Processes the module based on its type.

    If the module is a package, it will call the `_handle_package_module`
    function. Otherwise, it will call the `_handle_non_package_module` function.

    :raises InitializationError: If the module is not defined correctly within
    :raises RouterNotFound: If the module does not contain an `APIRouter`
    """
    if is_pkg:
        _handle_package_module(module, excluded_routers)
    else:
        _handle_non_package_module(module, excluded_routers, application)


def auto_include_routers(application: fastapi.FastAPI, router_module: ModuleType) -> None:
    """Include all routers in the router module."""

    excluded_routers = utils.fetch_excluded_routers(router_module)
    packages = list(pkgutil.walk_packages(router_module.__path__, router_module.__name__ + "."))
    if len(packages) == 0:
        raise exceptions.InitializationError()

    for _, module_name, is_pkg in packages:
        module = importlib.import_module(module_name)
        _process_module(module, is_pkg, excluded_routers, application)
