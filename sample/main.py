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
from pkg import commons

# a = 'a'
# print(f'a is {a}')
 
# x, y, z = 1, 2, 3
# print(f'a is {x}, {y}, {z}')
# print(f'a is {z}, {y}, {x}')
 
# name = 'Jun'
# family = 'Sakai'
# print(f'My name is {name} {family}. Watashi ha {family} {name}')

# x = {'a': 1}
# y = x.copy()
# y['a'] = 1000
# print(x)
# print(y)
# print(y['a'])


# count = 0
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print("終了")

# while True:
#     word = input("1 + 1 = ")
#     print(type(word))
#     if int(word) == 2:
#         break
#     print("next")

# list = ['test1', 'test2', 'test3', 'test4', 'test5']
# print(len(list))  # 8
# for index, item in enumerate(list):
#     print(index, item)

# days = ['Mon', 'Tue', 'Wed']
# eats = ['banana', 'apple', 'peach']
# for day, eat in zip(days, eats):
#     print(day, eat)

# 辞書型の取り出し
dic = {
    'x': 100,
    'y': 200
}
for index, value in dic.items():
    print(index, value)

# pkgのメソッドの呼び出し
commons.say()

ranking = {
    'A': 100,
    'B': 150,
    'C': 50,
}

print(sorted(ranking, key=ranking.get, reverse=True))
