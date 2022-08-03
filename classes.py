import pygame
from configuracoes import *
from os import path
from configuracoes import DIR_IMG
from elementos import CHAO, LARGURA_G

janela = pygame.display.set_mode((LARGURA,ALTURA))
GALINHA = pygame.image.load(path.join(DIR_IMG,'galinha.png')).convert_alpha()
GALINHA = pygame.transform.scale(GALINHA,(150,165))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = GALINHA
        self.rect = self.image.get_rect()
        self.speedy = 0
        self.rect.centerx = LARGURA/2 - LARGURA_G
        self.rect.centery = ALTURA/2
        self.rect.bottom = CHAO
        self.y_gravidade = 2


    def fly(self):
        self.speedy -= 150
        

    def update(self):
        self.rect.centery += 1 #gravité
    
    