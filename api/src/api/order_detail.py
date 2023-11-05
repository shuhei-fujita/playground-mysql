from datetime import datetime
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.database import database

router = APIRouter()

# DDL
# CREATE TABLE order_details (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     order_id INT,
#     product_id INT,
#     quantity INT,
#     FOREIGN KEY (order_id) REFERENCES order_details(id),
#     FOREIGN KEY (product_id) REFERENCES products(id)
# );

# DML
# INSERT INTO
#     order_details (order_id, product_id, quantity)
# VALUES
#     (1, 1, 2),
#     (1, 3, 1),
#     (2, 2, 1);


class OrderDetail(BaseModel):
    id: Optional[int] = None
    order_id: int
    product_id: int
    quantity: int


# HTTP GET
@router.get("/order_details", response_model=list[OrderDetail])
async def read_order_details():
    query = "SELECT * FROM order_details"
    try:
        order_details = await database.fetch_all(query)
        return order_details
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# HTTP GET
@router.get("/order_details/{order_details_id}", response_model=OrderDetail)
async def read_order_detail(order_details_id: int):
    query = "SELECT * FROM order_details WHERE id = :order_details_id"
    order_details = await database.fetch_one(
        query=query, values={"order_details_id": order_details_id}
    )
    if order_details:
        return order_details
    raise HTTPException(status_code=404, detail="Order not found")


# HTTP POST
@router.post("/order_details", response_model=OrderDetail)
async def create_order_details(order_details: OrderDetail):
    query = "INSERT INTO order_details(order_id, product_id, quantity) VALUES (:order_id, :product_id, :quantity)"
    last_record_id = await database.execute(
        query,
        values={
            "order_id": order_details.order_id,
            "product_id": order_details.product_id,
            "quantity": order_details.quantity,
        },
    )
    return {**order_details.dict(), "id": last_record_id}


# HTTP PUT
@router.put("/order_details/{order_details_id}", response_model=OrderDetail)
async def update_order_details(order_details_id: int, order_detail: OrderDetail):
    query = """
        UPDATE order_details
        SET order_id = :order_id, product_id = :product_id, quantity = :quantity
        WHERE id = :order_details_id
    """
    await database.execute(
        query,
        values={
            "order_id": order_detail.order_id,
            "product_id": order_detail.product_id,
            "quantity": order_detail.quantity,
            "order_details_id": order_details_id,
        },
    )
    return await read_order_detail(order_details_id)


# HTTP DELETE
@router.delete("/order_details/{order_details_id}", response_model=OrderDetail)
async def delete_order_details(order_details_id: int):
    order_details = await read_order_detail(order_details_id)
    query = "DELETE FROM order_details WHERE id = :order_details_id"
    await database.execute(query, values={"order_details_id": order_details_id})
    return order_details
