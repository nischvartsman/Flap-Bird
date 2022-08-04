import pygame
from configuracoes import *
from os import path
from configuracoes import DIR_IMG
from elementos import ALTURA_OVO, CHAO, LARGURA_G, LARGURA_OVO, TRONCO
import random

janela = pygame.display.set_mode((LARGURA,ALTURA))

GALINHA = pygame.image.load(path.join(DIR_IMG,'galinha.png')).convert_alpha()
GALINHA = pygame.transform.scale(GALINHA,(150,165))

TRONCO =pygame.image.load(path.join(DIR_IMG,'tronco_arvore.png')).convert_alpha()
TRONCO = pygame.transform.scale(TRONCO,(150,400))

OVO = pygame.image.load(path.join(DIR_IMG,'ovo.png')).convert_alpha()
OVO = pygame.transform.scale(OVO,(LARGURA_OVO,ALTURA_OVO))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = GALINHA
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.speedy = VEL
        self.rect.centerx = LARGURA/2 - LARGURA_G
        self.rect.centery = ALTURA/2
        #self.rect.bottom = CHAO
        self.y_gravidade = 2
        self.topo = 0


    def fly(self):
        self.speedy = - 1
        self.topo = self.rect.centery - 100
        

    def update(self):
        self.rect.centery += self.speedy
        if self.speedy > 0:
            self.speedy += GRAVIDADE 
        else:
            self.speedy -= GRAVIDADE
        if self.rect.centery < self.topo:
            self.speedy = 1
        if self.rect.centery > CHAO:
            self.rect.centery = CHAO



class Tronco(pygame.sprite.Sprite):
    def __init__(self,invertido):
        pygame.sprite.Sprite.__init__(self)
        self.image = TRONCO
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = LARGURA

        ytronco = random.randint(70,300)

        if invertido:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = - (self.rect[3] - ytronco)
        else:
            self.rect[1] = ALTURA - ytronco
        
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect[0] -= Level.level
        if self.rect.x < 0:
            Level.level += 0.1
            Pontuacao.pontos += 50
            self.kill()
        
class Pontuacao():
    pontos = 0

class Level():
    level = VEL

class Ovo(pygame.sprite.Sprite):
    def __init__(self, ymin, ymax):
        pygame.sprite.Sprite.__init__(self)
        self.image = OVO
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = LARGURA
        self.rect.y = random.randint(ymin + ALTURA_OVO ,ymax - ALTURA_OVO)
         
       # self.last_update = pygame.time.get_ticks()  #guarda o momento que a imagem for mostrada
    def update(self):
        self.rect[0] -= Level.level
        if self.rect.x < 0:
            
            self.kill()

