import fastapi

router = fastapi.APIRouter(tags=["data"])


@router.get("/")
async def read_root():
    return {"Hello": "World"}


@router.get("/create")
async def create_root():
    return {"Hello": "World"}
