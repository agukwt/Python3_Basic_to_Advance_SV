#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%Y/%d/%m %H:%M:%S.%f'))

import time
print('#####')
time.sleep(1)
print('#####')