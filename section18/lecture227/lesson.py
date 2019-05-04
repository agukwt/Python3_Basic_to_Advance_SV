#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

d = {}
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    if word not in d:
        d[word] = 0
    d[word] += 1
print(d)

d = {}
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    d.setdefault(word, 0)
    d[word] += 1
print(d)

d = collections.defaultdict(int)
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    d[word] += 1
print(d)

### 集合として扱痛い場合
d = collections.defaultdict(set)
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4),
     ('red', 1), ('blue', 4)]
for k, v in s:
    d[k].add(v)
print(d)

