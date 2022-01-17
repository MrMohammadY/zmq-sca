from uuid import uuid4

import zmq
import json

from utils.colors import *
from utils.input import InputManager


class Client:

    def __init__(self):
        """
        generate uuid and assign to each client created
        """
        self.id = u'client-%d' % uuid4()

    def run(self):
        """
        here we create context and socket and send user inputs to server and receive response and show that
        :return: None
        """
        context = zmq.Context()
        socket = context.socket(zmq.DEALER)
        socket.identity = self.id.encode('ascii')
        socket.connect('tcp://localhost:5570')
        print(f'{BEIGE}{self.id} started')

        poll = zmq.Poller()
        poll.register(socket, zmq.POLLIN)

        while True:
            command_type, command, data = InputManager.create_data()
            socket.send(json.dumps(data).encode('utf-8'))
            server_response = socket.recv().decode('utf-8')
            print(f'{VIOLET}server response is: {BLUE}{server_response}')

        socket.close()
        context.term()


if __name__ == '__main__':
    client = Client()
    client.run()
