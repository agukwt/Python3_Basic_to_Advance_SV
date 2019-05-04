#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open('test.txt', 'w')
f.write('Test\n')
print('I am print', file=f)
f.close()