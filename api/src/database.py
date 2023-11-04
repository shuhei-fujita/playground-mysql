from fastapi import FastAPI
from databases import Database
import os
from dotenv import load_dotenv

load_dotenv()  # .env ファイルから環境変数を読み込む

# 環境変数からデータベースの接続情報を取得
DATABASE_URL = f"mysql://{os.getenv('MYSQL_USER')}:" \
               f"{os.getenv('MYSQL_PASSWORD')}@" \
               f"{os.getenv('MYSQL_HOST')}:" \
               f"{os.getenv('MYSQL_PORT')}/" \
               f"{os.getenv('MYSQL_DB_NAME')}"

# 非同期データベースオブジェクトの作成
database = Database(DATABASE_URL)
print(DATABASE_URL)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()