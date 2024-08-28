import fastapi
import fastapi_endpoints

from example_app import routers

app = fastapi.FastAPI()

fastapi_endpoints.auto_include_routers(app, routers)
