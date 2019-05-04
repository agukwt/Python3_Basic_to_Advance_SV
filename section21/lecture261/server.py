import time

import zmq


context = zmq.Context()
sock = context.socket(zmq.PUSH)
sock.bind("tcp://127.0.0.1:5690")


id = 0
while True:
    id += 1
    sock.send(str(id).encode())
    print("Sent: {}".format(id))
    time.sleep(1)