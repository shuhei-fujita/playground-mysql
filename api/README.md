# API

FastAPIを使ったWebAPIのサンプルです。

## 環境構築

仮想環境を作成し、必要なライブラリをインストールする

```bash
cd ~/git/sample/playground-mysql/api &&
    python3 -m venv .venv &&
    source .venv/bin/activate &&
    poetry install
```

uvicornでローカルサーバーを起動する

```bash
uvicorn src.main:app --reload
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
  'http://localhost:8000/v1/users/1' \
  -H 'accept: application/json'
```

ex) POST /v1/sample
```bash
curl -X 'POST' \
  'http://localhost:8000/v1/users/' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "new_user",
  "password_hash": "somehashedpassword",
  "email": "user@example.com"
}'
```

ex) PUT /v1/sample
```bash
curl -X 'PUT' \
  'http://localhost:8000/v1/users/1' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "updated_user",
  "password_hash": "updatedpassword",
  "email": "updateduser@example.com"
}'
```

ex) DELETE /v1/sample
```bash
curl -X 'DELETE' \
  'http://localhost:8000/v1/users/1' \
  -H 'accept: application/json'
```

```bash
pytest --verbose --capture=no
```

```
=========================================================== test session starts ============================================================
platform darwin -- Python 3.10.5, pytest-7.4.3, pluggy-1.3.0 -- /Users/shuhei/git/sample/playground-mysql/api/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/shuhei/git/sample/playground-mysql/api
plugins: asyncio-0.21.1, anyio-3.7.1
asyncio: mode=strict
collecting ... mysql://root:xxxxxx@localhost:3306/shoes_ec_db
collected 3 items

src/test_main.py::test_read_main PASSED
src/test_main.py::test_connect_database mysql://root:xxxxxx@localhost:3306/shoes_ec_db
PASSED
src/test_main.py::test_read_users2 <Response [200 OK]>
200
PASSED
```

## デプロイ

## 参考

- [FastAPI](https://fastapi.tiangolo.com/)
