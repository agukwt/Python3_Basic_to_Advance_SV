#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

"""
match()     文字列の先頭で正規表現と一致するか判定  
search()    文字列を操作して、正規表現がどこに一致するか調べる
findall()   正規表現に一致する部分文字列をすべて探しリストとして返す
finditer()  重複しないマッチオブジェクトのイテレートを返す
"""

# m = re.match('a.c', 'abc')
# print(m)
# print(m.group())
#
# m = re.search('a.c', 'test abc test abc')
# print(m)
# print(m.span())
# print(m.group())
#
# m = re.findall('a.c', 'test abc test abc')
# print(m)
#
# m = re.finditer('a.c', 'test abc test abc')
# print(m)
# print([w.group() for w in m])

m = re.match('[a-zA-Z0-9]', '_')
m = re.match('\w', '_')
m = re.match('[^a-zA-Z0-9]', '@')
m = re.match('\W', '@')
print(m)