"""
    DB接続:sqlite3
    
    python -u "/Applications/MAMP/htdocs/Python系/DB/main.py"
    cd Applications/MAMP/htdocs/Python系/DB

    select * from persons;
    .table
    .exit

"""
import sqlite3

# 接続 DBが存在していなければ作成される
connect = sqlite3.connect('test_sqlite.db')
# connect = sqlite3.connect(':memory:')

# DBに対するオブジェクト
cursor = connect.cursor()

# # 実行(table作成)
# cursor.execute(
#     'Create table persons(id integer primary key autoincrement ,name string)'
# )
# # 実行(データ作成)
# cursor.execute(
#     'insert into persons(name) values("masato")'
# )
# # 実行(データ作成)
# cursor.execute(
#     'insert into persons(name) values("mai")'
# )
# # 実行(データ作成)
# cursor.execute(
#     'insert into persons(name) values("kana")'
# )
# )
# 実行(データ更新)
# cursor.execute(
#     'update persons set name = "MMMMMMMMM" where id = 3'
# )
# コミット
# connect.commit()

# 実行(データ削除)
# cursor.execute(
#     'delete from persons where id = 3'
# )
# コミット
# connect.commit()

# 検索
cursor.execute(
    'select * from persons;'
)
print(cursor.fetchall())


# 切断
cursor.close()
connect.close()
