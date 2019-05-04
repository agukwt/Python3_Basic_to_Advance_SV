#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging


logging.basicConfig(level=logging.INFO)
logging.info('info')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug('debug')


# # log test
# import logging
#
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
#
# def do_something():
#     logger.debug('from logtest debug')