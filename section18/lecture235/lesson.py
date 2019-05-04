#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

s = '<html><head><title>Title</title></head></html>'
print(re.match('<.*>', s))
print(re.match('<.*?>', s))

