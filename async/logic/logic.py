'''
    処理仕様ロジック
'''
# standard
from collections import defaultdict
import multiprocessing
import time

from common import common
from logic import logic
from model import model
import sys

# サンプルロジック


def sampleLogic():
    print('sampleLogic開始')
    model.sampleModel()
    print('sampleLogic終了')


# 非同期処理
def asyncSampleLogic():
    print('---------------------------')
    print('sampleLogic開始')
    print('sampleLogic終了')


def sampleMultiProcessing():
    # マルチスレッド処理
    print('---------------------------')
    print('sampleLogic開始')
    print('sampleLogic終了')
