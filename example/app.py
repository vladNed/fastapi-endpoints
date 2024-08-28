from fastapi import FastAPI
from fastapi_endpoints import auto_include_routers

from . import routers

app = FastAPI()
auto_include_routers(app, routers)
