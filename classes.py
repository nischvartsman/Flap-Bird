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
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.speedy = VEL
        self.rect.centerx = LARGURA/2 - LARGURA_G
        self.rect.centery = ALTURA/2
        self.rect.bottom = CHAO
        self.y_gravidade = 2


    def fly(self):
        self.speedy -= 10
        

    def update(self):
        self.speedy += GRAVIDADE #gravité
        self.rect.centery += self.speedy
    