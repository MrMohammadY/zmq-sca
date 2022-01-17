import json
from uuid import uuid4

import zmq
import threading
from subprocess import PIPE, run

from utils.colors import *
from utils.parser import ParserMessage


class Server:
    def __init__(self):
        """
        here we create public context
        """
        self.context = zmq.Context()

    @staticmethod
    def listener_worker(worker, uuid):
        """
        here we listener and receive message from client and send response to clients
        :param worker: worker
        :param uuid:  worker id
        :return:
        """
        while True:
            client_id, message = worker.recv_multipart()
            message = json.loads(json.loads(message.decode('utf-8')))
            cm_type, result = ParserMessage.parse(message)

            print(f'{VIOLET}worker-{uuid}{RESET} '
                  f'received {RED}{BOLD}{result}{RESET} from {YELLOW}{client_id.decode()}{WHITE}')

            if cm_type == 'os':
                output = run(result, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
                response = dict(given_os_command=result, result=output.stdout, error=output.stderr)
                worker.send_multipart([client_id, json.dumps(response).encode('utf-8')])
            elif cm_type == 'compute':
                response = dict(given_math_expression=result, result=eval(result))
                worker.send_multipart([client_id, json.dumps(response).encode('utf-8')])
            else:
                break

        worker.close()

    def initial_worker(self):
        """
        here create worker sockets and send worker to listener
        :return:
        """
        worker = self.context.socket(zmq.DEALER)
        worker.connect('inproc://backend')
        uuid = uuid4()
        print(f'{BLUE}worker-{uuid} started{RESET}')
        self.listener_worker(worker, uuid)

    def run(self):
        """
        here we create front and backend and create worker with thread
        :return: None
        """
        frontend = self.context.socket(zmq.ROUTER)
        frontend.bind('tcp://*:5570')

        backend = self.context.socket(zmq.DEALER)
        backend.bind('inproc://backend')

        for _ in range(5):
            thread = threading.Thread(target=self.initial_worker)
            thread.start()

        zmq.proxy(frontend, backend)

        frontend.close()
        backend.close()
        self.context.term()


if __name__ == "__main__":
    server = Server()
    server.run()
