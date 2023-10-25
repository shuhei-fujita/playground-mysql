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

def clean_test_data():
    # データベース接続
    connection = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, db=MYSQL_DB_NAME)
    cursor = connection.cursor()
    
    # テーブルデータのクリーンアップ
    cursor.execute("DELETE FROM order_details")
    cursor.execute("DELETE FROM orders")
    cursor.execute("DELETE FROM users")
    cursor.execute("DELETE FROM products")
    cursor.execute("DELETE FROM brands")
    cursor.execute("DELETE FROM categories")

    # 接続を閉じる
    connection.close()
    print("Finished cleaning up test data")

if __name__ == "__main__":
    clean_test_data()
