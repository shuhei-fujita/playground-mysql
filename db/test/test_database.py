import os
import sys

import pymysql
from dotenv import load_dotenv
from prettytable import PrettyTable

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


def log_test_result(table, test_case, table_name, expected, actual):
    status = "Passed" if expected == actual else "Failed"
    table.add_row([test_case, table_name, expected, actual, status])


def test_tables():
    connection = None
    try:
        connection = pymysql.connect(
            host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, port=MYSQL_PORT
        )
        cursor = connection.cursor()
        cursor.execute("USE {}".format(MYSQL_DB_NAME))

        # Set up the table
        print("Testing Results: Table Data")
        table = PrettyTable()
        table.field_names = ["Test Case", "Table", "Test Data", "Actual", "Result"]

        # Test for username shuhei
        cursor.execute("SELECT username FROM users WHERE email='shuhei@example.com'")
        user = cursor.fetchone()
        log_test_result(table, "Username Check for shuhei", "users", "shuheii", user[0])

        # Test for username shuheiii (even if it's expected to fail)
        cursor.execute("SELECT username FROM users WHERE email='shuhei@example.com'")
        user = cursor.fetchone()
        log_test_result(
            table, "Username Check for shuheiii", "users", "shuheiii", user[0]
        )

        # Test for username user2
        cursor.execute("SELECT username FROM users WHERE email='user2@example.com'")
        user = cursor.fetchone()
        log_test_result(table, "Username Check for user2", "users", "user2", user[0])

        # Test for product name
        cursor.execute("SELECT name FROM products WHERE price=150.00")
        product = cursor.fetchone()
        log_test_result(table, "Product Name Check", "products", "Air Max", product[0])

        # Test for brand name
        cursor.execute("SELECT name FROM brands WHERE id=1")
        brand = cursor.fetchone()
        log_test_result(table, "Brand Name Check", "brands", "Nike", brand[0])

        # Test for category name
        cursor.execute("SELECT name FROM categories WHERE id=1")
        category = cursor.fetchone()
        log_test_result(
            table, "Category Name Check", "categories", "Sneakers", category[0]
        )

        print(table)

    except pymysql.MySQLError as e:
        print(f"An error occurred: {e}")

    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    test_tables()
