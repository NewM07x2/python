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


def main():
    print('---■ 処理開始 ■---')
    # asyncLogic.sampleMultiProcessing()
    # asyncLogic.SynchronousProcessing()
    # asyncio.run(asyncLogic.asyncProcess2())
    # asyncLogic.sampleasyncProcess2()
    asyncLogic.sampleasyncProcess3()
    print('---■ 処理終了 ■---')


def commandRun():
    try:
        # res = subprocess.check_call('dummy')
        # print(res)
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
