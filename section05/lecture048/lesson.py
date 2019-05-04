#!/usr/bin/env python
# -*- coding: utf-8 -*-


def say_something():
    print('hi')


f = say_something
f()


def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green paper'
    else:
        return "I don't know"


print(what_is_this('red'))




