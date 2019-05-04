#!/usr/bin/env python
# -*- coding: utf-8 -*-

t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9,10)
r = [i for i in t if i % 2 == 0]

r = [i * j for i in t for j in t2]
print(r)
