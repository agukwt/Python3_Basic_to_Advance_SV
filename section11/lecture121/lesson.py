#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

formatter = '%(levelname)s: %(message)s'
# python用ロギング機能から、フォーマットを確認できる。

logging.basicConfig(level=logging.INFO, format=formatter)
logging.info('info {} {}'.format('test', 'test2'))

