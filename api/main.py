import os

from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

from src.api import user, product, brand, category, order, order_detail

load_dotenv()

app = FastAPI(docs_url='/docs')
routers = [
    (user.router, "users"),
    (product.router, "products"),
    (brand.router, "brands"),
    (category.router, "categorys"),
    (order.router, "orders"),
    (order_detail.router, "order_details"),
]
for router, tag in routers:
    app.include_router(router, prefix="/v1", tags=[tag])

class Item(BaseModel):
    id: int
    name: str
    description: str = None
    price: float

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}

@app.post("/items/")
def create_item(item: Item):
    return item
