#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

h = logging.FileHandler(r'section11/lecture123/logtest.log')
h.setFormatter(logging.Formatter('%(module)s %(levelname)s: %(message)s'))
logger.addHandler(h)

logger.info('handler')