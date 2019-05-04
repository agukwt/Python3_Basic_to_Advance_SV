#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3


conn = sqlite3.connect('test_sqlite.db')
conn.close()