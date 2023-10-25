-- ユーザーの追加
INSERT INTO users (name, email) VALUES ('John', 'john@example.com');

-- ユーザーの検索
SELECT * FROM users WHERE name = 'John';

-- ユーザーの更新
UPDATE users SET name = 'John Smith' WHERE name = 'John';

-- ユーザーの削除
DELETE FROM users WHERE name = 'John Smith';
