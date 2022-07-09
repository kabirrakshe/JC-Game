import pygame
import random
##Credits to https://www.chosic.com/free-music/all/ for the background music
#Credits to pixabay for sound effectsa
from pygame import mixer
pygame.init()
pygame.display.init()
canvas = pygame.display.set_mode((1439,845))
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
mixer.init()
# mixer.music.load('medievalmusic.mp3')
# mixer.music.set_volume(0.10)
# mixer.music.play()

movecounter= 0

heal = pygame.transform.smoothscale(pygame.image.load('heal.png'), (115, 65))
arrows = pygame.transform.smoothscale(pygame.image.load('arrows.png'), (115, 127))

selected = False
background = pygame.image.load("rome.jpeg")
title = pygame.font.SysFont('Verdana', 50, bold = True)
titlerender = title.render("Caesar's Battle of t"
                           "he Greats", True, BLUE)
attributes = pygame.font.SysFont('comicsans', 20, bold = True,italic = True)
BRUTUS = pygame.transform.smoothscale(pygame.image.load("Brutus.png"), (140, 190))
CASCA = pygame.transform.smoothscale(pygame.image.load("Casca.png"), (140,190))
ANTONY = pygame.transform.smoothscale(pygame.image.load("Decius.png"), (140,190))
DECIUS = pygame.transform.smoothscale(pygame.image.load("antony.png"), (140,190))
SOOTHSAYER = pygame.transform.smoothscale(pygame.image.load("Soothslayer.png"), (140,190))
CINNA = pygame.transform.smoothscale(pygame.image.load("Cinna.png"), (140,190))
ARCHER = pygame.transform.smoothscale(pygame.image.load("Archer.png"), (140,190))
CALPHURNIA = pygame.transform.smoothscale(pygame.image.load("Calphurnia.png"), (140,190))
class card():
    selected = False
    selectedcard = None
    counter = 0
    limit = False
    def __init__(self, x, y,health, damage=None, description = None, name = None, attack = None, prgm = None):
        self.x = x
        self.y = y
        self.description = description
        self.selection = False
        self.health = health
        self.damage = damage
        self.attack = attack
        self.name = name
        self.prgm = prgm
    def drawcard(self, askforheal):
        global movecounter
        finalask = False
        dname = attributes.render('Name: ' + str(self.description['name']), True, RED)
        dhealth = attributes.render('Health: ' + str(self.description['health']), True, RED)
        dattack = attributes.render('Attack: ' + str(self.description['attack']), True, RED)
        if self.selection == True:
            if self.selection and cardopp.selected:
                card.counter+=1
                if card.counter > 50:
                    self.selection = False
                    card.selected = False
                    card.selectedcard = None
                    card.counter = 0
                    card.limit = True
            pygame.draw.rect(canvas, GREEN, (self.x - 6, self.y - 6, 175, 230), 5)
            pygame.draw.rect(canvas, RED, (self.x, self.y, 165, 220))
            if self.description['main']: canvas.blit(self.description['main'], (self.x + 5, self.y + 5))
            pygame.draw.rect(canvas, GREEN, (self.x, self.y - 20, self.health, 15))
            canvas.blit(dname, (self.x, self.y - 120))
            canvas.blit(dhealth, (self.x, self.y - 100))
            canvas.blit(dattack, (self.x, self.y - 80))
            if askforheal == True and self.health > 0:
                canvas.blit(heal, (self.x, self.y))

            return
        xcoord, ycoord = pygame.mouse.get_pos()
        if xcoord in range(self.x, self.x + 150) and ycoord in range(self.y, self.y + 200) and not card.selected and self.health > 0:
            pygame.draw.rect(canvas, RED, (self.x, self.y, 165, 220))
            canvas.blit(dname, (self.x, self.y - 120))
            canvas.blit(dhealth, (self.x, self.y - 100))
            canvas.blit(dattack, (self.x, self.y - 80))
            if askforheal == True: finalask = True
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if askforheal == True:
                        finalask = True
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('bandageseffect.mp3'))
                        self.health+=30
                        movecounter += 1
                        canvas.blit(self.description['main'], (self.x + 5, self.y + 5))
                        pygame.draw.rect(canvas, GREEN, (self.x, self.y - 20, self.health, 15))
                        if finalask == True:
                            canvas.blit(heal, (self.x, self.y))
                        return False
                    card.counter = 0
                    self.selection = True
                    card.selected = True
                    card.selectedcard = self

        else:
            pygame.draw.rect(canvas, RED, (self.x,self.y,150,200))
        canvas.blit(self.description['main'], (self.x+5, self.y+5))
        pygame.draw.rect(canvas, GREEN, (self.x, self.y - 20,self.health,15))
        if finalask == True:
            canvas.blit(heal, (self.x,self.y))

def Deciusp(card1, card2):
    card1dupdescription = card1.description.copy()
    card1health = int(str(card1.health)[:])
    card1prgm = card1.prgm
    setattr(card1, 'health', card2.health)
    setattr(card2, 'health', card1health)
    setattr(card1, 'description', card2.description)
    setattr(card2, 'description', card1dupdescription)
    setattr(card1, 'prgm', card2.prgm)
    setattr(card2, 'prgm',card1prgm )


def Brutusp(card1, card2):
    card2.health -= card1.description['damage']

def Cascap(card1, card2):
    card2.health -= card1.description['damage']

def Cinnap(card1, card2):
    choice = random.randint(0,1)
    if choice == 0:
        card2.health = 0
    if choice == 1:
        card1.health = 0

def Archerp(card1, card2):
    card2.health -= card1.description['damage']

def Soothsayerp(card1, card2):
    card2.prgm(card1, card2)
def Antonyp(card1, card2):
    card2.health//=2

def Calphurniap(card1, card2):
    card1.health, card2.health = card2.health, card1.health


class cardopp(card):
    selected = False
    def drawcard(self, askforarrows):
        global movecounter

        finalask = False
        xcoord, ycoord = pygame.mouse.get_pos()
        if self.selection == True:
            if card.limit == True:
                self.selection = False
                cardopp.selected = False
                card.limit = False
            pygame.draw.rect(canvas, GREEN, (self.x - 6, self.y - 6, 175, 230), 5)
            pygame.draw.rect(canvas, RED, (self.x, self.y, 165, 220))
            if self.description['main']: canvas.blit(self.description['main'], (self.x + 5, self.y + 5))
            pygame.draw.rect(canvas, GREEN, (self.x, self.y - 20, self.health, 15))

            return
        pygame.draw.rect(canvas, RED, (self.x, self.y, 150, 200))
        if xcoord in range(self.x, self.x + 150) and ycoord in range(self.y, self.y + 200) and askforarrows: finalask = True
        if xcoord in range(self.x, self.x + 150) and ycoord in range(self.y, self.y + 200) and cardopp.selected == False:
            pygame.draw.rect(canvas, RED, (self.x, self.y, 165, 220))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if askforarrows == True:
                        self.health -= 30
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('arroweffect.mp3'))
                        movecounter += 1
                        if self.description['main']: canvas.blit(self.description['main'], (self.x + 5, self.y + 5))#
                        pygame.draw.rect(canvas, GREEN, (self.x, self.y - 20, self.health, 15))
                        if finalask == True: canvas.blit(arrows, (self.x, self.y))#
                        return False
                    elif card.selected == True:
                        card.selectedcard.prgm(card.selectedcard,self)
                        self.selection = True
                        cardopp.selected = True
                        movecounter+=1
        else:
            pygame.draw.rect(canvas, RED, (self.x, self.y, 150, 200))
        if self.description['main']: canvas.blit(self.description['main'], (self.x+5, self.y+5))
        pygame.draw.rect(canvas, GREEN, (self.x, self.y - 20,self.health,15))
        if finalask==True: canvas.blit(arrows, (self.x,self.y))


class deck():
    def __init__(self):
        self.carddeck = pygame.transform.smoothscale(pygame.image.load('carddeck.png'), (172, 220))
        self.carddeckmega = pygame.transform.smoothscale(pygame.image.load('carddeck.png'), (215, 275))
        choices = [heal, arrows]
        self.cards = [random.choice(choices) for i in range(10)]

    def drawdeck(self):
        global movecounter
        x, y = pygame.mouse.get_pos()
        if x in range(1285, 1425) and y in range(628,833):
            canvas.blit(self.carddeckmega, (1220, 570))
            pygame.draw.rect(canvas, GREEN, (1235, 578, 183, 270), 1)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return self.pickcard()

        else:
            canvas.blit(self.carddeck, (1270, 620))
            pygame.draw.rect(canvas, GREEN, (1285, 628, 140, 205), 1)

        powerupsleft = title.render(str(len(self.cards)), True, GREEN)
        canvas.blit(powerupsleft, (1300, 550))
    def pickcard(self):
        drawn = self.cards[-1]
        self.cards.pop()
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('popeffect.mp3'))
        return drawn
def main():
    global movecounter
    casca = {'main': CASCA, 'name': 'casca', 'damage': 20, 'health': 150, 'attack': 'Stab'}
    brutus = {'main': BRUTUS, 'name': 'brutus', 'damage': 30, 'health': 200, "attack": 'Stab'}
    cinna = {'main': CINNA, 'name': 'cinna', 'damage': 10, 'health': 125, 'attack': 'Bribe'}
    decius = {'main': DECIUS, 'name': 'decius', 'damage': 10, 'health': 100, 'attack': 'Betrayal'}
    soothsayer = {'main': SOOTHSAYER, 'name': 'soothsayer', 'damage': 20, 'health': 100, 'attack': 'Steal'}
    antony = {'main': ANTONY, 'name': 'antony', 'damage': 30, 'health': 250, 'attack': 'Slay'}
    archer = {'main': ARCHER, 'name': 'archer', 'damage': 40, 'health': 150, 'attack': 'Shoot'}
    calphurnia = {'main':CALPHURNIA, 'name': 'calphurnia', 'damage': 10, 'health': 100, 'attack': 'Seduce'}
    card1 = card(100, 600,health=casca['health'], description = casca, prgm = Cascap)
    card2 = card(400, 600, health=brutus['health'],description = brutus, prgm =  Brutusp)
    card3 = card(700, 600, health=cinna['health'],description = cinna, prgm = Cinnap)
    card4 = card(1000, 600,health=decius['health'], description = decius, prgm = Deciusp)
    card5 = cardopp(100, 100, health=soothsayer['health'],description = soothsayer, prgm = Soothsayerp)
    card6 = cardopp(400, 100, health = antony['health'], description = antony, prgm = Antonyp)
    card7 = cardopp(700, 100, health = calphurnia['health'], description = calphurnia, prgm = Calphurniap)
    card8 = cardopp(1000, 100, health = archer['health'], description = archer, prgm = Archerp)
    powerupsplayer1 = deck()
    powerupsplayer2 = deck()
    askforheal = False
    askforarrows = False
    powerups = [powerupsplayer1, powerupsplayer2]
    selectedpowerup = 0
    activated = False
    def switchsides(powerupask):
        card1des = card1.description.copy()
        card1health = int(str(card1.health)[:])
        card1prgm = card1.prgm
        card2des = card2.description.copy()
        card2health = int(str(card2.health)[:])
        card2prgm = card2.prgm
        card3des = card3.description.copy()
        card3health = int(str(card3.health)[:])
        card3prgm = card3.prgm
        card4des = card4.description.copy()
        card4health = int(str(card4.health)[:])
        card4prgm = card4.prgm

        setattr(card1, 'description', card5.description)
        setattr(card1, 'health', card5.health)
        setattr(card1, 'prgm', card5.prgm)
        setattr(card2, 'description', card6.description)
        setattr(card2, 'health', card6.health)
        setattr(card2, 'prgm', card6.prgm)
        setattr(card3, 'description', card7.description)
        setattr(card3, 'health', card7.health)
        setattr(card3, 'prgm', card7.prgm)
        setattr(card4, 'description', card8.description)
        setattr(card4, 'health', card8.health)
        setattr(card4, 'prgm', card8.prgm)

        setattr(card5, 'description', card1des)
        setattr(card5, 'health', card1health)
        setattr(card5, 'prgm', card1prgm)
        setattr(card6, 'description', card2des)
        setattr(card6, 'health', card2health)
        setattr(card6, 'prgm', card2prgm)
        setattr(card7, 'description', card3des)
        setattr(card7, 'health', card3health)
        setattr(card7, 'prgm', card3prgm)
        setattr(card8, 'description', card4des)
        setattr(card8, 'health', card4health)
        setattr(card8, 'prgm', card4prgm)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('clickeffect.mp3'))
        if powerupask == 0: return 1
        if powerupask == 1: return 0




    while True:
        # if not mixer.music.get_busy():
        #     mixer.music.rewind()
        #     mixer.music.play()
        canvas.fill((0, 0, 0))
        canvas.blit(background, (0,0))
        canvas.blit(titlerender, (300,0))
        if movecounter ==3:
            selectedpowerup = switchsides(selectedpowerup)
            movecounter = 0
        if card1.drawcard(askforheal) == False: askforheal = False
        if card2.drawcard(askforheal) == False: askforheal = False
        if card3.drawcard(askforheal) == False: askforheal = False
        if card4.drawcard(askforheal) == False: askforheal = False
        if card5.drawcard(askforarrows) == False: askforarrows = False
        if card6.drawcard(askforarrows) == False:askforarrows = False
        if card7.drawcard(askforarrows) == False:askforarrows = False
        if card8.drawcard(askforarrows) == False:askforarrows = False
        chosenpower = powerups[selectedpowerup].drawdeck()
        if chosenpower == None: activated = False
        else:activated = True
        if activated == True:
            if chosenpower == heal:
                askforheal = True
                askforarrows = False
            elif chosenpower == arrows:
                askforarrows = True
                askforheal = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT: break




        pygame.display.update()

main()