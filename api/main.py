import os

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv

from src.api import user, product, brand, category, order, order_detail

load_dotenv()

app = FastAPI(docs_url='/docs')
app.include_router(user.router, prefix="/v1/user", tags=["user"])
app.include_router(product.router, prefix="/v1/product", tags=["product"])
app.include_router(brand.router, prefix="/v1/brand", tags=["brand"])
app.include_router(category.router, prefix="/v1/category", tags=["category"])
app.include_router(order.router, prefix="/v1/order", tags=["order"])
app.include_router(order_detail.router, prefix="/v1/order_detail", tags=["order_detail"])

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
