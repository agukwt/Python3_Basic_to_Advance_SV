#!/usr/bin/env python
# -*- coding: utf-8 -*-


# def memoize(f):
#     memo = {}
#     def _wrapper(n):
#         if n not in memo:
#             memo[n] = f(n)
#         return memo[n]
#     return _wrapper
#
#
# @memoize
# def long_func(n):
#     r = 0
#     for i in range(10000000):
#         r += n * i
#     return r
#
#
# for i in range(10):
#     print(long_func(i))
#
# for i in range(10):
#     print(long_func(i))


import functools

def long_func(n):
    r = 0
    for i in range(10000000):
        r += n * i
    return r

@functools.lru_cache()
def long_func(n):
    r = 0
    for i in range(10000000):
        r += n * i
    return r


for i in range(10):
    print(long_func(i))

print(long_func.cache_info())

for i in range(10):
    print(long_func(i))

long_func.cache_clear()