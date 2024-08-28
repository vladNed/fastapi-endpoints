from fastapi import APIRouter

router = APIRouter(tags=["probes"])


@router.get("/")
async def read_root():
    return {"msg": "ok"}


@router.get("/{msg}/")
async def read_msg(msg: str):
    return {"msg": msg}
