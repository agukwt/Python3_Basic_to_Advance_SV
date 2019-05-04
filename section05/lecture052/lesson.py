#!/usr/bin/env python
# -*- coding: utf-8 -*-

def say_something(word, *args):
    for arg in args:
        print(arg)


say_something('Hi!', 'Mike', 'Nancy')