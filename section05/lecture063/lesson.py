#!/usr/bin/env python
# -*- coding: utf-8 -*-

def g():
    for i in range(10):
        yield i


# g = g()
# print(type(g))
# print(next(g))

g = (i for i in range(3))
print(type(g))
print(next(g))
print(next(g))
print(next(g))
