from os import path
import pygame
from configuracoes import *
import tela_inicial as In
import tela_jogo1 as Tj
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
    
    elif game == GAME:
        game = Tj.gameplay(janela)

    else:
        game == QUIT
    


    pygame.display.update()  
pygame.quit()
