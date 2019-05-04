#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import queue
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker(queue):
    logging.debug('start')
    while True:
        item = queue.get()
        if item is None:
            break
        logging.debug(item)
        queue.task_done()

    logging.debug('log Clean UP')
    logging.debug('end')


# def worker1(queue):
#     logging.debug('start')
#     queue.put(100)
#     time.sleep(3)
#     queue.put(200)
#     logging.debug('end')
#
#
# def worker2(queue):
#     logging.debug('start')
#     logging.debug(queue.get())
#     logging.debug(queue.get())
#     logging.debug('end')


# threadでは以下表記が必要
if __name__ == '__main__':
    d = {'x': 0}
    queue = queue.Queue()
    for i in range(10000):
        queue.put(i)
    # t1 = threading.Thread(target=worker1, args=(queue,))
    # t2 = threading.Thread(target=worker2, args=(queue,))
    # t1.start()
    # t2.start()
    ts = []
    for _ in range(3):
        t = threading.Thread(target=worker, args=(queue,))
        t.start()
        ts.append(t)
    logging.debug('task are not done')
    queue.join()
    logging.debug('task are done')
    queue.put(None)
    queue.put(None)
    queue.put(None)

    [t.join() for r in ts]

