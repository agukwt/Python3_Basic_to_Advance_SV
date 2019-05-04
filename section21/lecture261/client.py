import zmq


conntext = zmq.Context()
sock = conntext.socket(zmq.PULL)
sock.connect("tcp://127.0.0.1:5690")

while True:
    message = sock.recv()
    print("Recieved: {}".format(message.decode()))
