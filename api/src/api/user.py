from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Path, Request
from pydantic import BaseModel
from src.database import database
from src.logger_config import get_logger

router = APIRouter()


class User(BaseModel):
    id: Optional[int] = None
    username: str
    password_hash: str
    email: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@router.get("/users/", response_model=List[User])
async def read_users():
    query = "SELECT * FROM users"
    try:
        users = await database.fetch_all(query)
        return users
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/users/{id}", response_model=User)
async def read_user(id: int = Path(..., description="The ID of the user to get.")):
    query = "SELECT * FROM users WHERE id = :id"
    try:
        user = await database.fetch_one(query, values={"id": id})
        if user:
            return user
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ユーザーが id を送信しないようにして、データベースがそれを自動で割り当てることを確認します。
# values 辞書から id キーを削除します（もしそれが存在している場合）。
@router.post("/users/", response_model=User)
async def create_user(user: User):
    now = datetime.utcnow().isoformat()
    query = """
    INSERT INTO users(username, password_hash, email, created_at, updated_at)
    VALUES (:username, :password_hash, :email, :created_at, :updated_at)
    """
    values = {**user.dict(exclude_unset=True), "created_at": now, "updated_at": now}
    try:
        user_id = await database.execute(query=query, values=values)
        created_user = {
            **user.dict(),
            "id": user_id,
            "created_at": now,
            "updated_at": now,
        }
        return created_user
    except Exception as e:
        logger = get_logger()
        logger.error(f"Error creating user: {e}", exc_info=True)
        raise HTTPException(status_code=400, detail=str(e))


# exclude_unset=True を使用して、デフォルト値がセットされていないフィールドを除外し、exclude={"created_at", "id"} でこれら2つのフィールドを明示的に更新データから除外しています。
# これにより、created_at は更新クエリに含まれず、エラーを回避することができます。
@router.put("/users/{id}", response_model=User)
async def update_user(id: int, user: User):
    # 'created_at' と 'id' フィールドを更新データから除外
    update_data = user.dict(exclude_unset=True, exclude={"created_at", "id"})

    query = """
    UPDATE users
    SET username=:username, password_hash=:password_hash, email=:email, updated_at=CURRENT_TIMESTAMP
    WHERE id=:id
    """
    values = {**update_data, "id": id}  # ここで 'id' を指定
    try:
        await database.execute(query, values=values)
        return await read_user(id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/users/{id}", response_model=User)
async def delete_user(id: int):
    user = await read_user(id)
    query = "DELETE FROM users WHERE id = :id"
    try:
        await database.execute(query, values={"id": id})
        return user
    except Exception as e:
        logger = get_logger()
        logger.error(f"Error creating user: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
