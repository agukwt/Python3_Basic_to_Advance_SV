#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logging.basicConfig(level=logging.INFO)


class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message


logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter())
logger.info('OK info')
logger.info('password:={}'.format('password'))
