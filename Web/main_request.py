"""
サードパーティのリクエスト

"""

import requests
url_post = 'https://httpbin.org/post'
url_get = 'https://httpbin.org/get'

payload = {'key1': 'value1', 'key2': 'value2'}

# GET
req = requests.get(url_get, params=payload, timeout=1)
print(req.status_code)
print(req.text)
print(req.json())

# POST
req = requests.post(url_post, data=payload)
print(req.status_code)
print(req.text)
print(req.json())
