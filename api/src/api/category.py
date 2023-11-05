from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.database import database

router = APIRouter()

# DDL
# CREATE TABLE categories (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(50) NOT NULL UNIQUE
# );

# DML
# INSERT INTO
#     categories (name)
# VALUES
#     ('Sneakers'),
#     ('Boots');


class Category(BaseModel):
    id: Optional[int] = None
    name: str


@router.get("/categories", response_model=list[Category])
async def read_categories():
    query = "SELECT * FROM categories"
    return await database.fetch_all(query)


@router.get("/categories/{category_id}", response_model=Category)
async def read_category(category_id: int):
    query = "SELECT * FROM categories WHERE id = :category_id"
    category = await database.fetch_one(
        query=query, values={"category_id": category_id}
    )
    if category is not None:
        return category
    raise HTTPException(status_code=404, detail="Category not found")


@router.post("/categories", response_model=Category)
async def create_category(category: Category):
    query = "INSERT INTO categories(name) VALUES (:name)"
    last_record_id = await database.execute(query=query, values={"name": category.name})
    return {**category.dict(), "id": last_record_id}


@router.put("/categories/{category_id}", response_model=Category)
async def update_category(category_id: int, category: Category):
    query = "UPDATE categories SET name = :name WHERE id = :category_id"
    await database.execute(
        query, values={"name": category.name, "category_id": category_id}
    )
    return await read_category(category_id)


@router.delete("/categories/{category_id}", response_model=Category)
async def delete_category(category_id: int):
    category = await read_category(category_id)
    query = "DELETE FROM categories WHERE id = :category_id"
    await database.execute(query, values={"category_id": category_id})
    return category
