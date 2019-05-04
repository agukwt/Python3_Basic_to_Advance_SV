#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from lesson_package import utils
except ImportError:
    from lesson_package.tools import utils

utils.say_twice('word')