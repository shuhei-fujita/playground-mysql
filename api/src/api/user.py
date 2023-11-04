from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import sqlalchemy
from src.database import database

# SQLAlchemyのテーブルオブジェクトを定義
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(50), unique=True, nullable=False),
    sqlalchemy.Column("password_hash", sqlalchemy.String(255), nullable=False),
    sqlalchemy.Column("email", sqlalchemy.String(50)),
    sqlalchemy.Column("created_at", sqlalchemy.TIMESTAMP),
    sqlalchemy.Column("updated_at", sqlalchemy.TIMESTAMP),
)

router = APIRouter()

class User(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password_hash: Optional[str] = None

@router.post("/users/")
def create_user(user: User):
    return user

@router.get("/users/{users_id}")
def read_user(users_id: int, username: str = None, email: str = None):
    return {"user_id": users_id, "username": username, "email": email}

# @router.get("/users/", response_model=List[User])
# def read_users():
#     # 実際にはここでデータベースからすべてのユーザーを取得するロジックを実装します。
#     # 以下はモックのレスポンスです。
#     return [
#         {"id": 1, "username": "user1", "email": "user1@example.com", "password_hash": "hash1"},
#         {"id": 2, "username": "user2", "email": "user2@example.com", "password_hash": "hash2"}
#     ]

@router.get("/users/")
async def read_users():
    query = "SELECT * FROM users"  # 適宜、実際のテーブル名に変更してください
    try:
        await database.connect()
        users = await database.fetch_all(query)
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await database.disconnect()
