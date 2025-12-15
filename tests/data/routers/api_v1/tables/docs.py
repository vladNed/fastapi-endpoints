import fastapi

router = fastapi.APIRouter(tags=["tables.docs"])


@router.get("/")
async def read_docs():
    return {"Hello": "World"}


@router.get("/create")
async def create_docs():
    return {"Hello": "World"}
