#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('test_sqlite.db')
# conn = sqlite3.connect(':memory:')

curs = conn.cursor()
curs.execute(
    'CREATE TABLE persons ( id INTEGER PRIMARY KEY AUTOINCREMENT,'
    '                       name STRING )')
curs.execute('INSERT INTO persons(name) values("Mike")')
curs.execute('INSERT INTO persons(name) values("Nancy")')
curs.execute('INSERT INTO persons(name) values("Jun")')
curs.execute('UPDATE persons set name = "Michel" WHERE name = "Mike"')

curs.execute('DELETE from persons WHERE name = "Michel"')
curs.execute('SELECT * FROM persons')
print(curs.fetchall())

curs.close()

conn.commit()
conn.close()

