#!/usr/bin/env python
# -*- coding: utf-8 -*-

import contextlib

@contextlib.contextmanager
def tag(name):
    print('<{}>'.format(name))
    yield
    print('</{}>'.format(name))

# 方法①
# @tag('h2')
# def f(content):
#     print(content)
#
# f('test')

# 方法②
# with tag('h2'):
#     print('test')
