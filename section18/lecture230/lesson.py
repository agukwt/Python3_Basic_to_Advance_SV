#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import collections

with open('names,csv', 'w', newline='', encoding='utf8') as csvfile:
    fieldnames = ['first', 'last', 'address']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first': 'Mika', 'last': 'Jackson', 'address': 'A'})
    writer.writerow({'first': 'Jun', 'last': 'Sakai', 'address': 'B'})
    writer.writerow({'first': 'Nancy', 'last': 'Mask', 'address': 'C'})

with open('names,csv', 'r', newline='', encoding='utf8') as f:
    csv_reader = csv.reader(f)
    # 'Names'というnamedtupleでfieldnamesを辞書keyを作る
    Names = collections.namedtuple('Names', next(csv_reader))
    for row in csv_reader:
        # 辞書keyへvalueを流す
        names = Names._make(row)
        print(names.first, names.last, names.address)

# p = (10, 20)
# print(p[0])
#
# # tupleなので不可
# # p[0] = 100
#
# Point = collections.namedtuple('Point', ['x', 'y'])
# p = Point(10, 20)
# print(p.x)
#
# p1 = Point._make([100, 200])
# print(p1)
# print(p1._asdict())
#
# p1._replace(x=400)
# print(p1)
# p2 = p1._replace(x=400)
# print(p2)
#
#
# class SumPoint(collections.namedtuple('Point', ['x', 'y'])):
#     @property
#     def total(self):
#         return self.x + self.y
#
# p3 = SumPoint(2, 3)
# print(p3.x, p3.y, p3.total)

