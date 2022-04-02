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
from logic import logic
import sys

def main():
    print('---■ 処理開始 ■---')
    logic.sampleMultiProcessing()
    print('---■ 処理終了 ■---')

if __name__ == '__main__':
    main()
    # input("何かキーを押すと終了します")
