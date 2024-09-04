<p align="center">
    <img class="logo" width="100" height="105" src="assets/logo-black.png">
</p>

<h1 align="center">fastapi-endpoints</h1>
<p align="center" >Effortless routing, simplified</p>

---

fastapi-endpoints is a lightweight and simple file-based router for FastAPI framework.

The key features are:

* **Simple**: Organize and define routes directly through a clear and simple file structure.
* **Auto Discovery**: Automatically detects and registers all defined routers, reducing manual setup.
* **Effortless Integration**: Seamlessly integrates with existing FastAPI projects, with minimal configuration required.
* **Selective Routing**: Include or exclude specific routers by specifying Python modules, giving full control over active routes.

---

## Requirements

fastapi-endpoints behaves as a plugin for:

* <a href="https://fastapi.tiangolo.com">FastAPI</a> Framework

---

## Installation

Create and activate a virtual environment. Some options are:

* **[venv](https://docs.python.org/3/library/venv.html)**
* **[pyenv](https://github.com/pyenv/pyenv)**, which has a modern approach

### Using `pip`

```bash
pip install fastapi-endpoints
```

### Using `poetry`

```bash
poetry add fastapi-endpoints
```

---

## Examples

### Basic usage

The project structure should contain the directory `routers/`, for example this:

```bash hl_lines="1"
routers
|── __init__.py
├── api_v1
│   ├── __init__.py
│   ├── users.py
│   └── posts.py
└── dev
    ├── __init__.py
    └── probes.py
app.py
```

The `app.py` should contain the following code:

```py title="app.py"
from fastapi import FastAPI
from fastapi_endpoints import auto_include_routers

from . import routers

app = FastAPI()

auto_include_routers(app, routers)
```

And for the routers, define it as this:

```py title="routers/api_v1/users.py"
from fastapi import APIRouter

users_router = APIRouter()

@users_router.get("/")
async def get_users():
    ...
```

For the example above, the `get_users` endpoint will be located at path `http://localhost/api/v1/users/`.

All the other routes will be automatically disovered, and they will be included with a prefix following
the file structure.

### Exclude routers

In this example, the `routers/dev/posts.py` router will be excluded.

``` hl_lines="7 8 9"
routers
|── __init__.py
├── api_v1
│   ├── __init__.py
│   ├── users.py
│   └── posts.py
└── dev
    ├── __init__.py
    └── posts.py
app.py
```

Excluding routers is entirely done by specifying which module to exclude in the `__init__.py` file.

In `routers/dev/__init__.py`, import the `posts` module and add it to `EXCLUDED_ROUTERS` constant which is used
for excluding scanning for routers:

```py title="routers/dev/__init__.py"
from . import posts

EXCLUDED_ROUTERS = [posts]
```

The entire `routers/dev` module can be excluded by importing `dev` in the `routers/__init__.py`

```py title="routers/__init__.py"
from . import dev

EXCLUDED_ROUTERS = [dev]
```

---

## License

The project is licensed under the terms of the MIT license.

