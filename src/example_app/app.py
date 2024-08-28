import fastapi

from fastapi_endpoints import auto_include_routers
from example_app import routers

app = fastapi.FastAPI()
auto_include_routers(app, routers)