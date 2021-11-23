"""
    seleniumを用いたWebスクレイピング

    登場関数
    webdriver.Chrome() : GoogleChromeを自動起動する
    mplicitly_wait(3) : 指定したドライバが見つかるまでの待ち時間を設定
    browser.get(url_login) : getで指定したURLに遷移することができる。
    browser.find_element_by_id('swpm_user_name'):指定したid属性のエレメント情報を取得する。
    browser.find_element_by_name('swpm-login'):指定したname属性のエレメント情報を取得する。
    click():クリックする。
    browser.find_element_by_xpath('XPATH') : 指定したXpathのエレメント情報を取得する。id,name,classがない場合

"""

# coding=utf-8
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

# 変数定義
USER = 'test_user'
PASS = 'test_pw'

# GoogleChromeを自動起動
browser = webdriver.Chrome()

# implicitly_waitは指定したドライバが見つかるまでの待ち時間を設定
browser.implicitly_wait(3)

# ページへ移動してログインを行う。
url_login = "http://kino-code.work/membership-login/"
browser.get(url_login) #getで指定したURLに遷移することができる。
time.sleep(3) #urlへ遷移する前に、下記処理に行かないよう一時停止にする。
print("ログインページにアクセスしました。")

# テキストボックスに値を入力していく
element = browser.find_element_by_id('swpm_user_name')
element.clear()
element.send_keys(USER)
element = browser.find_element_by_id('swpm_password')
element.clear()
element.send_keys(PASS)
print("フォームに値を送信しました。")

# 入力したデータでクリックする
browser_from = browser.find_element_by_name('swpm-login')
time.sleep(3)
browser_from.click()
print("ログインしました。")

# webサイトにアクセスを行う
url = 'https://kino-code.work/member-only/'
time.sleep(3)
browser.get(url)
print("指定したURLに遷移しました。")

# ダウンロードボタンをクリックする
frm = browser.find_element_by_xpath('/html/body/div/div[3]/div/main/article/div/p[2]/button')
time.sleep(1)
frm.click()
print("ダウンロードボタンをクリックしました。")
