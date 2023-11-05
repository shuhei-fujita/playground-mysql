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


def clean_test_data():
    # データベース接続
    connection = pymysql.connect(
        host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, port=MYSQL_PORT
    )
    cursor = connection.cursor()
    cursor.execute("USE {}".format(MYSQL_DB_NAME))

    # 外部キー制約を無効
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

    # テーブルデータのクリーンアップ
    cursor.execute("DROP TABLE IF EXISTS order_details")
    cursor.execute("DROP TABLE IF EXISTS orders")
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS products")
    cursor.execute("DROP TABLE IF EXISTS brands")
    cursor.execute("DROP TABLE IF EXISTS categories")

    # 外部キー制約を有効
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

    # 接続を閉じる
    connection.close()
    print("Finished cleaning up test data")


if __name__ == "__main__":
    clean_test_data()
