#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import re

# d = {}
# l = ['a', 'a', 'a', 'b', 'b', 'c']
# for word in l:
#     if word not in d:
#         d[word] = 0
#     d[word] += 1
# print(d)
#
# d = {}
# l = ['a', 'a', 'a', 'b', 'b', 'c']
# for word in l:
#     d.setdefault(word, 0)
#     d[word] += 1
# print(d)
#
# d = collections.defaultdict(int)
# l = ['a', 'a', 'a', 'b', 'b', 'c']
# for word in l:
#     d[word] += 1
# print(d)

c = collections.Counter()
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    c[word] += 1
print(c)
print(c.most_common(3))
print(c.values())

with open('lesson.py', 'r', encoding='utf8') as f:
    words = re.findall(r'\w+', f.read().lower())
    print(words)
    print(collections.Counter(words).most_common(3))

