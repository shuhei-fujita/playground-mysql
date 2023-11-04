# API

FastAPIを使ったWebAPIのサンプルです。

```bash
cd ~/git/sample/playground-mysql/api &&
    python3 -m venv .venv &&
    source .venv/bin/activate &&
    pip install -r requirements.txt
```

```bash
uvicorn main:app --reload
```

```bash
open http://127.0.0.1:8000/docs
```

```bash
open http://127.0.0.1:8000/redoc
```

ex) GET /v1/sample
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/v1/user/users/' \
  -H 'accept: application/json'
```

ex) POST /v1/sample
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/v1/user/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 0,
  "username": "string",
  "email": "string",
  "password_hash": "string"
}'
```

## ディレクトリ構成

```
api
├── README.md
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── api_v1
│   │   │   ├── __init__.py
│   │   │   ├── endpoints
│   │   │   │   ├── __init__.py
│   │   │   │   └── sample.py
│   │   │   └── router.py
│   │   └── api_v2
│   │       ├── __init__.py
│   │       ├── endpoints
│   │       │   ├── __init__.py
│   │       │   └── sample.py
│   │       └── router.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── db.py
│   │   ├── security.py
│   │   └── settings.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   └── sample.py
│   └── schemas
│       ├── __init__.py
│       └── sample.py
├── docker-compose.yml
├── dockerfile
├── poetry.lock
├── pyproject.toml
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── test_api_v1
    │   ├── __init__.py
    │   └── test_sample.py
    └── test_api_v2
        ├── __init__.py
        └── test_sample.py
```

## ローカル環境構築

### 1. Dockerコンテナの起動

```bash
$ docker-compose up -d --build
```

### 2. マイグレーション

```bash
$ docker-compose exec api poetry run alembic upgrade head
```

### 3. APIの起動

```bash
$ docker-compose exec api poetry run uvicorn app.main:app --reload --host
```

### 4. APIの確認

```bash
$ curl http://localhost:8000/api/v1/sample
{"message":"Hello World"}
```

## テスト

```bash
$ docker-compose exec api poetry run pytest
```

## デプロイ

### 1. デプロイ先の設定

```bash
$ heroku git:remote -a <app_name>
```

### 2. デプロイ

```bash
$ git push heroku master
```

## ドキュメント

### Swagger

http://localhost:8000/docs

### Redoc

http://localhost:8000/redoc

## 参考

- [FastAPI](https://fastapi.tiangolo.com/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [FastAPIでWebAPIを作ってみる](https://qiita.com/bee2/items/1e8b3e7b2d0b0e6b0b0e)
