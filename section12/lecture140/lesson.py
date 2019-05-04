#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dbm

with dbm.open('cache', 'c') as db:
    db['key1'] = 'value1'
    db['key1'] = 'value2'

with dbm.open('cache', 'r') as db:
    print(db.get('key1'), db.get('key2'),)
