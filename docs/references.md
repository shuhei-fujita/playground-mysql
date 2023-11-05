## 参考

全体
- https://qiita.com/poly_soft/items/fb649573c19b7a5c0227
- https://note.nkmk.me/python-os-mkdir-makedirs/

DB
- https://dev.mysql.com/doc/refman/8.0/ja/
- https://zenn.dev/mpyw/articles/rdb-ids-and-timestamps-best-practices

API
- https://qiita.com/KNR109/items/d3b6aa8803c62238d990#%E7%9F%AD%E3%81%8F%E3%81%A6%E5%85%A5%E5%8A%9B%E3%81%8C%E3%81%97%E3%82%84%E3%81%99%E3%81%84
- https://qiita.com/shuto-S/items/78868cbf03f9deec0fba

---

# MySQLの学習プラン

## 基本的な学習内容

1. **基本的なDDL (Data Definition Language)**
    - `CREATE TABLE`
    - `ALTER TABLE`
    - `DROP TABLE`
    - `CREATE INDEX`

2. **基本的なDML (Data Manipulation Language)**
    - `SELECT`
    - `INSERT`
    - `UPDATE`
    - `DELETE`

3. **基本的なDCL (Data Control Language)**
    - `GRANT`
    - `REVOKE`

4. **文字コードとエンコーディング**
    - UTF-8, Latin1 など

5. **インデックス**
    - 一意インデックス
    - 非一意インデックス
    - フルテキストインデックス

6. **トランザクション**
    - ACID特性
    - COMMIT
    - ROLLBACK

7. **デッドロック**
    - 発生条件
    - 対処法

8. **マスター・スレーブ構成**
    - レプリケーション
    - フェイルオーバー

## 追加的な学習内容

- **RDSやフルマネージドなRDBの利用方法**
- **SQLのパフォーマンスチューニング**
- **ストアドプロシージャとトリガー**

## 学習リソース

1. **公式ドキュメント**
    - [MySQL Official Documentation](https://dev.mysql.com/doc/)

2. **GAFAMのTech Blog**
    - Google, Amazon, Facebook, Apple, Microsoftなどの技術ブログ

3. **オンラインコース**
    - Udemy, Courseraなど

4. **書籍**
    - "High Performance MySQL" など

## プラクティス

- 既存の`playground-mysql`リポジトリを活用して、各トピックに関するSQLスクリプトを作成。
- `init-database.sh`スクリプトを使用して、データベースとテーブルを初期化。

このプランは、基本的なRDBとSQLの知識を高めるためのものです。特に若いエンジニアがRDBやSQLに関する基本的な知識を身につけることで、より効率的かつ安全なデータベース操作が可能になります。
