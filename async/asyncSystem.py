"""
ここでは非同期で返り値なしの投げっぱなし処理を記載する。
構築方法はasyncSystemを例に

"""
import asyncio
import time

# 変数
list = {
    2: 'second',
    4: 'four',
    6: 'six'
}


def asyncProcess(num, str, times):
    """ここには返り値がない処理を記載する。"""
    print("asyncProcess : start")
    # ここに処理を記載------
    time.sleep(num)
    # -------------------
    print("asyncProcess : finish", str+"s stop")
    print("--- %s seconds ---" % (time.time() - times))


def asyncSystem():
    # ローカル変数
    times = time.time()

    # 非同期変数
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    """ここに非同期化したい関数を記載していく。"""
    # loop.run_in_executor(None, "関数名", "引数")
    loop.run_in_executor(None, asyncProcess, 1, "test")
    for key, value in list.items():
        loop.run_in_executor(None, asyncProcess, key, value, times)


if __name__ == "__main__":
    print('---■ 処理開始 ■---')
    # 非同期処理呼び出し
    asyncSystem()
    print('---■ 処理終了 ■---')
