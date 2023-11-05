from datetime import datetime
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.database import database

router = APIRouter()

# DDL
# CREATE TABLE orders (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     user_id INT,
#     total_price DECIMAL(10, 2),
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (user_id) REFERENCES users(id)
# );

# DML
# INSERT INTO
#     orders (user_id, total_price)
# VALUES
#     (1, 400.00),
#     (2, 250.00);

# curl -X GET "http://127.0.0.1:8000/v1/orders" -H  "accept: application/json"

# curl -X GET "http://127.0.0.1:8000/v1/orders/1" -H  "accept: application/json"

# curl -X POST "http://127.0.0.1:8000/v1/orders" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"user_id\":1,\"total_price\":400.0}"

# curl -X PUT "http://127.0.0.1:8000/v1/orders/1" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"user_id\":1,\"total_price\":400.0}"

# curl -X DELETE 'http://127.0.0.1:8000/v1/orders/1' -H 'accept: application/json'


class Order(BaseModel):
    id: Optional[int] = None
    user_id: int
    total_price: float
    created_at: Optional[datetime] = None


# HTTP GET
@router.get("/orders", response_model=list[Order])
async def read_orders():
    query = "SELECT * FROM orders"
    try:
        orders = await database.fetch_all(query)
        return orders
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# HTTP GET
@router.get("/orders/{id}", response_model=Order)
async def read_order(order_id: int):
    query = "SELECT * FROM orders WHERE id = :id"
    order = await database.fetch_one(query, values={"id": order_id})
    if order:
        return order
    raise HTTPException(status_code=404, detail="Order not found")


# HTTP POST
@router.post("/orders", response_model=Order)
async def create_order(order: Order):
    query = "INSERT INTO orders(user_id, total_price) VALUES (:user_id, :total_price)"
    last_record_id = await database.execute(
        query=query, values={"user_id": order.user_id, "total_price": order.total_price}
    )
    return {**order.dict(), "id": last_record_id}


# HTTP PUT
@router.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, order: Order):
    query = "UPDATE orders SET user_id = :user_id WHERE id = :order_id"
    await database.execute(
        query, values={"user_id": order.user_id, "order_id": order_id}
    )
    return await read_order(order_id)


# HTTP DELETE
@router.delete("/orders/{order_id}", response_model=Order)
async def delete_order(order_id: int):
    order = await read_order(order_id)
    query = "DELETE FROM orders WHERE id = :order_id"
    await database.execute(query, values={"order_id": order_id})
    return order
