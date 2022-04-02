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

from gevent import wait
import aiohttp
import requests

from common import common
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
            # asyncHttpRequestProcess(),
            # asyncProcess2()
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


# 非同期HTTPリクエスト
async def asyncHttpRequestProcess():
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        # pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'
        # async with session.get(pokemon_url) as resp:
        #     pokemon = await resp.json()
        #     print(pokemon['name'])
        for number in range(1, 25):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()
                print('asyncHttpRequestProcess', pokemon['name'])
    print("--- %s seconds ---" % (time.time() - start_time))


def SynchronousProcessing():
    # 同期処理
    start_time = time.time()
    for number in range(1, 25):
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'
        resp = requests.get(url)
        pokemon = resp.json()
        print(number, pokemon['name'])
    print("--- %s seconds ---" % (time.time() - start_time))


async def asyncProcess2():
    # 非同期処理書き方その２
    start_time = time.time()
    async with aiohttp.ClientSession() as session:

        for number in range(1, 25):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()
                print('asyncProcess2', pokemon['name'])

    print("--- %s seconds ---" % (time.time() - start_time))

# --------------------------------------------------------------------------------
# 非同期平行処理時に一方のプロセスを占有する
# --------------------------------------------------------------------------------


async def asyncProcessTest1(lock):
    print('asyncProcessTest1 start')
    async with lock:
        await asyncio.sleep(2)
    print('asyncProcessTest1 end')


async def asyncProcessTest2(lock):
    print('asyncProcessTest2 start')
    async with lock:
        await asyncio.sleep(2)
    print('asyncProcessTest2 end')


async def asyncProcessTest3(lock):
    print('asyncProcessTest3 start')
    async with lock:
        await asyncio.sleep(2)
    print('asyncProcessTest3 end')


def sampleasyncProcess2():
    lock = asyncio.Lock()
    asyncLoop2 = asyncio.get_event_loop()
    asyncLoop2.run_until_complete(asyncio.wait(
        [
            asyncProcessTest1(lock),
            asyncProcessTest2(lock),
            asyncProcessTest3(lock)
        ]
    ))
    asyncLoop2.close()


# --------------------------------------------------------------------------------
# 非同期平行処理中提起したタイミングでイベントを発火させる
# --------------------------------------------------------------------------------
async def asyncProcessTest1(event, index):
    index = 1
    await event.wait()
    print('asyncProcessTest1 start', index)
    await asyncio.sleep(index)
    print('asyncProcessTest1 end',index)


async def asyncProcessTest2(event, index):
    index = 2
    await event.wait()
    print('asyncProcessTest2 start',index)
    await asyncio.sleep(index)
    print('asyncProcessTest2 end',index)


async def asyncProcessTest3(event, index):
    index = 3
    print('asyncProcessTest3 start',index)
    await asyncio.sleep(index)
    print('asyncProcessTest3 end',index)
    event.set()


def sampleasyncProcess2():
    index = 0
    event = asyncio.Event()
    asyncLoop2 = asyncio.get_event_loop()
    asyncLoop2.run_until_complete(asyncio.wait(
        [
            asyncProcessTest1(event, index),
            asyncProcessTest2(event, index),
            asyncProcessTest3(event, index)
        ]
    ))
    asyncLoop2.close()

# --------------------------------------------------------------------------------
# asyncio.condition
# condition.notify_all()で発火させたのち１つずつ処理を行っていく
# --------------------------------------------------------------------------------
async def asyncProcessTest1(condition, index):
    index = 1
    async with condition:
        await condition.wait()
        print('asyncProcessTest1 start', index)
        await asyncio.sleep(index)
        print('asyncProcessTest1 end', index)


async def asyncProcessTest2(condition, index):
    index = 2
    async with condition:
        await condition.wait()
        print('asyncProcessTest2 start', index)
        await asyncio.sleep(index)
        print('asyncProcessTest2 end', index)


async def asyncProcessTest3(condition, index):
    index = 3
    await asyncio.sleep(0)
    async with condition:
        print('asyncProcessTest3 start', index)
        await asyncio.sleep(index)
        print('asyncProcessTest3 end', index)
        condition.notify_all()


def sampleasyncProcess3():
    index = 0
    condition = asyncio.Condition()
    asyncLoop2 = asyncio.get_event_loop()
    asyncLoop2.run_until_complete(asyncio.wait(
        [
            asyncProcessTest1(condition, index),
            asyncProcessTest2(condition, index),
            asyncProcessTest3(condition, index)
        ]
    ))
    asyncLoop2.close()

