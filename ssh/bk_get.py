# imoport
import paramiko
import os
import datetime
import csv

# 変数
host = '---★★★ IP ★★★---'
port = '---★★★ port ★★★---'
username = '---★★★ username ★★★---'
password = '---★★★ password ★★★---'
tmp = 'tmp/'
folders = [
    # '20210426_SAGYO-1187', '---★★★ 取得したいフォルダの指定 ★★★---'
    '20210426_SAGYO-1187',
]


def main():
    with paramiko.SSHClient() as ssh:
        #インスタンスを生成
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=port, username=username, password=password)

        for folder in folders:
            Files = []
            makeFolder(folder)
            stdin, stdout, stderr = ssh.exec_command('cd ../../../' + tmp + folder + ';ls')
            for value in stdout:

                # 実行結果を表示
                try:
                    File = value.rstrip()
                    print('取得対象フォルダ:', folder)
                    print('取得対象ファイル:', File)
                    print('---■ SFTPセッション開始 ■---')
                    # SFTPセッション開始
                    sftp_connection = ssh.open_sftp()

                    # リモートサーバーからローカルPCへファイルを転送
                    print('・・・処理中・・・')
                    sftp_connection.get('../../../' + tmp + folder + '/' + File, folder + '/' + File)

                except Exception as e:
                    print('Exception')
                    print(e.args)

                finally:
                    print('---■ SFTPセッション終了 ■---')
            return True
        return False

def makeFolder(folder):
    if not os.path.isdir(folder):
        os.makedirs(folder)

if __name__ == '__main__':
    print('---■ 処理開始 ■---')
    result = main()
    print('---■ 処理終了 ■---')
