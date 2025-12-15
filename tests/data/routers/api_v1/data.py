from fastapi import APIRouter

router = APIRouter(tags=["data"])


@router.get("/")
async def read_root():
    return {"Hello": "World"}


@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
