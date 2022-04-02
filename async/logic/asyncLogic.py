'''
    処理仕様ロジック
'''
# standard
from collections import defaultdict
from concurrent.futures import thread
import multiprocessing
import threading
import time
import asyncio
from tkinter import Y

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
    # 通常処理
    # print('---------------------------')
    # stop(2)

    # マルチスレッド処理
    # print('--マルチスレッド処理--')
    # t1 = threading.Thread(target=stop)
    # t2 = threading.Thread(target=stop)
    # t1.start()
    # t2.start()

    # マルチプロセス処理
    # print('--マルチプロセス処理--')
    # p1 = multiprocessing.Process(target=stop)
    # p2 = multiprocessing.Process(target=stop)
    # p1.start()
    # p2.start()

    # 非同期処理
    print('--非同期処理--')
    asyncLoop = asyncio.get_event_loop()
    # asyncLoop.run_until_complete(asyncio.wait([asyncTest(), asyncTest()]))
    # この書き方は指定した関数が全て完了するまで待機する
    asyncLoop.run_until_complete(asyncio.wait(
        [
            # 非同期処理させたいfunctionを指定
            asyncProcessTest(), 
            asyncProcessTest()
        ]
    ))
    asyncLoop.close()


def stop():
    print('start')
    # 数秒間停止
    print('processing...')
    time.sleep(5)
    # print('{time}秒間停止しました。'.format(time=index))
    print('stop')

# この記載方法はpython3.5以前までの形


@asyncio.coroutine
def asyncTest():
    print('start')
    print('processing...')
    yield from asyncio.sleep(2)
    print('stop')


# python3.6以降
async def asyncProcessTest():
    print('start')
    print('processing...')
    await asyncio.sleep(2)
    print('stop')
