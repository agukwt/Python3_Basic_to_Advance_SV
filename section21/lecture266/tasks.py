import time
import random

import celery

app = celery.Celery(
    'tasks',
    broker='amqp://guest@localhost',
    backend='amqp://guest@localhost'
)

@app.task
def build_server():
    print('wait 10 sec')
    time.sleep(10)
    server_id = random.randint(1, 100)
    return server_id