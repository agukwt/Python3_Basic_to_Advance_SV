#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

s = ('ars:aws:cloudformation:amnvnnaibabcb:stack/'
     'cmaoaoncnak/vjojamcm/an-annv-na')

m = re.match(r'ars:aws:cloudformation:[\w\:]+stack/[\w]+/[\w]+/[\w-]+', s)
print("delta")
print(m)

s = ('ars:aws:cloudformation:amnvnnaibabcb:stack/')

m = re.match(r'ars:aws:cloudformation:[\w\:]+stack/', s)
print("delta")
print(m.group())

RE_STACK = re.compile(r'ars:aws:cloudformation:[\w\:]+stack/')
m = RE_STACK.match(str)