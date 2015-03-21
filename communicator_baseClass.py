__author__ = 'OL'
import socket


class Communicator:
    """ Define the communicator of the game """

    def __init__(self):
        # create an INET, STREAMing socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.s.connect()



