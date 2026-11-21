import random, pygame, os
import numpy as np


class PexesoGame():
    sizeX = 4
    sizeY = 3
    spriteX = 64
    spriteY = 64
    font_small = pygame.font.SysFont("Consolas", 20)
    font_large = pygame.font.SysFont("Consolas", 50)
    strings = {"cz": {"P0": "Hráč 1", "P1": "Hráč 2"}, "en": {"P0": "Player 1", "P1": "Player 2"}}
    fieldX = sizeX*spriteX
    fieldY = sizeY*spriteY
    def __init__(self, screen):
        self.activePlayer = 0
        self.running = True
        self.scores = [0,0]
        self.screen = screen
        self.turned = [()]
        self.lang = "cz"
        if self.sizeX*self.sizeY%2==1:
            raise Exception
        self.pairsLeft = int(self.sizeX*self.sizeY/2)
        self.deck = list(range(1, self.pairsLeft+1))*2
        random.shuffle(self.deck)
        self.deck = np.array(self.deck)
        self.field = self.deck.reshape(self.sizeX, self.sizeY)
        self.spritesheet = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resource", "spritesheet.png"))
        self.sprites = [pygame.Surface((self.spriteX,self.spriteY)) for _ in range(self.pairsLeft+2)]
        for s, i in zip(self.sprites, range(0, len(self.sprites))): s.blit(self.spritesheet, (0, 0), pygame.Rect(self.spriteX*i, 0, self.spriteX, self.spriteY))
    def click(self, x, y):
        if y > self.fieldY:
            return
        x>>=6
        y>>=6
        if (x,y) in self.turned: return
        if self.turned[0] == ():
            self.turned[0] = (x,y)
        else:
            if self.turned[0] != (x,y):
                self.activePlayer = not self.activePlayer
                self.eval_pair(x,y)
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
                pygame.time.wait(3000)
                self.running = False
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
        for x,y in np.ndindex((self.sizeX,self.sizeY)):
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

def main():
    pygame.init()
    screen = pygame.display.set_mode((PexesoGame.fieldX, PexesoGame.fieldY+128))
    pexeso = PexesoGame(screen)
    while pexeso.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONUP:
                pexeso.click(*pygame.mouse.get_pos())
        pexeso.draw()
