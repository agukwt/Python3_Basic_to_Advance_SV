#!/usr/bin/env python
# -*- coding: utf-8 -*-


def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)


menu('banana', 'apple', 'orange', entree='beef', drink='coffee')
