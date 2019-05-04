#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zipfile
import glob

with zipfile.ZipFile('test.zip', 'w') as z:
    for f in glob.glob(r'section08/lecture100/testdir/**', recursive=True):
        print(f)
        z.write(f)

with zipfile.ZipFile('test.zip', 'r') as z:
    z.extractall('zip')

