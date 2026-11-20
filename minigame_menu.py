import pygame, importlib.util

pygame.font.init()

class Minigames:
    options = ["pexeso", "Zpět"]
    font = pygame.font.SysFont("Consolas", 20)
#
#
#
# Nešahat!!
#
#
#
def main(callback):
    screen = pygame.display.set_mode((256, 24*len(Minigames.options)*2))
    screen.fill((255,255,255))
    pygame.display.set_caption("Minihry")
    for i in range(0,len(Minigames.options)):
        a=Minigames.font.render(Minigames.options[i].capitalize(), True, (0,0,0))
        x,y=a.get_size()
        screen.blit(a, (64-x>>1, 20*i))
    pygame.display.flip()
    while True:
        pass
