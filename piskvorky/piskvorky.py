import pygame
running = True
pygame.init()

#mrizka
pole = [[0,0,0],
        [0,0,0],
        [0,0,0]]

#nacteni onrazku
o_ikonka = pygame.transform.scale(pygame.image.load("./piskvorky/visual/o.png"), (140, 140))
x_ikonka = pygame.transform.scale(pygame.image.load("./piskvorky/visual/x.png"), (140, 140))

#obrazovka
obraz = pygame.display.set_mode((500,500))
obraz.fill((56, 98, 166))
pygame.display.set_caption("Piškvorky")

#mrizka na obazovce
pygame.draw.rect(obraz, (156, 184, 230), [30, 30, 450, 450])
pygame.draw.line(obraz, (0,0,0), (180, 50), (180, 450), (5))
pygame.draw.line(obraz, (0,0,0), (320, 50), (320, 450), (5))        #1 ctverecek = 140x140px
pygame.draw.line(obraz, (0,0,0), (50, 180), (450, 180), (5))
pygame.draw.line(obraz, (0,0,0), (50, 320), (450, 320), (5))

pygame.display.flip()

#gameloop
while running:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(pygame.mouse.get_pos())
            mys_x, mys_y = pygame.mouse.get_pos()
            if 30 < mys_x < 480 and 30 < mys_y < 480:
                print("valid klik")