#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import queue

q = queue.Queue()       # FIFO
lq = queue.LifoQueue()  # LIFO
l = []
dr = collections.deque()   # Double-end queue:
dl = collections.deque()   # Double-end queue:

d = collections.deque()   # Double-end queue:

for i in range(3):
    q.put(i)
    lq.put(i)
    l.append(i)
    dr.append(i)
    dl.append(i)
    d.append(i)


# for _ in range(3):
#     print('FIFO queue = {}'.format(q.get()))
#     print('LIFO queue = {}'.format(lq.get()))
#     print('List       = {}'.format(l.pop()))
#     print('dequeue(R) = {}'.format(dr.pop()))
#     print('dequeue(L) = {}'.format(dl.popleft()))
#     print()

print(d)
d.rotate(1)
print(d)
d.rotate(-1)
print(d)
d.extend('R')
d.extendleft('L')
print(d)

d.clear()
print(d)

