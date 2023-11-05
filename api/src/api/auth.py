from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from pydantic import BaseModel

router = APIRouter()


class User(BaseModel):
    username: str
    password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/signup")
async def sign_up(user: User):
    # ユーザー登録のロジックを実装します
    hashed_password = pwd_context.hash(user.password)
    return {"message": "ユーザーが作成されました"}


@router.post("/signin")
async def sign_in(user: User):
    # ログイン処理とJWTトークンの発行を実装します
    return {"message": "ログインしました"}


@router.get("/authz")
def read_auth():
    return {"msg": "Hello World"}

@router.get("/authn")
def read_auth():
    return {"msg": "Hello World"}
