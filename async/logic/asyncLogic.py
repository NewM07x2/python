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
from bitarray import test

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
    print('asyncProcessTest1 end', index)


async def asyncProcessTest2(event, index):
    index = 2
    await event.wait()
    print('asyncProcessTest2 start', index)
    await asyncio.sleep(index)
    print('asyncProcessTest2 end', index)


async def asyncProcessTest3(event, index):
    index = 3
    print('asyncProcessTest3 start', index)
    await asyncio.sleep(index)
    print('asyncProcessTest3 end', index)
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

# --------------------------------------------------------------------------------
# asyncio.queue
# 同時にタスクを走らせて、一方でキューにデータを格納し、他方でその値を仕様する方法
# 複数使用することはできないので、その場合はeventなどを用いて発火のタイミングを指定する必要がある。
# --------------------------------------------------------------------------------


async def test1(queue, event):
    index = 1
    print('test1 start')
    x = 100
    await queue.put(x)
    # await asyncio.sleep(index)
    print('test1 end', x)


async def test2(queue, event):
    index = 2
    print('test2 start')
    x = await queue.get()
    await asyncio.sleep(index)
    x = x + 100
    await queue.put(x)
    print('test2 end', x)
    event.set()


async def test3(queue, event):
    index = 3
    await event.wait()
    print('test3 start')
    x = await queue.get()
    await asyncio.sleep(index)
    x = x + 100
    print('test3 end', x)


def sampleAsyncQueue():
    index = 0
    queue = asyncio.Queue()
    event = asyncio.Event()
    asyncLoop2 = asyncio.get_event_loop()
    asyncLoop2.run_until_complete(asyncio.wait(
        [
            test1(queue, event),
            test2(queue, event),
            test3(queue, event)
        ]
    ))
    asyncLoop2.close()

# --------------------------------------------------------------------------------
# Future
# asyncio.Future()
# Futureオブジェクトを生成し、そのオブジェクトが非同期関数で終了したかを判断する。
# --------------------------------------------------------------------------------


async def test(future):
    print('test start')
    await asyncio.sleep(2)
    future.set_result('future finish!!!')
    print('test end')


async def sampleAsyncFuture():
    # loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(test(future))
    # loop.run_until_complete(future)
    print(future.result())
    # loop.close()

# --------------------------------------------------------------------------------
# コルーチンのチェーン
# --------------------------------------------------------------------------------


async def compute(x, y):
    # computeはprint_sumのタスクとして配置
    # 結果を返却する。
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(2)
    return x + y


async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))


def sampleAsyncTask():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_sum(1, 2))
    loop.close()


# --------------------------------------------------------------------------------
# sample
# --------------------------------------------------------------------------------
Seconds = {
    'frist': 1,
    'second': 2,
    'third': 3
}


async def work1():
    for key, value in Seconds.items():
        print(key, value)
        await asyncio.sleep(value)


async def work2():
    for key, value in Seconds.items():
        print(key, value)
        await asyncio.sleep(value)


async def sampleAsync():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([
        # work1(),
        # work2()
        sampleSingleAsync()
    ]))
    loop.close()


async def sampleSingleAsync():
    await asyncio.sleep(3)
    print("OK")
