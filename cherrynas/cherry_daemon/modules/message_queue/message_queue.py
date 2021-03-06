# Copyright 2022 fnwinter@gmail.com

import time
import zmq

def process_main(context):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        #  Wait for next request from client
        message = socket.recv()
        print(f"Received request: {message}")

        #  Do some 'work'
        time.sleep(1)

        #  Send reply back to client
        socket.send(b"World")
