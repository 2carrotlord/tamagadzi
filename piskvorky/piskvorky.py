import pygame
running = True
pygame.init()

#mrizka
pole = [[0,0,0],    # 1 2 3
        [0,0,0],    # 4 5 6
        [0,0,0]]    # 7 8 9
zacatky = [40, 180, 320]
uhlopricka_zleva = [pole[0][0], pole[1][1], pole[2][2]]
uhlopricka_zprava = [pole[0][2], pole[1][1], pole[2][0]]

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

volna_mista = True
#hra
'''
def hra():
    global mys_y, mys_x, volna_mista, radek, sloupec, klik
    moje_rada = True
    klik = False
    while volna_mista == True:
        if moje_rada == True:
            hraluz = False
            while hraluz == False:
                #get intput, if free, place
                if klik == True:
                    if pole[radek][sloupec] == 0:
                        hraluz = True
                    else:
                        klik = False
            obraz.blit(o_ikonka, (zacatky[sloupec], zacatky[radek]))
            pygame.display.flip()

            if 0 not in pole:
                volna_mista = False
            moje_rada = False
        if volna_mista == True:
            bot()
'''
def hra():
    pass
def bot():
    pass    #if 2 in row, place third (to win or block), else choose random

#gameloop
while running:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if klik == False:
                mys_x, mys_y = pygame.mouse.get_pos()
                if 30 < mys_x < 480 and 30 < mys_y < 480:   #get radek a sloupec kliknuti
                    sloupec = 0 if mys_x < 180 else 1 if mys_x < 320 else 2
                    radek = 0 if mys_y < 180 else 1 if mys_y < 320 else 2
                    klik = True
                    '''
                    obraz.blit(o_ikonka, (zacatky[sloupec], zacatky[radek]))
                    pygame.display.flip()
                '''
    hra()