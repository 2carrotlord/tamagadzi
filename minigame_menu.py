import pygame, importlib.util, os

InMenu = True
first_click = True
rootdir = ""

class Minigames:
    height = 28
    padding = 4
    totalHeight = height + padding
    options = ["pexeso", "Zpět"]
    font = pygame.font.SysFont("Consolas", height)

def click(x,y):
    global InMenu, first_click
    # Fix queued click exits menu
    if first_click:
        first_click = False
        return
    y>>=5
    if y == len(Minigames.options) - 1:
        InMenu = False
        return
    minigame_module_spec = importlib.util.spec_from_file_location(f"minigame_{Minigames.options[y]}", os.path.join(rootdir, Minigames.options[y], "main.py"))
    minigame_module = importlib.util.module_from_spec(minigame_module_spec)
    minigame_module_spec.loader.exec_module(minigame_module)
    minigame_module.main()
    InMenu = False

def main(path):
    global InMenu, rootdir
    rootdir = path
    screen = pygame.display.set_mode((256, Minigames.totalHeight*len(Minigames.options)))
    screen.fill((255,255,255))
    pygame.display.set_caption("Minihry")
    for i in range(0,len(Minigames.options)):
        a=Minigames.font.render(Minigames.options[i].capitalize(), True, (0,0,0))
        x,y=a.get_size()
        screen.blit(a, (128-(x>>1), Minigames.totalHeight*i))
    pygame.display.flip()
    while InMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONUP:
                click(*pygame.mouse.get_pos())
