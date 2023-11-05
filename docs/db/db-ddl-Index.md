```prompt
データベース設計をして
- SQL設計（DDL）
- Index設計
- tableを.mdのドキュメントに残して

---
## 設計するwebサイトの情報
- “Year 2000”のY2Kのトレンドを取り入れたスニーカー専用ECサイトです
- 韓国ファッションやカルチャーを取り入れたブランドのスニーカー専用ECサイトです
```

## DDL設計
users
products
brands
categories
orders
order_details 

## Index設計
idx_username
idx_product_name
idx_product_brand
idx_product_category
idx_order_user

## DDL設計

```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

```sql
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    brand_id INT,
    category_id INT,
    price DECIMAL(10, 2),
    stock_quantity INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (brand_id) REFERENCES brands(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
```

```sql
CREATE TABLE brands (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE
);
```

```sql
CREATE TABLE categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE
);
```

```sql
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    total_price DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

```sql
CREATE TABLE order_details (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

## Index設計

```sql
CREATE INDEX idx_username ON users(username);
```

```sql
CREATE INDEX idx_product_name ON products(name);

CREATE INDEX idx_product_brand ON products(brand_id);

CREATE INDEX idx_product_category ON products(category_id);
```

```sql
CREATE INDEX idx_order_user ON orders(user_id);
```
