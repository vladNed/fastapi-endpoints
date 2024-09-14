# Quick start

## New Project

First, be sure you have a python environment created and activated.

Create a project with the following structure:
```
routers
├── items.py
└── __init__.py
app.py
__init__.py
```

In the `app.py` file, add the following code:

```py
from fastapi import FastAPI
from fastapi_endpoints import auto_include_routers

from . import routers

app = FastAPI()

auto_include_routers(app, routers)
```

In the `routers/items.py` file, add the following code:

```py
from fastapi import APIRouter

items_router = APIRouter()

@items_router.get("/")
def get_items():
    return {"item1": "my-item"}


@items_router.get("/{item_id}/")
def get_item(item_id: int):
    return {"item1": "my-item", "id": item_id}
```

Start the FastAPI webserver using `uvicorn`

The items endpoints should now appear if you go to 

[http://localhost:8000/docs](http://localhost:8000/docs)

---

## Existing Project

An example of an existing project structure:

```
routers
├── items.py
└── __init__.py
app.py
__init__.py
```

```py title="app.py"
from fastapi import FastAPI

from .routers import items

app = FastAPI()

app.include_router(items.router, prefix="/api/v1/items")
```

```py title="routers/items.py"
from fastapi import APIRouter

items_router = APIRouter()

@items_router.get("/")
def get_items():
    return {"item1": "my-item"}


@items_router.get("/{item_id}/")
def get_item(item_id: int):
    return {"item1": "my-item", "id": item_id}
```

First, import `auto_include_routers` in `app.py` and give the `routers` module and `app` as parameters. 

Then, remove the `app.include_router` from the file.

```py title="app.py" hl_lines="2 7"
from fastapi import FastAPI
from fastapi_endpoints import auto_include_routers

from . import routers

app = FastAPI()
auto_include_routers(app, routers)
```

To keep the same prefix as specified in the `app.include_router`, move `items.py` to `routers/api_v1/items.py`.

The project structure should look like this now:

``` hl_lines="2 3 4"
routers
|── api_v1
|   |── items.py
|   └── __init__.py
└── __init__.py
app.py
__init__.py
```

Now, the same behaviour is kept and now creating new routers is just adding files to the `api_v1` directory.

---

## Adding a new router

A new router can be added to the FastAPI app as simple as creating a new file. Actually, this is how you add 
a new router to an existing project.

For example, having a project structure like this: 

```
routers
|── api_v1
|   |── items.py
|   └── __init__.py
└── __init__.py
app.py
__init__.py
```

Create a new file, like `new_router.py` and add it anywhere within the `routers` project. First, let's try
adding it under `routers/api_v1`.

``` hl_lines="3"
routers 
|── api_v1
|   |── new_router.py
|   |── items.py
|   └── __init__.py
└── __init__.py
app.py
__init__.py
```

Create a new `APIRouter` instance, and add your routes:

```py title="routers/api_v1/new_router.py"
from fastapi import APIRouter

router = APIRouter()

# Add routes here
# ...
```

Start the project normally, and now observe that the new endpoints routes have paths `/api/v1/new_router/`.
