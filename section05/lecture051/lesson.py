#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


# y = [1, 2, 3]
# r = test_func(100, y)
# print(r)
#
# y = [1, 2, 3]
# r = test_func(200, y)
# print(r)

r = test_func(100)
print(r)

r = test_func(100)
print(r)
