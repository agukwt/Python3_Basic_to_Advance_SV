#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
REST
HTTPメソッド クライアントが行いたい処理をサーバ伝える

GET     データの参照
POST    データの新規登録
PUT     データの更新
DELETE  データの削除
"""
# GET
# import urllib.request
# import json
#
# payload = {"key1": "value1", "key2": "value2"}

# url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
# with urllib.request.urlopen(url) as f:
#     # バイトコードで獲得のため、デコード
#     ans_json = f.read().decode('utf8')
#     # Json形式で記載のため、json,loadでdict型にする。
#     ans = json.loads(ans_json)
#     print(ans)

# POST
# import urllib.request
# import json
#
# payload = json.dumps({"key1": "value1", "key2": "value2"}).encode('utf8')
# req = urllib.request.Request(
#     'http://httpbin.org/post', data=payload, method='POST')
#
# with urllib.request.urlopen(req) as f:
#     print(json.loads(f.read().decode('utf8')))

import urllib.request
import json

payload = json.dumps({"key1": "value1", "key2": "value2"}).encode('utf8')
req = urllib.request.Request(
    'http://httpbin.org/put', data=payload, method='PUT')

with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf8')))

# import urllib.request
# import json
#
payload = json.dumps({"key1": "value1", "key2": "value2"}).encode('utf8')
req = urllib.request.Request(
    'http://httpbin.org/delete', data=payload, method='DELETE')

with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf8')))