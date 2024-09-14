# Exclude Routers

You can exclude routers from being registered by the router by defining the `EXCLUDED_ROUTERS` variable in the `__init__.py` file of any submodule of the `routers` module. All excluded routers will be bundled together and excluded from the registration process.

!!! note
    The `EXCLUDED_ROUTERS` constant variable is a keyword that the `auto_include_routers` function looks for when registering routers. It is important to define the variable in the `__init__.py` file of the submodule you want to exclude.

!!! info
    It is important to note that the `EXCLUDED_ROUTERS` variable should be a list of the routers you want to exclude from the registration process.

For example, if you have the following directory structure:
```
routers
├── __init__.py
├── api_v1
│   ├── __init__.py
│   ├── users.py
│   └── posts.py
app.py
```

You can exclude the `users.py` router from being registered by defining the `EXCLUDED_ROUTERS` variable in the `api_v1/__init__.py` file.

```python title="src/routers/api_v1/__init__.py"
from . import users

EXCLUDED_ROUTERS = [users]
```