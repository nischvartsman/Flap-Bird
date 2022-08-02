import flappy
from configuracoes import DIR_IMG, DT, LARGURA, ALTURA 
from os import path
from elementos import ALTURA_G, LARGURA_G, GALINHA, CHAO

class Player(flappy.sprite.Sprite):
    def __init__(self, grupo):
        flappy.sprite.Sprite.__init__(self)
        self.imagens = []
        for i in range(0,2):
            self.image = flappy.image.load(path.join(DIR_IMG,GALINHA,'galinha.png'.format(i) )).convert_alpha()
            self.image = flappy.transform.scale(self.image, (LARGURA_G, ALTURA_G))
            self.imagens.append(self.image)

        self.mask = flappy.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA - LARGURA_G/2
        self.rect.bottom = CHAO
        self.speedx = 0
        self.speedy = 0
        self.groups = grupo

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

        if self.speedx < 0:
            self.image = self.imagens[1]
        if self.speedx > 0:
            self.image = self.imagens[0]
            