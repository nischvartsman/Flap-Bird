from os import path
import pygame
from configuracoes import INIC, LARGURA, ALTURA, GAME, QUIT, GAME_OVER
import tela_inicial as In
#import Tela_de_jogo as Tj
#from elementos import MUSICA_MENU
#import Musicas as mus
#import finalização as fim

pygame.init()
pygame.mixer.init()

janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Flappy Chicken')

game = INIC
while game != QUIT:
    
    if game == INIC:
        game = In.tela_inicial(janela)

    pygame.display.update()  