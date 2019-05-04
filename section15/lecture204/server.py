import queue
from multiprocessing.managers import BaseManager

queue = queue.Queue()


class QueueManager(BaseManager):
    pass


QueueManager.register(
    'get_queue', callable=lambda: queue)
manager = QueueManager(
    address=('127.0.0.1', 50000),
    authkey=b'asdfgtrewq')
server = manager.get_server()
server.serve_forever()

