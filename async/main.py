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
import time
import asyncio
import aiohttp
import subprocess
from collections import defaultdict

# web
import urllib.request
import requests
import http.server
import socket
import socketserver

# pkg
from common import common
from logic import asyncLogic
import sys


async def test():
    print('start')
    await asyncio.sleep(1)
    print('end')


async def main():
    print('---■ 処理開始 ■---')
    # asyncLogic.sampleMultiProcessing()
    # asyncLogic.SynchronousProcessing()
    # asyncio.run(asyncLogic.asyncProcess2())
    # asyncLogic.sampleasyncProcess2()
    # asyncLogic.sampleasyncProcess3()
    # asyncLogic.sampleAsyncQueue()
    # asyncio.run(asyncLogic.sampleAsyncFuture())
    # asyncLogic.sampleAsyncTask()
    # asyncLogic.sampleAsync()

    asyncio.create_task(asyncLogic.sampleSingleAsync())
    await asyncio.sleep(5)
    print('---■ 処理終了 ■---')

if __name__ == '__main__':
    asyncio.run(main())
