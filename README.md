# DDL (Data Definition Language) と DML (Data Manipulation Language) の学習

```bash
docker-compose up -d
```

```bash
mysql -h 127.0.0.1 -P 3306 -u root
```

## SQLの方法
- コマンドライン: 一行で短く（コマンド履歴の管理が容易）
- `.sql`ファイル: 改行やインデントを使って整形（可読性が高い）

## 仮想環境でmycliを使う

```bash
python -m venv .venv
```

````bash
source venv/bin/activate
````

```bash
pip install mycli
```
