# API

FastAPIを使ったWebAPIのサンプルです。

## 環境構築

仮想環境を作成し、必要なライブラリをインストールする

```bash
cd ~/git/sample/playground-mysql/api &&
    python3 -m venv .venv &&
    source .venv/bin/activate &&
    pip install -r requirements.txt
```

uvicornでローカルサーバーを起動する

```bash
uvicorn main:app --reload
```

Swagger UI or ReDocを開く

```bash
open http://127.0.0.1:8000/docs
```

```bash
open http://127.0.0.1:8000/redoc
```

## テスト

ex) GET /v1/sample
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/v1/users/' \
  -H 'accept: application/json'
```

ex) POST /v1/sample
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/v1/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 0,
  "username": "string",
  "email": "string",
  "password_hash": "string"
}'
```

## デプロイ

## 参考

- [FastAPI](https://fastapi.tiangolo.com/)
