__author__ = 'OL'


class Judge:
    """  The base class of a judge who can moderate the result of each step  """

    def __init__(self):

        self.pA_move = None

        self.pB_move = None

    def receive(self, pA_move, pB_move):

        self.pA_move = pA_move

        self.pB_move = pB_move

    def rulling(self):

        if self.pA_move > self.pB_move:

            result = 0

        else:

            result = 1

        return result



