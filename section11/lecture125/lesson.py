#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging


logger = logging.getLogger(__name__)


logger.error('Api call is failed.')



func = 10*10

logger.error({
    'action': 'func',
    'status': 'fail',
    'message': 'Api call is failed'
})