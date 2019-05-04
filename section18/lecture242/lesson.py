#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools


def d(f):
    @functools.wraps(f)
    def w():
        """ wrapper docstring """
        print('deco')
        return f()
    return w

@d
def example():
    """ Example docstring """
    print('example')


example()

help(example)
print(example.__doc__)