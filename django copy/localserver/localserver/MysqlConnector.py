# coding:utf-8
import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'port': 8889,
    'database': 'python',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cursor = cnx.cursor(dictionary=True)

# SQL
sql = 'SELECT user_id,user_email FROM user'

# 実行
cursor.execute(sql)

# コミット
# cursor.commit()

# 取得
results = cursor.fetchall()

for row in results:
    user_id = row['user_id']
    user_email = row['user_email']
    print(user_id, user_email)

cnx.close()