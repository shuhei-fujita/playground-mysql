from dotenv import load_dotenv
from fastapi import FastAPI, Request
from pydantic import BaseModel
from src.api import brand, category, order, order_detail, product, user
from src.database import connect_to_db, disconnect_from_db
from src.logger_config import get_logger

# logger をグローバル変数として初期化
logger = get_logger()

load_dotenv()
app = FastAPI(docs_url="/docs")


def return_app():
    return app


routers = [
    (user.router, "users"),
    (product.router, "products"),
    (brand.router, "brands"),
    (category.router, "categorys"),
    (order.router, "order"),
    (order_detail.router, "order_detail"),
]
for router, tag in routers:
    app.include_router(router, prefix="/v1", tags=[tag])


@app.get("/")
def read_root():
    return {"msg": "Hello World"}


@app.on_event("startup")
async def startup_event():
    await connect_to_db()


@app.on_event("shutdown")
async def shutdown_event():
    await disconnect_from_db()


# ミドルウェアの追加
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"リクエスト開始: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(
        f"リクエスト完了: {request.method} {request.url}, ステータス: {response.status_code}"
    )
    return response
