#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

od = collections.OrderedDict(
    {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2})
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
print(d == od)

dic = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
o_dic = collections.OrderedDict(sorted(dic.items(), key=lambda t: t[0]))
print(o_dic)

o_dic['cc'] = 100
o_dic = collections.OrderedDict(sorted(o_dic.items(), key=lambda t: t[0]))
print(o_dic)