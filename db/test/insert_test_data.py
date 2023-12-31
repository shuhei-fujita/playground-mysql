import os
import sys

import pymysql
from dotenv import load_dotenv

load_dotenv()


def get_env_variable(name):
    value = os.getenv(name)
    if value is None:
        print(f"環境変数 {name} が設定されていません。", file=sys.stderr)
        sys.exit(1)
    return value


MYSQL_HOST = get_env_variable("MYSQL_HOST")
MYSQL_USER = get_env_variable("MYSQL_USER")
MYSQL_PORT = int(get_env_variable("MYSQL_PORT"))
MYSQL_PASSWORD = get_env_variable("MYSQL_PASSWORD")
MYSQL_DB_NAME = get_env_variable("MYSQL_DB_NAME")


def execute_single_statement(statement, cursor):
    if not statement.strip():
        return
    try:
        cursor.execute(statement)
    except pymysql.MySQLError as e:
        print(f"エラーが発生しました: {e}")


def execute_sql_from_file(filename, cursor):
    with open(filename, "r") as file:
        sql_statements = file.read().split(";")
    for statement in sql_statements:
        execute_single_statement(statement, cursor)


def create_shoes_ec_db():
    # connection = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER)
    connection = pymysql.connect(
        host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, port=MYSQL_PORT
    )
    cursor = connection.cursor()

    # データベースを作成
    cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(MYSQL_DB_NAME))

    # 新しく作成したデータベースに接続
    cursor.execute("USE {}".format(MYSQL_DB_NAME))

    # DDLの各SQLファイルを実行
    ddl_files = [
        "../ddl/users.sql",
        "../ddl/brands.sql",
        "../ddl/categories.sql",
        "../ddl/products.sql",
        "../ddl/orders.sql",
        "../ddl/order_details.sql",
    ]
    for ddl_file in ddl_files:
        execute_sql_from_file(os.path.join("ddl", ddl_file), cursor)

    dml_files = [
        "../dml/users.sql",
        "../dml/categories.sql",
        "../dml/brands.sql",
        "../dml/products.sql",
        "../dml/orders.sql",
        "../dml/order_details.sql",
    ]
    for dml_file in dml_files:
        execute_sql_from_file(os.path.join("dml", dml_file), cursor)

    # Indexの各SQLファイルを実行
    index_files = [
        "../index/users_index.sql",
        "../index/orders_index.sql",
        "../index/products_index.sql",
    ]
    for index_file in index_files:
        execute_sql_from_file(os.path.join("index", index_file), cursor)

    # コミットと接続解除
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    create_shoes_ec_db()
