#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tarfile

path = r'section08/lecture099/testdir'

with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add(path)

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    tr.extractall('test_tar')
