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

# Temporary runner for testing
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    pygame.display.flip()



    clock.tick(60)

pygame.quit()
