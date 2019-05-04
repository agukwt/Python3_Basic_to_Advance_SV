#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

class T(object):
    def __init__(self, name):
        self.name = name


data = {
    'a': [1, 2, 3],
    'b': ('test', 'test'),
    'c': {'key': 'value'},
    'd': T('test')}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('data.pickle', 'rb') as f:
    data_loaded = pickle.load(f)
    print(data_loaded)

