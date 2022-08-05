#importa bibliotecas necessárias
import pygame
from configuracoes import *
import tela_inicial as In
import tela_jogo1 as Tj
import tela_final as fim


pygame.init()
pygame.mixer.init()

janela = pygame.display.set_mode((LARGURA, ALTURA)) #cria janela no tamanho definido previamente no arquivo 'configuracoes.py'
pygame.display.set_caption('Flappy Chicken')

game = INIC

while game != QUIT: #looping principal do jogo
    
    if game == INIC:
        game = In.tela_inicial(janela) #carrega tela inicial e suas configuracoes
        
    elif game == GAME:
        game = Tj.gameplay(janela) #carrega tela de jogo e suas configuracoes
    
    elif game == GAME_OVER:
        game = fim.gameover(janela) #carrega tela de game over

    else:
        game == QUIT 
    
    pygame.display.update()  


pygame.quit()
