#!/usr/bin/env python
# -*- coding: utf-8 -*-

# print('{}, {}, {}'.format('a', 'b', 'c'))
# print('{0}, {1}, {2}'.format('a', 'b', 'c'))
# print('{1}, {2}, {0}'.format('a', 'b', 'c'))
# print('{name} {family}, {family} {name}'.format(name='jun', family='sakai'))

# t = (1, 2, 3)
#
# print('{t[0]} {t[1]} {t[2]}'.format(t=t))
# print('{0} {1} {2}'.format(*t))
# print('{0} {1} {2}'.format(1, 2, 3))
#
# d = {'name': 'jun', 'family': 'sakai'}
# print('{0[name]} {0[family]}'.format(d))
# print('{name} {family}'.format(**d))
# print('{name} {family}'.format(name='jun', family='sakai'))


print('{:<30}'.format('left'))          # 左詰め   30文字
print('{:>30}'.format('right'))         # 右詰め   30文字
print('{:^30}'.format('center'))        # 中央詰め  30文字

print('{:*^30}'.format('astarisc'))     # 中央詰め  10文字    埋め文字'*'

print('{str:{fill}{align}{width}}'.format(str='abcde', fill='-', align='^', width=30))

print('{num:,}'.format(num=100000))
print('{num:+f}'.format(num=3.14159))

print('{num:.2}'.format(num=3.14159))
print('{num:.2%}'.format(num=0.64))

print('{num:.2%}'.format(num=0.64))

print('{accuracy:<20}'.format(accuracy=0.987654321))        # 0.987654321
print('{accuracy:>20}'.format(accuracy=0.987654321))        #         0.987654321
print('{accuracy:^20}'.format(accuracy=0.987654321))        #    0.987654321

print('{accuracy:.5}'.format(accuracy=0.987654321))         # 0.98765
print('{accuracy:.5%}'.format(accuracy=0.987654321))        # 98.76543%

print('{accuracy:>20.5%}'.format(accuracy=0.987654321))     #            98.76543%
print('{accuracy:_>20.5%}'.format(accuracy=0.987654321))    # ___________98.76543%




