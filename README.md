# FastAPI Endpoints

[![CI checks](https://github.com/vladNed/fastapi-endpoints/actions/workflows/ci.yaml/badge.svg?branch=main&event=push)](https://github.com/vladNed/fastapi-endpoints/actions/workflows/ci.yaml)

This is a file-based router for FastAPI that automatically discovers and registers route files based on their filenames.
This tool simplifies the organization and scaling of your FastAPI projects by allowing you to structure your endpoints in a modular way.
With `fastapi-endpoints`, you can easily manage complex applications by keeping your routes clean, intuitive, and maintainable.
This project is inspired from [SettleAPI/settle-fastapi-extensions](https://github.com/SettleAPI/settle-fastapi-extensions)

Please refer to the documentation here:

- **[Documentation](https://vladned.github.io/fastapi-endpoints/)**

## Installation

```bash
pip install fastapi-endpoints
```

## Usage

### Auto discovery

The auto discovery feature allows you to organize your routes in separate files and directories and will be automatically registered by the router.
All routers should be under the `routers` directory within your FastAPI application.

```python
# src/app.py

from fastapi import FastAPI
from fastapi_endpoints import auto_include_routers

from . import routers

app = FastAPI()
auto_include_routers(app, routers)
```

```python
# src/routers/users.py
from fastapi import APIRouter

users_router = APIRouter()

# Define your routes here
```

The routes under `src/routers/users.py` will be automatically registered by the router. The prefix to the routes will be the path to the file relative to the `routers` directory.
For the example above, the routes will be available under `/users`.

The auto discovery feature also supports nested directories. For example, if you have the following directory structure:

```
routers
|── __init__.py
├── api_v1
│   ├── __init__.py
│   ├── users.py
│   └── posts.py
└── api_v2
    ├── __init__.py
    ├── users.py
    └── posts.py
app.py
```

The routes under `src/routers/api_v1/users.py` will be available under `/api/v1/users`.
The same applies to the other files. The routes under `src/routers/api_v2/users.py` will be available under `/api/v2/users`.

### Exclude Routers

You can exclude routers from being registered by the router by defining the `EXCLUDED_ROUTERS` variable in the `__init__.py` file of any submodule of the `routers` module. All excluded routers will be bundled together and excluded from the registration process.

For example, if you have the following directory structure:
```
routers
|── __init__.py
├── api_v1
│   ├── __init__.py
│   ├── users.py
│   └── posts.py
app.py
```

You can exclude the `users.py` router from being registered by defining the `EXCLUDED_ROUTERS` variable in the `api_v1/__init__.py` file.

```python
# src/routers/api_v1/__init__.py
from . import users

EXCLUDED_ROUTERS = [users]
```

You can also exclude an entire directory by defining the `EXCLUDED_ROUTERS` variable in the `__init__.py` file of the directory.

```python
# src/routers/__init__.py
from . import api_v1

EXCLUDED_ROUTERS = [api_v1]
```


## Development

You are required to have [Poetry](https://python-poetry.org/) installed in your system to manage the dependencies.

### Setup

```bash
poetry install
```

### Running tests

```bash
pytest
```

### Linting & Formatting

To check the format:
```bash
ruff format --check src/
```

To check the lint:
```bash
ruff check src/
```

After running both commands, the format errors can be applied by running the formatter without the `--check` flag.


