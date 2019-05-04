#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

a = {'a': 'a', 'c': 'c', 'num': 0}
b = {'b': 'b', 'c': 'cc'}
c = {'b': 'bbb', 'c': 'ccc'}

class DeepChainMap(collections.ChainMap):
    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                if type(mapping[key]) is int and mapping[key] < value:
                    mapping[key] = value
                return
        self.maps[0][key] = value

m = DeepChainMap(a, b, c)
m['num'] = 1
print(m.maps)


# print(a)
# a.update(b)
# print(a)
# a.update(c)
# print(a)

# m = collections.ChainMap(a, b, c)
# m.maps.reverse()
# m.maps.insert(0, {'c': 'cccccc'})
# del m.maps[0]
# print(m['c'])
# m['b'] = 'BBBBB'
# print(m.maps)