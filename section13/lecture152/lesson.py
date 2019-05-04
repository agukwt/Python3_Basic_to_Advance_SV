#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


HEAD_PATH = r'C:\Programing\SiliconValleyPython\section13\lecture152' + '\\'

j = {"employee": [{"id": 111, "name": "Mike"},
                  {"id": 222, "name": "Nancy"}]}

# python上でのエンコード・デコード
a = json.dumps(j)
b = json.loads(a)

# 書き込み
with open(HEAD_PATH + 'test,json', 'w') as f:
    json.dump(j, f)

# 読み込み
with open(HEAD_PATH + 'test,json', 'r') as f:
    print(json.load(f))