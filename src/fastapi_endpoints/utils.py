# fastapi-endpoints
# Copyright (c) 2024 Vlad Nedelcu
# Licensed under the MIT License

from types import ModuleType
from typing import Optional

import fastapi

from . import constants, exceptions


def format_prefix(route_path: str) -> str:
    return route_path.replace("_", "/").replace(".", "/")


def get_module_router(module: ModuleType) -> Optional[fastapi.APIRouter]:
    for attr in dir(module):
        attr_value = getattr(module, attr)
        if isinstance(attr_value, fastapi.APIRouter):
            return attr_value

    return None


def extract_route_path(module_name: str) -> str:
    try:
        _, endpoint_path = module_name.split(constants.DEFAULT_ENDPOINTS_ROOT)
    except ValueError:
        raise exceptions.InitializationError()

    return endpoint_path
