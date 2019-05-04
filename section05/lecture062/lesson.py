#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = set()

for i in range(10):
    s.add(i)

print(s)

s = {i for i in range(10)}
print(s)