#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import (
    Process,
    Lock, RLock, Semaphore, Queue, Event, Condition, Barrier,
    Value, Array, Pipe, Manager)

import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def worker1(i):
    logging.debug('start')
    logging.debug(i)
    time.sleep(1)
    logging.debug('end')


def worker2(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')


if __name__ == '__main__':
    i = 10
    t1 = multiprocessing.Process(target=worker1, args=(i,))
    t1.daemon = True
    t2 = multiprocessing.Process(target=worker2, args=(i,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
