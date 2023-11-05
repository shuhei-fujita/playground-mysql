from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Path
from pydantic import BaseModel
from src.database import database

router = APIRouter()


class Product(BaseModel):
    id: Optional[int] = None
    name: str
    brand_id: int
    category_id: int
    price: float
    stock_quantity: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@router.get("/products/", response_model=List[Product])
async def read_products():
    query = "SELECT * FROM products"
    try:
        products = await database.fetch_all(query)
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/products/{id}", response_model=Product)
async def read_product(
    id: int = Path(..., description="The ID of the product to get.")
):
    query = "SELECT * FROM products WHERE id = :id"
    try:
        product = await database.fetch_one(query, values={"id": id})
        if product:
            return product
        raise HTTPException(status_code=404, detail="Product not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/products/", response_model=Product)
async def create_product(product: Product):
    now = datetime.utcnow().isoformat()
    query = """
    INSERT INTO products(name, brand_id, category_id, price, stock_quantity, created_at, updated_at)
    VALUES (:name, :brand_id, :category_id, :price, :stock_quantity, :created_at, :updated_at)
    """
    values = {**product.dict(exclude_unset=True), "created_at": now, "updated_at": now}
    try:
        product_id = await database.execute(query=query, values=values)
        created_product = {
            **product.dict(),
            "id": product_id,
            "created_at": now,
            "updated_at": now,
        }
        return created_product
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/products/{id}", response_model=Product)
async def update_product(id: int, product: Product):
    update_data = product.dict(exclude_unset=True, exclude={"created_at", "id"})
    query = """
    UPDATE products
    SET name=:name, brand_id=:brand_id, category_id=:category_id, price=:price, stock_quantity=:stock_quantity, updated_at=CURRENT_TIMESTAMP
    WHERE id=:id
    """
    values = {**update_data, "id": id}
    try:
        await database.execute(query, values=values)
        return await read_product(id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/products/{id}", response_model=Product)
async def delete_product(id: int):
    product = await read_product(id)
    query = "DELETE FROM products WHERE id = :id"
    try:
        await database.execute(query, values={"id": id})
        return product
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
