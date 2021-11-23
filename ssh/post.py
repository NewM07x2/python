import paramiko
import os
import datetime
import csv
import glob

# 変数
host = '172.20.40.50'
port = 22
username = 'nittam93'
password = 'nittam93'

# 変更不可
tmp = '../../../tmp/'
local = 'C:\\pleiades\\workspace\\Python\\ssh\\post\\'
filePath = []
files = []

def main():
    with paramiko.SSHClient() as ssh:
        #インスタンスを生成
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=port, username=username, password=password)

        filePath = glob.glob(local + "*", recursive=True)
        for file in filePath:
            files.append(os.path.basename(file))
        for file in files:
            print(file)

        for file in files:
            try:
                print('UP対象ファイル:', file)
                print('---■ SFTPセッション開始 ■---')
                # SFTPセッション開始
                sftp_connection = ssh.open_sftp()
                # ローカルPCからリモートサーバーへファイルをアップロード
                print('・・・UpLoad中・・・')
                sftp_connection.put(local + file, tmp + file)
                print('・・・UpLoad完了・・・')
            except Exception as e:
                print('Exception')
                print(e.args)

            finally:
                print('---■ SFTPセッション終了 ■---')

if __name__ == '__main__':
    print('---■ 処理開始 ■---')
    result = main()
    print('---■ 処理終了 ■---')
