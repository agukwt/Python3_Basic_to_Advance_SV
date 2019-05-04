import time

import zmq


context = zmq.Context()
sock = context.socket(zmq.PUB)
sock.bind("tcp://127.0.0.1:5690")


id = 0
while True:
    id += 1
    sock.send(("Sub1: " + str(id)).encode())
    print("Sent: {}".format(id))
    time.sleep(1)