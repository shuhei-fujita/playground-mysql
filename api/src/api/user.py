from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from src.database import database

router = APIRouter()

class User(BaseModel):
    id: Optional[int] = None
    username: str
    password_hash: str
    email: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

@router.post("/users/", response_model=User)
async def create_user(user: User):
    query = """
    INSERT INTO users(username, password_hash, email, created_at, updated_at)
    VALUES (:username, :password_hash, :email, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
    """
    values = {**user.dict()}
    values.pop("id", None)  # IDは自動生成されるため、値を削除
    try:
        await database.execute(query=query, values=values)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user

@router.get("/users/", response_model=List[User])
async def read_users():
    query = "SELECT * FROM users"
    try:
        users = await database.fetch_all(query)
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
