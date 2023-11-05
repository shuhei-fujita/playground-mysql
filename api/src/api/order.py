from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Order(BaseModel):
    id: int
    user_id: int
    total_price: float


@router.post("/orders/")
def create_order(order: Order):
    return order
