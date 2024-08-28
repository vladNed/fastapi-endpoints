# fastapi-endpoints
# Copyright (c) 2024 Vlad Nedelcu
# Licensed under the MIT License

import pkgutil
import importlib
from types import ModuleType
import fastapi

from . import exceptions, utils


def auto_include_routers(application: fastapi.FastAPI, router_module: ModuleType) -> None:
    """Include all routers in the router module."""
    packages = pkgutil.walk_packages(router_module.__path__, router_module.__name__ + ".")
    if len(list(packages)) == 0:
        raise exceptions.InitializationError()

    for _, module_name, is_pkg in packages:
        module = importlib.import_module(module_name)
        if is_pkg:
            continue

        route_path = utils.extract_route_path(module_name)
        route_prefix = utils.format_prefix(route_path)
        module_router = utils.get_module_router(module)
        if module_router is None:
            raise exceptions.RouterNotFound()

        application.include_router(
            module_router,
            prefix=route_prefix
        )
