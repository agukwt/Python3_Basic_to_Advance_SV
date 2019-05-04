#!/usr/bin/env python
# -*- coding: utf-8 -*-

class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)
try:
    check()
except UppercaseError as exc:
    print('This is my Defined Error.')