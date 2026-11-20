import pygame
import random
pygame.init()
running = True

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
hrac_na_rade = True
need_pos = True
#hra
def hra():      #!!!!add checking for draw (or victory)
    global hrac_na_rade, need_pos
    #if my turn, get inupt, check if its valid, make it, check for victory or draw
    if any(0 in radek for radek in pole):
        if hrac_na_rade == True:    #pokud hraje hrac
            if need_pos == False:   #na neco kliknul
                if pole[radek][sloupec] != 0:       #posral to, potrebuju novy input
                    need_pos = True
                else:       #je to volne pole
                    pole[radek][sloupec] = 1    #write it in pole
                    obraz.blit(o_ikonka, (zacatky[sloupec], zacatky[radek]))        #show it on screen
                    pygame.display.flip()
                    hrac_na_rade = False
        else:
            bot()

def bot():
    global bot_radek, bot_sloupec, hrac_na_rade, need_pos
    #pass    #if 2 in row, place third (to win or block), else choose random
    bot_radek = random.randint(0, 2)
    bot_sloupec = random.randint(0,2)
    while pole[bot_radek][bot_sloupec] != 0:
        bot_radek = random.randint(0, 2)
        bot_sloupec = random.randint(0,2)
    pole[bot_radek][bot_sloupec] = 2
    obraz.blit(x_ikonka, (zacatky[bot_sloupec], zacatky[bot_radek]))        #show it on screen
    pygame.display.flip()
    hrac_na_rade = True
    need_pos = True

#gameloop
while running:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mys_x, mys_y = pygame.mouse.get_pos()
            if 30 < mys_x < 480 and 30 < mys_y < 480 and need_pos == True:   #get radek a sloupec kliknuti
                sloupec = 0 if mys_x < 180 else 1 if mys_x < 320 else 2
                radek = 0 if mys_y < 180 else 1 if mys_y < 320 else 2
                need_pos = False
    hra()