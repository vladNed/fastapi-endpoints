import fastapi

router = fastapi.APIRouter(tags=["data"])


@router.get("/")
async def read_root():
    return {"Hello": "World"}
