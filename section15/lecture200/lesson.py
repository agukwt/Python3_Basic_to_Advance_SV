#!/usr/bin/env python
# -*- coding: utf-8 -*-


from multiprocessing import (
    Process,
    Lock, RLock, Semaphore, Queue, Event, Condition, Barrier,
    Value, Array, Pipe, Manager)

import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(d, lock):
    logging.debug('start')
    with lock:
        i = d['x']
        time.sleep(3)
        d['x'] = i + 1
        logging.debug(d)
        with lock:
            d['x'] = i + 1
            logging.debug(d)
    logging.debug('end')


def worker2(d, lock):
    logging.debug('start')
    lock.acquire()
    i = d['x']
    d['x'] = i + 1
    logging.debug(d)
    lock.release()
    logging.debug('end')


# threadでは以下表記が必要
if __name__ == '__main__':
    d = {'x': 0}
    lock = multiprocessing.RLock()
    t1 = multiprocessing.Process(target=worker1, args=(d, lock))
    t2 = multiprocessing.Process(target=worker2, args=(d, lock))
    t1.start()
    t2.start()
    print('started')