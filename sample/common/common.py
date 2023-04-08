'''
    共通処理記載

'''
# 初期化

# DB接続処理
import mysql.connector
config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'port': 8889,
    'database': 'python',
    'raise_on_warnings': True
}
def connectMySQL():
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(dictionary=True)
        cursor.execute('SELECT * FROM `user`')
        results = cursor.fetchall()
        for row in results:
            user_id = row['user_id']
            user_name = row['user_name1'] + row['user_name2']
            print(user_id)
            print(user_name)
        cnx.close()
    except Exception as e:
        print(f"Error Occurred: {e}")

# 文字コード変換処理

# ファイル読込処理

# ファイル書込処理

# Json読込処理

# 非同期処理

# 暗号化処理

# API通信

# SSH通信
