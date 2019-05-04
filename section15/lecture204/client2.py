from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass


QueueManager.register('get_queue')
manager = QueueManager(
    address=('127.0.0.1', 50000),
    authkey=b'asdfgtrewq')

manager.connect()
queue = manager.get_queue()
print(queue.get())
