#!/usr/bin/env python
# -*- coding: utf-8 -*-


l = ['Mon', 'tue', 'Wed', 'Thu', 'Fri', 'sat', 'Sun']


def change_word(words, func):
    for word in words:
        print(func(word))


# def sample_func(word):
#     return word.capitalize()

change_word(l, lambda word: word.capitalize())
change_word(l, lambda word: word.lower())

