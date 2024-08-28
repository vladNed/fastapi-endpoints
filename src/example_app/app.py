import fastapi
import fastapi_endpoints

app = fastapi.FastAPI()

fastapi_endpoints.include_routers(app)
