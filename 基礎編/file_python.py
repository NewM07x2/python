"""
    ファイルに書き込んでいく
    ファイルは開いたら閉じること。
    w：書き込み
    r：読み込み
    a：追加
"""
# f = open('test.txt', 'w')
# f.write('123\n')
# print('My', 'name', 'is', 'Masato', sep=' ', end='!', file=f)
# f.close()

"""
    ファイルに書き込んでいく
    closeし忘れた場合,
    withを用いればOK
# """
# with open('test2.txt', 'w') as f:
#     f.write('123\n')
#     print('My', 'name', 'is', 'Masato2', sep=' ', end='!', file=f)

"""
    ファイルを読み込んでいく
    test2.txtを読み込んでいく
"""
# with open('test2.txt', 'r') as f_read:
# # 一気に酔込み
# result = f_read.read()
# print(result)

# １行づつ読み込んでいく
# while True:
#     line = f_read.readline()  # 1行読み込み
#     print(line , end='')
#     if not line:  # 行がなくなった場合、break
#         break

"""
    seekを使って読み込んでいく
    文字指定で読み込みができる
"""

# with open('test2.txt', 'r') as f_read:
#     print(f_read.tell())


"""
    読みこんで書き込んでいく
"""

# with open('test2.txt', 'w+') as f:
#     f.write('test')
#     f.seek(0)  # 書き込みにより最後はD後の開業になっているため,Seekで０番目に戻る必要がある。
#     print(f.read())

"""
    読み込んで書き込んでいく
"""

# with open('test2.txt', 'r+') as f:
#     print(f.read())
#     f.write('test')
#     f.seek(0)  # 書き込みにより最後はD後の開業になっているため,Seekで０番目に戻る必要がある。
#     print(f.read())

"""
    テンプレート
"""

# import string
# tmp_str = """\
# Hi! $name

# $contents

# さようなら！！！
# """
# t = string.Template(tmp_str)
# contents = t.substitute(name=123, contents='またね！')
# with open('test３.txt', 'w') as f:
#     f.write(contents)


"""
    CSVファイルの読み込み
"""
# 書き込み
# import csv
# with open('test.csv', 'w') as csv_file:
#     fieldnames = ['Name', 'Count']
#     writer = csv.DictWriter(csv_file, fieldnames)
#     writer.writeheader()
#     writer.writerow({'Name': '新田', 'Count': 3})
#     writer.writerow({'Name': '新田2', 'Count': 4})

# with open('test.csv', 'r') as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         print(row['Name'], row['Count'])
#         print(row['Name'], row['Count'])

"""
    添付ファイルからcsvのデータを用いてデータを加工する（練習）
"""
# with open('crm_point.csv', 'w') as csv_file:
#     headernames = ['customer', 'id', 'dt']
#     writer = csv.DictWriter(csv_file, headernames)
#     writer.writeheader()
#     writer.writerow({'customer': '10001', 'id': 1, 'dt':'2020-08-01 23:59:59'})
#     writer.writerow({'customer': '10002', 'id': 2, 'dt': '2020-08-02 23:59:59'})


# import string
# import csv
# with open('crm_point.csv', 'r') as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         list = row

#         with open('tmp_insert.txt', 'r') as insert_file:
#             t = string.Template(insert_file.read())

#             contents = t.substitute(
#                 customer=list['customer'],
#                 id=list['id'],
#                 dt=list['dt'],
#                 reason_id=list['reason_id'],
#                 reason_name=list['reason_name'],
#                 point=list['point'],
#                 point_in=list['point_in'],
#                 goods=list['goods'],
#                 name=list['name'],
#                 qty=list['qty'],
#                 remarks=list['remarks'],
#                 rgdt=list['rgdt'],
#                 updt=list['updt'],
#                 upuser=list['upuser'],
#                 point_calc_dt=list['point_calc_dt']
#             )
#         with open('test３.txt', 'a') as f:
#             f.write(contents)

"""
    ファイルを圧縮して解凍する(tarfile)
"""
# まずはライブラリをimport

# 圧縮
# with tarfile.open('test.tar.gz', 'w:gz') as tr:  # tarfile.open('圧縮したいフォルダ名','w:gz')
#     tr.add('test') # 圧縮したいフォルダ名を指定

# 解凍
# import tarfile
# with tarfile.open('test.tar.gz', 'r:gz') as tr:
#     tr.extractall(path='testtest')  # 解凍先のフォルダを指定

"""
    ファイルを圧縮して解凍する(zipfile)
"""

# import zipfile
# import glob
# with zipfile.ZipFile('test.zip', 'w') as z:
#     # z.write('zip')  # フォルダしか作っていない状態のため、圧縮したいファイルを指定する必要がある
#     # z.write('zip/zip.txt')

#     # zipファイル配下の全てのファイルを圧縮していく。その際に＊が2ついることに注目
#     for f in glob.glob('zip/**', recursive=True):
#         z.write(f)

#     # zipファイルの読み込み
# with zipfile.ZipFile('test.zip', 'r') as z:
#     # z.extractall('testtesttest111')  # extractallで指定した名前で展開していく

"""
    tempile (一時的なデータ)
"""
# import tempfile
# # 一時的なファイルの作成：終了時に削除される。
# with tempfile.TemporaryFile(mode= 'w+' ) as t:
#     t.write('テスト開発')
#     t.seek(0)
#     print(t.read())

# # 永続的に添付ファイルを作成する
# with tempfile.NamedTemporaryFile(delete=False) as t:
#     with open(t.name, 'w+') as f:
#         print(t.name)
#         f.write('test123\n')
#         f.seek(0)
#         print(f.read())

"""
    subprocessでコマンドを実行していく。いつもターミナルで行っていたことをおこなっていく
"""
# import subprocess
# subprocess.run(['ls','-al'])

"""
    datetime
"""
# import datetime
# now = datetime.datetime.now()
# print(now)
# print(now.isoformat())  # 国際ISOフォーマット
# print(now.strftime('%Y/%m/%d'))  # strftimeを用いることで、フォーマットを変更することができる。
# print('--------------------------')
# # 日付のみ
# today = datetime.date.today()
# print(today)
# print(today.isoformat())
# print(today.strftime('%d/%m/%Y'))
# print('--------------------------')
# # 自分で日付を作成して表示させる
# time = datetime.time(hour=9, minute=42, second=00, microsecond=000)
# print(time)
# print(time.isoformat())
# print('--------------------------')
# # 1年前などの日付操作
# # ...     days = 50,
# # ...     seconds = 27,
# # ...     microseconds = 10,
# # ...     milliseconds = 29000,
# # ...     minutes = 5,
# # ...     hours = 8,
# # ...     weeks = 2
# #1年前は365日前としてやればOK
# print(now)
# d = datetime.timedelta(hours = 8)
# print(now - d)

# print('--------------------------')

# import time
# print('#######')
# time.sleep(5) # ５S後に後述を表示させる
# print('#######')

"""
    bkファイルを作成していく
"""
# import os
# import datetime
# import shutil

# now = datetime.datetime.now()
# file_name = 'test.txt'
# if os.path.exists(file_name):
#     shutil.copy(file_name, "{}.{}".format(file_name, now.strftime('%Y%m%d.%H%M%S')))

# with open(file_name, 'w') as g:
#     g.write('testtest')
