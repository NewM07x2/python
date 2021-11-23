"""
REST

HTTPメソッド クライアントが行いたい処理をサーバに伝達する

GET   ： データの参照
POST  ： データの新規登録
PUT   ： データの更新
DELETE： データの削除

https://httpbin.org/get
{
  "args": {}, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
    "Accept-Encoding": "gzip, deflate, br", 
    "Accept-Language": "ja,en-US;q=0.9,en;q=0.8", 
    "Host": "httpbin.org", 
    "Sec-Fetch-Dest": "document", 
    "Sec-Fetch-Mode": "navigate", 
    "Sec-Fetch-Site": "none", 
    "Sec-Fetch-User": "?1", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-5f588bfc-b5c2f9ca388ad691bad1a715"
  }, 
  "origin": "111.239.171.158", 
  "url": "https://httpbin.org/get"
}

"""
import urllib.request
import json  # httpからのresをjson形式で判断する

url_get = 'https://httpbin.org/get'
# urlにアクセスする
with urllib.request.urlopen(url_get) as url_files:
    url_file = url_files.read().decode('utf-8')
    # json形式で読み込んでやる。pythonのdic型
    url_file_json = json.loads(url_file)
    print(url_file_json)

# URLにパラメータを付与してやる場合
# payload = {'key1': 'value1', 'key2': 'value2'}
# url = 'https://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
# print(url)  # 結果：https://httpbin.org/get?key1=value1&key2=value2

# POSTでデータを送信する場合、データを加工する必要がある。
url_post = 'https://httpbin.org/post'
payload = {'key1': 'value1', 'key2': 'value2'}
payload = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    url_post,
    data=payload,
    method='POST'
)

with urllib.request.urlopen(req) as url_files:
    url_file = url_files.read().decode('utf-8')
    # json形式で読み込んでやる。pythonのdic型
    url_file_json = json.loads(url_file)
    print(url_file_json)
