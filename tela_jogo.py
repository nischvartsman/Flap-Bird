import pygame
from classes import  Player 
from configuracoes import ALTURA, DIR_IMG,DT,FPS, GAME_OVER, LARGURA,PRETO,QUIT,GAME
from os import path
from elementos import ALTURA_G
import random
#import Musicas as mus

def gameplay(janela):

    tempo_fps = pygame.time.Clock()
    plano_jogo = pygame.image.load(path.join(DIR_IMG, 'fundo_fazenda.jpg')).convert()
    plano_jogo = pygame.transform.scale(plano_jogo, (LARGURA,ALTURA))

    todos_sprites = pygame.sprite.Group()
    jogadores = pygame.sprite.Group()

    grupo = {}
    grupo['todos_sprites'] = todos_sprites

    jogador = Player(grupo)
    todos_sprites.add(jogador)
    jogadores.add(jogador)

    direcao1 = 'C'
    direcao2 = 'B'

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
                