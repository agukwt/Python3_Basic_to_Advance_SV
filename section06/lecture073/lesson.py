#!/usr/bin/env python
# -*- coding: utf-8 -*-

# print(globals())

ranking = {
    'A': 100,
    'B': 85,
    'C': 92
}

print(sorted(ranking, key=ranking.get, reverse=True))