from fastapi import APIRouter

from app.schemas import item

router = APIRouter()


@router.get("/", response_model=item.ItemBase)
async def read_items():
    return {"title": "Test", "description": "Test"}
