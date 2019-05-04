#!/usr/bin/env python
# -*- coding: utf-8 -*-

import enum

class Status(enum.Enum):
    ACTIVE = 1
    # RENAMED_ACTIVE = 1
    INACTIVE = 2
    RUNNING = 3

# どんなステータスコードがあるか調べる
# for s in Status:
#     print(s)
#     print(type(s))
#
# print(Status(1))

print(Status.ACTIVE)            # Status.ACTIVE
print(repr(Status.ACTIVE))      # <Status.ACTIVE: 1>
print(Status.ACTIVE.name)       # ACTIVE
print(Status.ACTIVE.value)      # 1

db = {'stack1': 1, 'stack2': 2}

if Status(db['stack1']) == Status.ACTIVE:
    print('shutdown')
elif Status(db['stack1']) == Status.INACTIVE:
    print('terminate')



