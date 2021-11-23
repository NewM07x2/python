import paramiko
import os
import datetime
import csv
import sys

# 変数
host = '172.20.40.50'
port = 22
tmp = 'tmp/'
folders = []


def main(folder, username, password):
    with paramiko.SSHClient() as ssh:
        #インスタンスを生成
        try:
            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, port=port, username=username, password=password)
        except Exception as e:
            print('エラー発生。ID もしくは PW が間違ってるで。')
            return False

        stdin, stdout, stderr = ssh.exec_command('cd ../../../' + tmp + folder + ';ls')
        for value in stderr:
            print('エラー発生。たぶんそんなファイル無いで ：' + folder)
            return False
        # for value in stdin:
        #     print(value)
        Files = []
        makeFolder(folder)
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
                return False
            finally:
                print('---■ SFTPセッション終了 ■---')
        return True
    return False

def makeFolder(folder):
    if not os.path.isdir(folder):
        os.makedirs(folder)


if __name__ == '__main__':
    print('---■ 処理開始 ■---')
    # args = sys.argv
    # if len(args) <= 1:
    #     print('取得対象フォルダを指定して下さい。')
    # else:
    #     result = main(args[1])
    print('172.20.40.50 に接続します。')
    ID = input("ID : ")
    PW = input("PW : ")
    value = input("取得対象フォルダ : ")
    if value == '':
        print('取得対象フォルダを指定して下さい。')
    else:
        result = main(value, ID, PW)
    print('---■ 処理終了 ■---')
    input("何かキーを押すと終了します")
