#!/usr/bin/env python
# -*- coding: utf-8 -*-

def t():
    for i in range(10):
        yield i


for i in t():
    print(i)

print((lambda x, r: x*r)(8000, 1.08))