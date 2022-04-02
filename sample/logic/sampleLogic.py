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
from model import model
import sys

'''
    処理ロジック
'''
def sampleLogic():
    print('sampleLogic開始')
    model.sampleModel()
    print('sampleLogic終了')
