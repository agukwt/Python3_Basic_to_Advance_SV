#!/usr/bin/env python
# -*- coding: utf-8 -*-


# def outer(a, b):
#     def inner():
#         return a + b
#
#     return inner
#
#
# f = outer(1, 2)
# r = f()
# print(r)

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.14159)

print(ca1(10))
print(ca2(10))
