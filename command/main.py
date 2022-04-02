# coding=utf-8
import subprocess

# 変数定義
USER = 'test_user'
PASS = 'test_pw'


def commandRun():
    try:
        res = subprocess.call('ls')
        print(res)
        subprocess.check_output('ls')
        print(res)

    except:
        print("Error.")


if __name__ == '__main__':
    # main()
    commandRun()
    # input("何かキーを押すと終了します")
