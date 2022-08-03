import pygame
from classes import  Player 
from configuracoes import ALTURA, DIR_IMG,DT,FPS, GAME_OVER, LARGURA,PRETO,QUIT,GAME
from os import path
from elementos import ALTURA_G
import random
#import Musicas as mus

game = True
def gameplay(janela):
    
    tempo_fps = pygame.time.Clock()
    plano_jogo = pygame.image.load(path.join(DIR_IMG, 'fundo_fazenda.jpg')).convert()
    plano_jogo = pygame.transform.scale(plano_jogo, (LARGURA,ALTURA))

    

    while game == GAME:
        tempo_fps.tick(FPS)

         
        janela.blit(plano_jogo, (0, 0))


        pygame.display.update()

    '''todos_sprites = pygame.sprite.Group()
    #jogadores = pygame.sprite.Group()

    grupo = {}
    grupo['todos_sprites'] = todos_sprites

    jogador = Player(grupo)
    todos_sprites.add(jogador)
    #jogadores.add(jogador)

   

    tecla = {}

    rodando = GAME
    while rodando != GAME_OVER and rodando != QUIT:
        tempo_fps.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = QUIT
            if rodando == GAME:
                if evento.type == pygame.MOUSEBUTTONDOWN: 
                    tecla[evento.key] = True
                    if evento.key == pygame.MOUSEBUTTONUP:
                        jogador.fly()
                '''