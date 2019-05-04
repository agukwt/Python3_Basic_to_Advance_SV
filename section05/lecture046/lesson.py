#!/usr/bin/env python
# -*- coding: utf-8 -*-

days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orage']
drinks = ['coffee', 'tea', 'beer']

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)
