#!/usr/bin/env python
# -*- coding: utf-8 -*-

import contextlib
import os

# try:
#     os.remove('anlajcn.tmp')
# except FileNotFoundError:
#     pass

with contextlib.suppress(FileNotFoundError):
    os.remove('anlajcn.tmp')