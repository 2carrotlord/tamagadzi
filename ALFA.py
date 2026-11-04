#knihovny
import pygame 
import os
import sys
import time
import random

#obrazovka
pygame.init()
obrazovka = pygame.display.set_mode((300,420))
pygame.display.set_caption("Tamogatchi")

#čas
cas = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 200)
play_time = 0

#fonty
font = pygame.font.SysFont("Consolas", 20)
font_button = pygame.font.SysFont("Consolas", 30)

#Načítání obrázků 
CESTA_K_KODU = os.path.dirname(os.path.abspath(__file__))
Slozka_s_obrazky_staty = os.path.join(CESTA_K_KODU, "obrazky_staty")
Slozka_s_obrazky_mazlicek = os.path.join(CESTA_K_KODU, "obrazky_mazliček")

#jídlo
hunger_obrazek_1 = pygame.image.load(os.path.join(Slozka_s_obrazky_staty, "hunger_1.png")).convert_alpha()
hunger_stav_1 = pygame.transform.scale(hunger_obrazek_1, (40,40))
hunger_obrazek_2 = pygame.image.load(os.path.join(Slozka_s_obrazky_staty, "hunger_2.png")).convert_alpha()
hunger_stav_2 = pygame.transform.scale(hunger_obrazek_2, (40,40))
hunger_obrazek_3 = pygame.image.load(os.path.join(Slozka_s_obrazky_staty, "hunger_3.png")).convert_alpha()
hunger_stav_3 = pygame.transform.scale(hunger_obrazek_3, (40,40))

#voda
voda_obrazek_1 = pygame.image.load(os.path.join(Slozka_s_obrazky_staty, "voda_1.png")).convert_alpha()
voda_stav_1 = pygame.transform.scale(voda_obrazek_1, (40,40))
voda_obrazek_2 = pygame.image.load(os.path.join(Slozka_s_obrazky_staty, "voda_2.png")).convert_alpha()
voda_stav_2 = pygame.transform.scale(voda_obrazek_2, (40,40))
voda_obrazek_3 = pygame.image.load(os.path.join(Slozka_s_obrazky_staty, "voda_3.png")).convert_alpha()
voda_stav_3 = pygame.transform.scale(voda_obrazek_3, (40,40))


#staty
counter_hlad = 100
text_hlad_cislo = "100"
hlad_text = font.render("jídlo", True, (0,0,0))

counter_voda = 100
text_voda_cislo = "100"
voda_text = font.render("voda", True, (0,0,0))

counter_spina = 0
text_spina_cislo = "0"
spina_text = font.render("špína", True, (0,0,0))



#odpad
odpadky = []
def pridat_odpad(pocet = 3):
    global novy_odpad
    for odp in range(pocet):
        x = random.choice([random.randint(0, 70), random.randint(200, 250)])
        y = random.randint(180,250)
        novy_odpad = pygame.Rect(x, y, 20, 20)
        odpadky.append(novy_odpad)

#mazlíček
class mazlicek(pygame.sprite.Sprite):
    def __init__(self, obrazky):
        super().__init__()
    
        obrazek_mazlicek = os.path.join(Slozka_s_obrazky_mazlicek, obrazky)
        cely_obrazek = pygame.image.load(obrazek_mazlicek).convert_alpha()
        
        sirka_obrazku = cely_obrazek.get_width()
        vyska_obrazku = cely_obrazek.get_height()
        
        pocet_snimku = 10
        self.sirka_snimku = sirka_obrazku // pocet_snimku
        self.vyska_snimku = vyska_obrazku
        
        self.snimky = []
        for i in range(pocet_snimku):
            x_pozice = i * self.sirka_snimku
            
            oblast = pygame.Rect(x_pozice, 0, self.sirka_snimku, self.vyska_snimku)
            snimek = cely_obrazek.subsurface(oblast)
            snimek = pygame.transform.scale(snimek, (self.sirka_snimku * 5, self.vyska_snimku * 5))
            self.snimky.append(snimek)
            
        self.aktualni_snimek = 0
        self.image = self.snimky[self.aktualni_snimek]
        self.rect = self.image.get_rect(center=(165, 190))
        
        self.rychlost_animace = 0.15
        
    def update(self):
        self.aktualni_snimek += self.rychlost_animace
        if self.aktualni_snimek >= len(self.snimky):
            self.aktualni_snimek = 0
        self.image = self.snimky[int(self.aktualni_snimek)]

#přidávání mazlíčků
vsichni_spritove = pygame.sprite.Group()
kocka = mazlicek("kocka.png")
vsichni_spritove.add(kocka)

#tlačítko
objects = []
class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, cooldown = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.cooldown = cooldown
        self.lastClickTime = 0
        self.alreadyPressed = False
        

        self.fillColors = {
            'normal': "#ffffff",
            'hover': '#666666',
            'pressed': '#333333',
            'cooldown': "#fd0303"
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonText = buttonText
        objects.append(self)
    #animace tlačítka 
    def process(self):
        mousePos = pygame.mouse.get_pos()
        currentTime = pygame.time.get_ticks()
        isOnCooldown = (currentTime - self.lastClickTime) < self.cooldown
        if isOnCooldown:
            self.buttonSurface.fill(self.fillColors['cooldown'])
        else:
            self.buttonSurface.fill(self.fillColors['normal'])
            if self.buttonRect.collidepoint(mousePos):
                self.buttonSurface.fill(self.fillColors['hover'])
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    self.buttonSurface.fill(self.fillColors['pressed'])
                    if not self.alreadyPressed:
                        if self.onclickFunction:
                            self.onclickFunction()
                        self.alreadyPressed = True
                        self.lastClickTime = currentTime
                    else:
                        self.alreadyPressed = False
                else:
                    self.alreadyPressed = False

        self.buttonSurf = font_button.render(self.buttonText, True, (20,20,20))
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        obrazovka.blit(self.buttonSurface, self.buttonRect)

#jidlo
def jidlo():
    global counter_hlad
    counter_hlad += 10
    pridat_odpad()

#voda
def voda():
    global counter_voda
    counter_voda += 10

#špína
def spina():
    global counter_spina 
    counter_spina -= 10

paused = True

#STOP
def stop():
    global paused
    paused = not paused

#tlačítka 
Button(55, 80, 80, 30, "Hlad", jidlo, cooldown = 1000)
Button(160, 80, 80, 30, "Voda", voda, cooldown = 1000)
Button(30, 285, 120, 30, "Uklidit", spina, cooldown = 2000)
Button(200, 285, 80, 30, "STOP", stop, cooldown = 1000)

run = True
while run:
    #pozadí
    obrazovka.fill ((255,255,255))
    text_spina_cislo = str(counter_spina) 
    for action in pygame.event.get():
    #měřič jídla a vody
        if paused:
            if action.type == pygame.USEREVENT:
                play_time = random.randint(1,50)
                if play_time == 1:
                    pridat_odpad()
                counter_hlad -=1
                text_hlad_cislo = str(counter_hlad)
                if counter_hlad <= 0:
                    text_hlad_cislo = "umřel"
                    run = False
                if counter_hlad > 100:
                    text_hlad_cislo = "překrmen"
                    run = False
                counter_voda -=1
                text_voda_cislo = str(counter_voda)
                if counter_voda <= 0:
                    text_voda_cislo = "umřel"
                    run = False
                if counter_voda > 100:
                    text_voda_cislo = "prasknul"
                    run = False
            if action.type == pygame.QUIT:
                run = False

        #odpad
            elif action.type == pygame.MOUSEBUTTONDOWN:
                if action.button == 1:
                    for odpad in odpadky[::-1]:
                        if odpad.collidepoint(action.pos):
                            counter_spina += 10                      
                            odpadky.remove(odpad)
    
        for odpad in odpadky:
            pygame.draw.rect(obrazovka, (150, 75, 0), odpad)
        if len(odpadky) > 10:
            print ("moc odpadků")
            run = False

    #statistika hladu, obrázek hladu
        if counter_hlad >= 80:
            obrazovka.blit(hunger_stav_1, (80,0))
        elif counter_hlad <= 80 and counter_hlad >= 50:
            obrazovka.blit(hunger_stav_2, (80,0))
        elif counter_hlad <= 50:
            obrazovka.blit(hunger_stav_3, (80,0))
    #statistika vody, obrázek vody        
        if counter_voda >= 80:
            obrazovka.blit(voda_stav_1, (180,0))
        elif counter_voda <= 80 and counter_voda >= 50:
            obrazovka.blit(voda_stav_2, (180,0))
        elif counter_voda <= 50:
            obrazovka.blit(voda_stav_3, (180,0))

    #text čísla pro vodu, jídlo, špína 
        obrazovka.blit(font.render(text_hlad_cislo, True,(0,0,0)), (85,60))
        obrazovka.blit(font.render(text_voda_cislo, True,(0,0,0)), (185,60))
        obrazovka.blit(font.render(text_spina_cislo, True,(0,0,0)), (85,315))
    #text jídla, vody, špíny 
        obrazovka.blit(hlad_text, (75,40))
        obrazovka.blit(voda_text, (175,40))
        obrazovka.blit(spina_text,(62,332))
    #update tlačítka 
        for object in objects:
            object.process()
    #update animace
        vsichni_spritove.update()
        vsichni_spritove.draw(obrazovka)
        pygame.display.flip()
        cas.tick(60)

pygame.quit()
sys.exit()