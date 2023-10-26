from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Category(BaseModel):
    id: int
    name: str

@router.post("/categories/")
def create_category(category: Category):
    return category
