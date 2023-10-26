#!/bin/bash

# .envファイルから環境変数を読み込む
source .env

# 出力の見出しを表示する関数
print_header() {
    echo "$1"
    echo " "
}

# データベースが存在するか確認
# `grep -o` を使用して特定の文字列だけを取得
# DB_EXISTS=$(mysql --defaults-extra-file=~/.my.cnf -h ${MYSQL_HOST} -P ${MYSQL_PORT} -u ${MYSQL_USER} -e "SHOW DATABASES LIKE '${MYSQL_DB_NAME}';" 2>/dev/null | grep -o ${MYSQL_DB_NAME})
DB_EXISTS=$(mysql -h ${MYSQL_HOST} -P ${MYSQL_PORT} -u ${MYSQL_USER} -e "SHOW DATABASES LIKE '${MYSQL_DB_NAME}';" 2>/dev/null | grep -o ${MYSQL_DB_NAME})
# テーブルが存在するか確認
# TABLE_EXISTS=$(mysql --defaults-extra-file=~/.my.cnf -h ${MYSQL_HOST} -P ${MYSQL_PORT} -u ${MYSQL_USER} -e "SHOW TABLES FROM ${MYSQL_DB_NAME} LIKE 'users_table';" 2>/dev/null | grep -o 'users_table')
TABLE_EXISTS=$(mysql -h ${MYSQL_HOST} -P ${MYSQL_PORT} -u ${MYSQL_USER} -e "SHOW TABLES FROM ${MYSQL_DB_NAME} LIKE 'users_table';" 2>/dev/null | grep -o 'users_table')

print_header "Initializing Database"

# データベースが存在しない場合、作成
# `[ -z "$VAR" ]` は `$VAR` が空（つまり存在しない）場合にTrue
# if [[ "$DB_EXISTS" == "my_database" ]]; then
if [ -z "$DB_EXISTS" ]; then
    print_header "Creating database ${MYSQL_DB_NAME}"
    mysql -h ${MYSQL_HOST} -P ${MYSQL_PORT} -u ${MYSQL_USER} -t < ./ddl/create-database.sql
else
    echo "Database ${MYSQL_DB_NAME} already exists."  
fi
mysql -h ${MYSQL_HOST} -P ${MYSQL_PORT} -u ${MYSQL_USER} -t < ./dml/show-database.sql

# テーブルが存在しない場合、作成
# `[ -z "$VAR" ]` は `$VAR` が空（つまり存在しない）場合にTrue
# if [[ "$TABLE_EXISTS" == "users_table" ]]; then
if [ -z "$TABLE_EXISTS" ]; then
    print_header "Creating tables in database ${MYSQL_DB_NAME}"
    mysql -h ${MYSQL_HOST} -P ${MYSQL_PORT} -u ${MYSQL_USER} ${MYSQL_DB_NAME} -t < ./ddl/create-tables.sql
else
    echo "Table users_table already exists."
fi
mysql -h ${MYSQL_HOST} -P ${MYSQL_PORT} -u ${MYSQL_USER} ${MYSQL_DB_NAME} -t < ./dml/show-tables.sql
