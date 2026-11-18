import random, pygame, os
import numpy as np

class PexesoGame():
    def __init__(self, screen):
        self.screen = screen
        self.xSize = 4
        self.ySize = 3
        self.spriteX = 64
        self.spriteY = 64
        self.turned = [()]
        # Does field size make sense?
        if self.xSize*self.ySize%2==1:
            raise Exception
        self.pairsLeft = int(self.xSize*self.ySize/2)
        self.deck = list(range(1, self.pairsLeft+1))*2
        random.shuffle(self.deck)
        self.deck = np.array(self.deck)
        self.field = self.deck.reshape(self.xSize, self.ySize)
        self.spritesheet = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resource", "spritesheet.png"))
        self.sprites = [pygame.Surface((self.spriteX,self.spriteY)) for _ in range(self.pairsLeft+2)]
        for s, i in zip(self.sprites, range(0, len(self.sprites))): s.blit(self.spritesheet, (0, 0), pygame.Rect(self.spriteX*i, 0, self.spriteX, self.spriteY))
    def click(self, x, y):
        if self.turned[0] == ():
            self.turned[0] = (x>>6,y>>6)
        else: self.eval_pair(x>>6,y>>6)
    def eval_pair(self,x,y):
        if self.field[self.turned[0]] == self.field[x,y]:
            self.field[self.turned[0]] = -1
            self.field[x,y] = -1
            self.pairsLeft -= 1
            if self.pairsLeft == 0:
                # TODO: Win
                exit(0)
            self.turned.append(self.turned[0])
            self.turned.append((x,y))
            self.turned[0] = ()
        else:
            self.turned.append((x,y))
            self.draw()
            self.turned.pop(-1)
            self.turned[0] = ()
            pygame.time.wait(1500)
    def draw(self):
        self.screen.fill("white")
        for x,y in np.ndindex((self.xSize,self.ySize)):
            self.screen.blit(self.sprites[self.field[x,y] if (x,y) in self.turned else 0], (self.spriteX*x, self.spriteY*y))
        pygame.display.flip()


# Temporary runner for testing
pygame.init()
screen = pygame.display.set_mode((256, 192))
pexeso = PexesoGame(screen)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pexeso.draw()

    event = pygame.event.wait()
    if event.type == pygame.MOUSEBUTTONUP:
        pexeso.click(*pygame.mouse.get_pos())

    clock.tick(60)

pygame.quit()
