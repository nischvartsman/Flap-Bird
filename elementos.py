from os import path
import pygame
from configuracoes import ALTURA, SND_DIR

#definindo elementos do jogo

  


GALINHA = 'galinha.png'
LARGURA_G = 150
ALTURA_G = 165

PLANO_DE_FUNDO = 'fundo_fazenda.jpg'

CHAO = 740

TRONCO = 'tronco_arvore.png'
LARGURA_T = 150
ALTURA_T = 165

OVO = 'ovo.png'
LARGURA_OVO = 30
ALTURA_OVO = 50

def som_assets():
    assets = {}

    pygame.mixer.music.load(path.join(SND_DIR, 'fazendinha.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets['fazendinha'] = pygame.mixer.Sound(path.join(SND_DIR, 'fazendinha.wav'))
    assets['galinha'] = pygame.mixer.Sound(path.join(SND_DIR,'galinha.wav'))
    assets[ 'colisao'] = pygame.mixer.Sound(path.join(SND_DIR,'colisao_galinha.wav'))
    assets['game over'] = pygame.mixer.Sound(path.join(SND_DIR, 'game_over.wav'))

    return assets
