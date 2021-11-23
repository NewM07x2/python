# クラスの定義 objectを書いておくことでbaseとすることができる。→継承で区別するため。
"""
selfは関数内で自信を差す変数。

"""
import abc


class test(object):
    # クラスの初期化とクラス変数
    # __init__ とすることで、初期設定が可能
    def __init__(self, name):
        print('初期読み込みを行います。')
        self.name = name
        print(self.name, 'って呼びました')

    def say(self):
        print('こんにちわ！')

    # __del__は最後に読み込む
    def __del__(self):
        print('処理を終了していました。')


# オブジェクトを生成
test = test('まさと')  # コンストラクタの役割
# test.say(

