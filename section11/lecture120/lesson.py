#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

path = r'section11/lecture120/api.log'
logging.basicConfig(filename=path, level=logging.DEBUG)

# logging.critical('critical')
# logging.error('error')
# logging.warning('warning')
# logging.info('info')
# logging.debug('debug')

logging.info('info {} {}'.format('test', 'test2'))
