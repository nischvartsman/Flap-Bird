import pygame
import flappy
from configuracoes import DIR_IMG, DT, LARGURA, ALTURA 
from os import path
from elementos import ALTURA_G, LARGURA_G, GALINHA, CHAO

class Player(pygame.sprite.Sprite):
    def __init__(self, grupo):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(path.join(DIR_IMG,GALINHA,'galinha.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (LARGURA_G, ALTURA_G))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA - LARGURA_G/2
        self.rect.bottom = CHAO
        self.speedx = 0
        self.speedy = 0
        self.groups = grupo
        self.click = False

        self.y_gravidade = 2
        self.chao = CHAO

    def movimento_vertical(self):
        self.speedy += self.y_gravidade
        if self.speedy > 20*DT:
            self.speedy = 20*DT
        if self.rect.bottom > self.chao:
            self.no_chao = True
            self.speedy = 0
            self.rect.bottom = self.chao
        
    def update(self):
        
        self.rect.x += self.speedx
        self.rect.bottom += self.speedy

            