from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    id: int
    username: str
    email: str

@router.post("/users/")
def create_user(user: User):
    return user

@router.get("/users/{users_id}")
def read_user(users_id: int, username: str = None, email: str = None):
    return {"user_id": users_id, "username": username, "email": email}
