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
    time.sleep(1.5)
    logging.debug('end')
    return i * 2


if __name__ == '__main__':
    with multiprocessing.Pool(3) as p:
        r = p.map(worker1, [100, 200])
        logging.debug('executed')
        logging.debug(r)

        r = p.imap(worker1, [100, 200])
        logging.debug('executed')
        logging.debug([i for i in r])

        r = p.map_async(worker1, [100, 200])
        logging.debug('executed')
        logging.debug(r.get())

        # p1 = p.apply_async(worker1, (100,))
        # p2 = p.apply_async(worker1, (100,))
        # logging.debug('executed')
        # logging.debug(p1.get())
        # logging.debug(p2.get())