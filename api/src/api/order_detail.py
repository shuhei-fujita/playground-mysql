from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class OrderDetail(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int

@router.post("/order_details/")
def create_order_detail(order_detail: OrderDetail):
    return order_detail
