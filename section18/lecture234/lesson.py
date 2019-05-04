#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

s = 'My name is ... Mike'
print(s.split())

p = re.compile(r'\W+')
print(p.split(s))

p = re.compile(r'blue|white|red')
print(p.sub('colour', 'blue socks and red shoes'))
print(p.sub('colour', 'blue socks and red shoes', count=1))
print(p.subn('colour', 'blue socks and red shoes'))

def hexrepl(match):
    value =int(match.group())
    return hex(value)

p = re.compile(r'\d')
print(p.sub(hexrepl, '12345 55 157 test'))
