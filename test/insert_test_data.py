import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

# .env ファイルから接続情報を取得
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PORT = int(os.getenv('MYSQL_PORT'))
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DB_NAME = os.getenv('MYSQL_DB_NAME')

def execute_single_statement(statement, cursor):
    if not statement.strip():
        return
    try:
        cursor.execute(statement)
    except pymysql.MySQLError as e:
        print(f"エラーが発生しました: {e}")

def execute_sql_from_file(filename, cursor):
    with open(filename, 'r') as file:
        sql_statements = file.read().split(';')
    for statement in sql_statements:
        execute_single_statement(statement, cursor)

def create_shoes_ec_db():
    connection = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER)
    cursor = connection.cursor()

    # データベースを作成
    cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(MYSQL_DB_NAME))
    
    # 新しく作成したデータベースに接続
    cursor.execute("USE {}".format(MYSQL_DB_NAME))

    # DDLの各SQLファイルを実行
    ddl_files = [
        "users.sql",
        "brands.sql",
        "categories.sql",
        "products.sql",
        "orders.sql",
        "order_details.sql"
    ]

    for ddl_file in ddl_files:
        execute_sql_from_file(os.path.join("ddl", ddl_file), cursor)

    
    dml_files = [
        "users.sql",
        "categories.sql",
        "brands.sql",
        "products.sql",
        "orders.sql",
        "order_details.sql"
    ]

    for dml_file in dml_files:
        execute_sql_from_file(os.path.join("dml", dml_file), cursor)

    # Indexの各SQLファイルを実行
    index_files = [
        "users_index.sql",
        "orders_index.sql",
        "products_index.sql"
    ]

    for index_file in index_files:
        execute_sql_from_file(os.path.join("index", index_file), cursor)

    # コミットと接続解除
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    create_shoes_ec_db()
