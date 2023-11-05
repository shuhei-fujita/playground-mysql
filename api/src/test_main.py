import os

import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from httpx import AsyncClient
from src.api.user import router
from src.database import DATABASE_URL, connect_to_db, disconnect_from_db

from .main import app

load_dotenv()

client = TestClient(app)
app.include_router(router)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


@pytest.mark.asyncio
async def test_connect_database():
    print(DATABASE_URL)
    await connect_to_db()
    assert (
        DATABASE_URL == f"mysql://{os.getenv('MYSQL_USER')}:"
        f"{os.getenv('MYSQL_PASSWORD')}@"
        f"localhost:"
        f"{os.getenv('MYSQL_PORT')}/"
        f"{os.getenv('MYSQL_DB_NAME')}"
    )
    await disconnect_from_db()


# FastAPIの TestClient を使用する場合、データベース接続を開始と終了するための非同期イベントハンドラー（connect_to_db, disconnect_from_db）が正しく動作するか確認する必要があります。
# テストクライアントでの非同期処理をサポートするために AsyncTestClient を使用
# テストケース内でデータベース接続と切断を明示的に行います。
@pytest.mark.asyncio
async def test_read_users2():
    await connect_to_db()
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/users")
    await disconnect_from_db()
    print(response)
    print(response.status_code)
    assert response.status_code == 200
