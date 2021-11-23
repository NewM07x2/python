# coding=utf-8
"""
BeautifulSoupを用いたスクレイピング方法

"""
# standard
import os
import sys
import json
import abc
import datetime
import shutil
import collections
import csv
import abc
import string
import tarfile
import zipfile
import glob
import tempfile
import time
import pandas as pd
from collections import defaultdict

# web
import urllib.request as req
import requests
import http.server
import socket
import socketserver
from selenium import webdriver
from bs4 import BeautifulSoup

# DB
import sqlite3
# import mysql.connector
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm
from sqlalchemy import engine

# pkg
from common import common

# 変数宣言
url = 'https://www.python.org'

# まずHTML情報の取得
html = requests.get(url)

# BeautifulSoupの形式に変換
soup = BeautifulSoup(html.text, 'lxml')

# タイトルタグの情報を取得
titles = soup.find_all('title')
a = [] 
a = soup.find_all('a')
# print(titles[0].text)
print(a[0:5])
for v in a[0:5]:
    print(v.text)
    print(v.attrs['href'])
intro = soup.find_all('div', {'class': 'introduction'})
# print(intro)
# print('@@@@@@@@')
# print(intro[0].text)

