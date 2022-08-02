import pygame
#from classes import Plataforma, Player1, Player2
from configuracoes import ALTURA, DIR_IMG,DT,FPS, GAME_OVER, LARGURA,PRETO,QUIT,GAME
from os import path
from elementos import ALTURA_G
#import Musicas as mus

def gameplay(janela):

    tempo_fps = pygame.time.Clock()
    plano_jogo = pygame.image.load(path.join(DIR_IMG, 'fundo_fazenda.jpg')).convert()
    plano_jogo = pygame.transform.scale(plano_jogo, (LARGURA,ALTURA))

    todos_sprites = pygame.sprite.Group()
    jogadores = pygame.sprite.Group()

    grupo = {}
    grupo['todos_sprites'] = todos_sprites

    #jogador1 = Player1(grupo)
    #todos_sprites.add(jogador1)
    #jogadores.add(jogador1)

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
                if evento.type == pygame.KEYDOWN: 
                    tecla[evento.key] = True
                    if evento.key == pygame.K_UP:
                        #jogador1.jump()
                if evento.type == pygame.KEYUP:
                    if evento.key in tecla and tecla[evento.key]:
                        if evento.key == pygame.K_LEFT:
                                    #jogador1.speedx += 8*DT
                                    
                        if evento.key == pygame.K_RIGHT:
                            #jogador1.speedx -= 8*DT
                                        
                        if evento.key == pygame.K_DOWN:
                            encima1 = True