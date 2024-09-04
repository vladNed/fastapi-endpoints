# Auto Discovery

The auto discovery feature works by calling the `auto_include_routers` function within the project, with the FastAPI application and the routers module as paramters.

!!! note

    It is mandatory, for now, to have a directory called `routers` where all the endpoints are defined and instanciated with an `fastapi.APIRouter` object.i

## File-based routing

When a project is launched with `auto_include_routers` called, fastapi-endpoints walks through each module under the `routers` module of the app.

Python modules found with an `APIRouter` instance will be registered in the application.

!!! info "Keep routers directory clean"

    There should not be any python module (beside `__init__.py`) without an instance of a router. The app will raise an error if the case is applicable.

## Prefix format

The prefix for any router is obtained by the path to the file relative to the `routers` directory.

For example, if you have the following directory structure:

```
routers
|── __init__.py
├── api_v1
│   ├── __init__.py
│   ├── users.py
│   └── posts.py
|── api_v2
|    ├── __init__.py
|    ├── users.py
|    └── posts.py
app.py
```

For each router file, the prefix will be as follows:

- `src/routers/api_v1/users.py` -> `/api/v1/users`
- `src/routers/api_v1/posts.py` -> `/api/v1/posts`
- `src/routers/api_v2/users.py` -> `/api/v2/users`
- `src/routers/api_v2/posts.py` -> `/api/v2/posts`
