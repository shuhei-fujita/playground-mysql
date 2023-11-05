from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.database import database

router = APIRouter()


class Brand(BaseModel):
    id: Optional[int] = None
    name: str


@router.get("/brands", response_model=list[Brand])
async def read_brands():
    query = "SELECT * FROM brands"
    return await database.fetch_all(query)


@router.get("/brands/{brand_id}", response_model=Brand)
async def read_brand(brand_id: int):
    query = "SELECT * FROM brands WHERE id = :brand_id"
    brand = await database.fetch_one(query=query, values={"brand_id": brand_id})
    if brand is not None:
        return brand
    raise HTTPException(status_code=404, detail="Brand not found")


@router.post("/brands", response_model=Brand)
async def create_brand(brand: Brand):
    query = "INSERT INTO brands(name) VALUES (:name)"
    last_record_id = await database.execute(query=query, values={"name": brand.name})
    return {**brand.dict(), "id": last_record_id}


@router.put("/brands/{brand_id}", response_model=Brand)
async def update_brand(brand_id: int, brand: Brand):
    query = "UPDATE brands SET name = :name WHERE id = :brand_id"
    await database.execute(query, values={"name": brand.name, "brand_id": brand_id})
    return await read_brand(brand_id)


@router.delete("/brands/{brand_id}", response_model=Brand)
async def delete_brand(brand_id: int):
    brand = await read_brand(brand_id)
    query = "DELETE FROM brands WHERE id = :brand_id"
    await database.execute(query, values={"brand_id": brand_id})
    return brand
