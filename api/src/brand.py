from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Brand(BaseModel):
    id: int
    name: str

@router.post("/brands/")
def create_brand(brand: Brand):
    return brand
