#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = """\
AAA
BBB
CCC
DDD
"""

# 書き込み ＋ 読み込み
with open('test,txt', 'w+') as f:
    f.write(s)
    f.seek(0)
    print(f.read())

# 読み込み ＋ 書き込み
with open('test,txt', 'r+') as f:
    print(f.read())
    f.read(0)
    f.write(s)
