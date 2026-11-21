import pygame, importlib.util, os

InMenu = True
first_click = True
Minigames = None

class Minigames_Obj:
    height = 28
    padding = 4
    totalHeight = height + padding
    font = pygame.font.SysFont("Consolas", height)
    def __init__(self, rootdir):
        self.rootdir = rootdir
        self.options = os.listdir(os.path.join(self.rootdir, "minigames"))
        self.options.append("Zpět")
    def run_minigame(self, i):
        minigame_module_spec = importlib.util.spec_from_file_location(f"minigame_{self.options[i]}", os.path.join(self.rootdir, "minigames", self.options[i], "main.py"))
        minigame_module = importlib.util.module_from_spec(minigame_module_spec)
        minigame_module_spec.loader.exec_module(minigame_module)
        minigame_module.main()

def click(x,y):
    global InMenu, first_click, Minigames
    # Fix queued click exits menu
    if first_click:
        first_click = False
        return
    y>>=5
    if y == len(Minigames.options) - 1:
        InMenu = False
        return
    Minigames.run_minigame(y)
    InMenu = False

def main(path):
    global Minigames
    Minigames = Minigames_Obj(path)
    global InMenu
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
