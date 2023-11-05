# DDL (Data Definition Language) と DML (Data Manipulation Language) の学習

```bash
docker-compose up -d
```

```bash
mysql -h 127.0.0.1 -P 3306 -u root -p
```

## SQLの方法
- コマンドライン: 一行で短く（コマンド履歴の管理が容易）
- `.sql`ファイル: 改行やインデントを使って整形（可読性が高い）

```bash
poetry install
```

## 静的解析ツールの実行

flake8の実行 (コードのLinter):

```bash
poetry run flake8 .
```

blackの実行 (コードフォーマット):

```bash
poetry run black .
```

isortの実行 (インポートのソート):

```bash
poetry run isort .
```

mypyの実行 (型チェック):

```bash
poetry run mypy .
```

全ての静的解析ツールを実行:

```bash
poetry run flake8 &&
poetry run black . &&
poetry run isort . &&
poetry run mypy .
```
