import random, pygame, os
import numpy as np

class PexesoGame():
    def __init__(self, screen):
        self.font_small = pygame.font.SysFont("Consolas", 20)
        self.font_large = pygame.font.SysFont("Consolas", 50)
        self.activePlayer = 0
        self.scores = [0,0]
        self.screen = screen
        self.xSize = 4
        self.ySize = 3
        self.spriteX = 64
        self.spriteY = 64
        self.fieldX = self.xSize*self.spriteX
        self.fieldY = self.ySize*self.spriteY
        self.turned = [()]
        self.lang = "cz"
        self.strings = {"cz": {"P0": "Hráč 1", "P1": "Hráč 2"}}
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
        if y > self.fieldY:
            return
        if (x>>6,y>>6) in self.turned: return
        if self.turned[0] == ():
            self.turned[0] = (x>>6,y>>6)
        else:
            if self.turned[0] != (x>>6,y>>6):
                self.activePlayer = not self.activePlayer
                self.eval_pair(x>>6,y>>6)
    def eval_pair(self,x,y):
        if self.field[self.turned[0]] == self.field[x,y]:
            self.activePlayer = not self.activePlayer
            self.field[self.turned[0]] = -1
            self.field[x,y] = -1
            self.pairsLeft -= 1
            self.scores[self.activePlayer] += 1
            if self.pairsLeft == 0:
                self.draw()
                if self.scores[1] > self.scores[0]:
                    self.draw_ui_p1("W")
                    pygame.display.flip()
                elif self.scores[1] == self.scores[0]:
                    self.draw_ui_p0("W")
                    self.draw_ui_p1("W")
                    pygame.display.flip()
                else:
                    self.draw_ui_p0("W")
                    pygame.display.flip()
                self.event = pygame.event.wait()
                pygame.time.wait(500)
                exit(0)
            self.turned.append(self.turned[0])
            self.turned.append((x,y))
            self.turned[0] = ()
        else:
            self.turned.append((x,y))
            self.draw()
            self.turned.pop(-1)
            self.turned[0] = ()
            pygame.time.wait(1000)
    def draw(self):
        self.screen.fill("white")
        for x,y in np.ndindex((self.xSize,self.ySize)):
            self.screen.blit(self.sprites[self.field[x,y] if (x,y) in self.turned else 0], (self.spriteX*x, self.spriteY*y))
        self.draw_ui()
        pygame.display.flip()
    def draw_ui(self):
        self.draw_ui_p0(self.scores[0])
        self.draw_ui_p1(self.scores[1])
    def draw_ui_p0(self, score):
        self.screen.blit(self.font_small.render(self.strings[self.lang]["P0"], True, (0,0,0), None if self.activePlayer else (0,0,255)), (4, self.fieldY+4))
        sx,sy=self.font_small.size(self.strings[self.lang]["P0"])
        self.screen.blit(self.font_large.render(f"{score}", True, (0,0,255),(255,255,255)), ((4+(sy>>1)), self.fieldY+4+sy))
    def draw_ui_p1(self, score):
        sx,sy=self.font_small.size(self.strings[self.lang]["P1"])
        lx,ly=self.font_large.size(f"{self.scores[1]}")
        self.screen.blit(self.font_small.render(self.strings[self.lang]["P1"], True, (0,0,0), (255,0,0) if self.activePlayer else None), (self.fieldX-4-sx, self.fieldY+4))
        self.screen.blit(self.font_large.render(f"{score}", True, (255,0,0), (255,255,255)), (self.fieldX-(4+(sy>>1))-lx, self.fieldY+4+sy))

# Temporary runner for testing
pygame.init()
# TODO: Remove hardcoded values, if possible
screen = pygame.display.set_mode((256, 192+128))
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
