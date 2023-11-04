from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Product(BaseModel):
    id: int
    name: str
    brand_id: int
    category_id: int
    price: float
    stock_quantity: int

@router.post("/products/")
def create_product(product: Product):
    return product
