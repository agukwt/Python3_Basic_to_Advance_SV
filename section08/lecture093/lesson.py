#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = """\
AAA
BBB
CCC
DDD
"""

with open('test.txt', 'r') as f:
    # print(f.read())
    while True:
        line = f.readline()
        print(line, end='')
        if not line:
            break
