import paramiko
import os
import datetime
import csv

# 変数
host = '172.20.40.50'
port = 22
username = 'nittam93'
password = 'nittam93'
tmp = 'tmp/'
folders = [
    # '20210426_SAGYO-1181',
    # '20210426_SAGYO-1187',
]
local = 'C:\\'


def main():
    with paramiko.SSHClient() as ssh:
        #インスタンスを生成
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=port, username=username, password=password)
        # 実行結果を表示
        try:
            print('---■ SFTPセッション開始 ■---')
            # SFTPセッション開始
            sftp_connection = ssh.open_sftp()

            # リモートサーバーからローカルPCへファイルを転送
            print('・・・処理中・・・')
            sftp_connection.get('/tmp/test.txt', 'C:\\Users\\DUKeDev0044\\Desktop\\test.txt')

        except Exception as e:
            print('Exception')
            print(e.args)

        finally:
            print('---■ SFTPセッション終了 ■---')

def makeFolder(folder):
    if not os.path.isdir(folder):
        os.makedirs(folder)


if __name__ == '__main__':
    print('---■ 処理開始 ■---')
    result = main()
    print('---■ 処理終了 ■---')
