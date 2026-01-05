import importlib.util
import inspect
import pathlib
import sys
import types
import typing

import fastapi

import fastapi_endpoints
import fastapi_endpoints.constants
import fastapi_endpoints.exceptions


class FastAPIApp(fastapi.FastAPI):
    """The wrapper class for `FastAPI` that will auto include routers module

    All the routers defined under the routers module will be included and
    prefixed automatically by the `auto_include_routers` function.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        project_root = pathlib.Path(__file__).resolve().parent
        root = self._caller_root(project_root)
        candidate_routers_path = root / fastapi_endpoints.constants.DEFAULT_ENDPOINTS_ROOT
        routers_path_init = candidate_routers_path / "__init__.py"

        if not candidate_routers_path.is_dir() and not routers_path_init.exists():
            raise fastapi_endpoints.exceptions.InitializationError

        routers_module = self._import_routers_module(routers_path_init)
        fastapi_endpoints.auto_include_routers(self, routers_module)

    @staticmethod
    def _caller_root(lib_dir: pathlib.Path) -> typing.Optional[pathlib.Path]:
        """Return the directory of the first frame whose file is *not* inside
        the library directory. If no such frame exists, return ``None``.
        """
        for frame_info in inspect.stack()[1:]:
            caller_file = pathlib.Path(frame_info.filename).resolve()
            if not caller_file.is_relative_to(lib_dir):
                return caller_file.parent

        return None

    @staticmethod
    def _import_routers_module(module_init_path: pathlib.Path) -> typing.Optional[types.ModuleType]:
        """Loads the default endpoints root module into modules"""
        spec = importlib.util.spec_from_file_location(
            name=fastapi_endpoints.constants.DEFAULT_ENDPOINTS_ROOT,
            location=module_init_path.resolve(),
        )
        if spec is None:
            return None

        module = importlib.util.module_from_spec(spec)
        sys.modules[fastapi_endpoints.constants.DEFAULT_ENDPOINTS_ROOT] = module
        spec.loader.exec_module(module)

        return module
