# テストに関するドキュメント

`test` フォルダには、データベースのテストに関連するスクリプトが格納されています。

## ファイルの

- **insert_test_data.py**: テスト用のデータをデータベースに挿入するためのスクリプト。
- **test_database.py**: 実際のデータベーステストを実行するスクリプト。テスト結果は、テーブル形式で出力されます。
- **clean_test_data.py**: テストデータをクリーンアップするためのスクリプト。

## テストの実行方法

1. 仮想環境を有効にする

```bash
cd ~/git/sample/playground-mysql/db &&
    python3 -m venv .venv &&
    source .venv/bin/activate &&
    pip install -r requirements.txt
```

2. テストデータをデータベースに挿入する

```bash
python ./test/insert_test_data.py
```

3. テストを実行する

```bash
python ./test/test_database.py
```

4. テストデータをクリーンアップする

```bash
python ./test/clean_test_data.py
```

実行すると、テーブル形式でテスト結果が表示されます
```bash
(.venv) ~/playground-mysql $ python ./test/test_database.py
Testing Results: Table Data
+-----------------------------+------------+-----------+----------+--------+
|          Test Case          |   Table    | Test Data |  Actual  | Result |
+-----------------------------+------------+-----------+----------+--------+
|  Username Check for shuhei  |   users    |   shuhei  |  shuhei  | Passed |
| Username Check for shuheiii |   users    |  shuheiii |  shuhei  | Failed |
|   Username Check for user2  |   users    |   user2   |  user2   | Passed |
|      Product Name Check     |  products  |  Air Max  | Air Max  | Passed |
|       Brand Name Check      |   brands   |    Nike   |   Nike   | Passed |
|     Category Name Check     | categories |  Sneakers | Sneakers | Passed |
+-----------------------------+------------+-----------+----------+--------+
```

5. 仮想環境を無効にする

```bash
deactivate
```
