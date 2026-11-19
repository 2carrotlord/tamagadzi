import pygame
running = True

pygame.init()
obraz = pygame.display.set_mode((500,500))
obraz.fill((56, 98, 166))

#mrizka
pygame.draw.rect(obraz, (156, 184, 230), [30, 30, 450, 450])
pygame.draw.line(obraz, (0,0,0), (180, 50), (180, 450), (5))
pygame.draw.line(obraz, (0,0,0), (320, 50), (320, 450), (5))
pygame.draw.line(obraz, (0,0,0), (50, 180), (450, 180), (5))
pygame.draw.line(obraz, (0,0,0), (50, 320), (450, 320), (5))

pygame.display.flip()

#gameloop
while running:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           running = False