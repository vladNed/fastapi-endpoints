# fastapi-endpoints
# Copyright (c) 2024 Vlad Nedelcu
# Licensed under the MIT License

from types import ModuleType
from typing import Optional, Set

import fastapi

import fastapi_endpoints.constants
import fastapi_endpoints.exceptions


def format_prefix(route_path: str) -> str:
    formatted_path = route_path.replace("_", "/").replace(".", "/")
    return "/" + formatted_path


def get_module_router(module: ModuleType) -> Optional[fastapi.APIRouter]:
    for attr in dir(module):
        attr_value = getattr(module, attr)
        if isinstance(attr_value, fastapi.APIRouter):
            return attr_value

    return None


def extract_route_path(module_name: str) -> str:
    root = fastapi_endpoints.constants.DEFAULT_ENDPOINTS_ROOT
    parts = module_name.split(".")

    try:
        root_index = parts.index(root)
    except ValueError:
        raise fastapi_endpoints.exceptions.InitializationError()

    endpoint_parts = parts[root_index + 1 :]

    if endpoint_parts and endpoint_parts[-1] == "root":
        endpoint_parts.pop()

    return ".".join(endpoint_parts)


def fetch_excluded_routers(router_module: ModuleType) -> Set[ModuleType]:
    excluded_routers = set()
    if hasattr(router_module, fastapi_endpoints.constants.DEFAULT_EXCLUDED_ROUTERS):
        excluded_routers.update(getattr(router_module, fastapi_endpoints.constants.DEFAULT_EXCLUDED_ROUTERS))

    return excluded_routers
