__author__ = 'OL'
import random


class Player:
    """ Define the base class for a computer player """

    def __init__(self):
        self.move = None

    def think(self):
        """ Define the think proc of a computer player for the next move """
        self.move = random.random()






