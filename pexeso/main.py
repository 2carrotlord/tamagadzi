import random, pygame, os
import numpy as np

class PexesoGame():
    def __init__(self):
        self.xSize = 4
        self.ySize = 3
        # Does field size make sense?
        if self.xSize*self.ySize%2==1:
            raise Exception
        self.pairsLeft = int(self.xSize*self.ySize/2)
        self.deck = list(range(1, self.pairsLeft+1))*2
        random.shuffle(self.deck)
        self.deck = np.array(self.deck)
        self.field = self.deck.reshape(self.xSize, self.ySize)
        self.spritesheet = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resource", "spritesheet.png"))
        self.sprites = [pygame.Surface((64,64)) for _ in range(self.pairsLeft+1)]
        for s, i in zip(self.sprites, range(0, len(self.sprites))): s.blit(self.spritesheet, (0, 0), pygame.Rect(64*i, 0, 64, 64))


# Temporary runner for testing
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pexeso = PexesoGame()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")

    for x,y in np.ndindex((pexeso.xSize,pexeso.ySize)):
        screen.blit(pexeso.sprites[pexeso.field[x,y]], (64*x, 64*y))

    pygame.display.flip()
    clock.tick(1)

pygame.quit()
