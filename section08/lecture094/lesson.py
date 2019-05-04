#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('test.txt', 'r') as f:
    print(f.tell())
    print(f.read(1))
    f.seek(5)
    print(f.read(1))
    f.seek(14)
    print(f.read(1))
