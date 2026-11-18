import random, pygame
import numpy as np

class PexesoGame():
    def __init__(self):
        self.xSize = 6
        self.ySize = 6
        # Does field size make sense?
        if self.xSize*self.ySize%2==1:
            raise Exception
        self.pairsLeft = int(self.xSize*self.ySize/2)
        self.deck = list(range(0, self.pairsLeft))*2
        random.shuffle(self.deck)
        self.deck = np.array(self.deck)
        self.field = self.deck.reshape(self.xSize, self.ySize)

