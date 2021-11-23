# standard
import os
import sys
import json
import abc
import datetime
import shutil
import collections
import tracemalloc
import csv
import abc
import string
import tarfile
import zipfile
import glob
import tempfile
import builtins
from collections import defaultdict

# web
import urllib.request
import requests
import http.server
import socket
import socketserver

# pkg
from common import common


# 親クラス
class sampleParent(object):

    # クラス変数
    name = 'name'

    def __init__(self, name=None):
        self.name = name
        print(self.name)

    def say(self):
        print('sampleParent!')


# 子クラス
class sampleChild(sampleParent):
    # コンストラクタ（初期化）
    def __init__(self, name='masato'):
        # クラス変数
        self.name = name
        print(self.name)
    
    # デストラクタ（終期化）
    # def __del__(self):
    #     print('処理を終了します。: {name}'.format(name = self.name))
    # def say(self):
    #     print('sampleChild!')


# 子クラス2
class sampleChild2(sampleParent):
    def __init__(self, name='masato2', status=False):
        # 親要素のコンストラクタを呼び出し
        super().__init__(name)
        # 子で独自の変数を定義
        self.name = name 
        self._status = status  # 子で独自の変数を定義
    
    @property
    def getStatus(self):
        return self._status

    @property
    def setStatus(self, status):
        self._status = status

    def say(self):
        print('sampleChild2!')

# 抽象クラス


class abstractClass(object, metaclass=abc.ABCMeta):
    def __init__(self, test):
        self.test = test
    
    @abc.abstractmethod
    def testMethod(self):
        print('抽象クラス')


class testClass(abstractClass):
    def __init__(self, test):
        self.test = test
    
    def testMethod(self):
        print('継承しました。')


# オブジェクトの生成
sampleParentObject = sampleParent()
print('******')
sampleChildObject = sampleChild('nitta')
print('******')
sampleChildObject2 = sampleChild2('nitta2', True)
sampleChildObject2._status = 123
print(sampleChildObject2._status)
# 実行
# sample1.say()  # masato
# sample2.say()  # nitta

test = testClass('test')
test.testMethod()
