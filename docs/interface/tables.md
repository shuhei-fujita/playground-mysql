## Table設計

| カラム        | 説明                                                         |
| ------------- | ------------------------------------------------------------ |
| id            | ユーザーID（主キー、自動採番）                               |
| username      | ユーザー名（ユニーク制約あり）                               |
| password_hash | パスワードのハッシュ（NOT NULL制約あり）                     |
| email         | メールアドレス                                               |
| created_at    | 作成日時（デフォルトで現在の日時）                           |
| updated_at    | 更新日時（デフォルトで現在の日時、レコード更新時に自動更新） |

### Products Table

| カラム         | 説明                                                         |
| -------------- | ------------------------------------------------------------ |
| id             | 商品ID（主キー、自動採番）                                   |
| name           | 商品名（NOT NULL制約あり）                                   |
| brand_id       | ブランドID（外部キー）                                       |
| category_id    | カテゴリID（外部キー）                                       |
| price          | 価格                                                         |
| stock_quantity | 在庫数量                                                     |
| created_at     | 作成日時（デフォルトで現在の日時）                           |
| updated_at     | 更新日時（デフォルトで現在の日時、レコード更新時に自動更新） |

### Brands Table

| カラム | 説明                           |
| ------ | ------------------------------ |
| id     | ブランドID（主キー、自動採番） |
| name   | ブランド名（ユニーク制約あり） |

### Categories Table

| カラム | 説明                           |
| ------ | ------------------------------ |
| id     | カテゴリID（主キー、自動採番） |
| name   | カテゴリ名（ユニーク制約あり） |

### Orders Table

| カラム      | 説明                               |
| ----------- | ---------------------------------- |
| id          | 注文ID（主キー、自動採番）         |
| user_id     | ユーザーID（外部キー）             |
| total_price | 合計金額                           |
| created_at  | 作成日時（デフォルトで現在の日時） |

### OrderDetails Table

| カラム     | 説明                           |
| ---------- | ------------------------------ |
| id         | 注文詳細ID（主キー、自動採番） |
| order_id   | 注文ID（外部キー）             |
| product_id | 商品ID（外部キー）             |
| quantity   | 注文数量                       |

## Index設計

### Index Table

| インデックス名       | 対象テーブル | 対象カラム  |
| -------------------- | ------------ | ----------- |
| idx_username         | users        | username    |
| idx_product_name     | products     | name        |
| idx_product_brand    | products     | brand_id    |
| idx_product_category | products     | category_id |
| idx_order_user       | orders       | user_id     |
