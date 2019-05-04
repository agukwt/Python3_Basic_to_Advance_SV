#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pprint

l = ['apple', 'orange', 'banana', 'peach', 'mango']
print(l)
l.insert(0, l[:])
pp = pprint.PrettyPrinter(indent=4, width=40, compact=True, depth=2)
pp.pprint(l)

d = {'a': 'A', 'b': 'B', 'c': {'x': {'a': 'A', 'b': 'B', 'c': 'C'}}}
pp.pprint(d)
print(json.dumps(d, indent=4))





