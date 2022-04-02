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




