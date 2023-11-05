### エンドポイントの設計について

DDL設計とINDEX設計を元に、RESTfulなAPIエンドポイントを設計することができます。以下は基本的なエンドポイントの一例です。

1. Users
    - `GET /v1/users`
    - `GET /v1/users/{id}`
    - `POST /v1/users`
    - `PUT /v1/users/{id}`
    - `DELETE /v1/users/{id}`

2. Products
    - `GET /v1/products`
    - `GET /v1/products/{id}`
    - `POST /v1/products`
    - `PUT /v1/products/{id}`
    - `DELETE /v1/products/{id}`

3. Brands
    - `GET /v1/brands`
    - `GET /v1/brands/{id}`
    - `POST /v1/brands`
    - `PUT /v1/brands/{id}`
    - `DELETE /v1/brands/{id}`

4. Categories
    - `GET /v1/categories`
    - `GET /v1/categories/{id}`
    - `POST /v1/categories`
    - `PUT /v1/categories/{id}`
    - `DELETE /v1/categories/{id}`

5. Orders
    - `GET /v1/orders`
    - `GET /v1/orders/{id}`
    - `POST /v1/orders`
    - `PUT /v1/orders/{id}`
    - `DELETE /v1/orders/{id}`

6. Order Details (Nested Resources)
    - `GET /v1/orders/{order_id}/details`
    - `GET /v1/orders/{order_id}/details/{id}`
    - `POST /v1/orders/{order_id}/details`
    - `PUT /v1/orders/{order_id}/details/{id}`
    - `DELETE /v1/orders/{order_id}/details/{id}`

#### フィルタリングとページネーション

- `GET /v1/users?active=true&page=2`

curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"id": 1, "username": "test_user", "email": "test@example.com"}' \
    http://0.0.0.0:8000/v1/user/users

curl http://0.0.0.0:8000/v1/user/users/1
