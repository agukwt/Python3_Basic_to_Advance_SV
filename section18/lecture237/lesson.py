#!/usr/bin/env python
# -*- coding: utf-8 -*-

print('s')
print(str('s'))
print(repr('s'))

import datetime

d = datetime.datetime.now()
print(d)            # 2019-04-21 16:36:19.257483
print(str(d))       # 2019-04-21 16:36:19.257483
print(repr(d))      # datetime.datetime(2019, 4, 21, 16, 36, 19, 257483)

print('{!r} {} {!s}'.format('test', 'test', 'test'))

class Point(object):
    def __str__(self):
        return 'Point ############'
    def __str__(self):
        return 'Point<object>'

    pass

p = Point()
print('{0!r} {0} {0!s}'.format(p))