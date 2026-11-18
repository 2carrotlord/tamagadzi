import random, pygame
import numpy as np

xSize = 6
ySize = 6
if xSize*ySize%2==1:
    raise Exception
pairsLeft = int(xSize*ySize/2)
deck = list(range(0, pairsLeft))*2
random.shuffle(deck)
deck = np.array(deck)
field = deck.reshape(xSize, ySize)

