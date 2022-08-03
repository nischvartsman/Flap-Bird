import pygame
from os import path
from configuracoes import ALTURA, DIR_IMG,FPS, GAME_OVER, LARGURA, QUIT, GAME, PRETO
from classes import Pontuacao

def gameover(janela):

    tempo_fps = pygame.time.Clock()
    plano_over = pygame.image.load(path.join(DIR_IMG, 'fundo_over.png')).convert()
    plano_over = pygame.transform.scale(plano_over, (LARGURA,ALTURA))
    pdf_rect = plano_over.get_rect()

    rodando = GAME_OVER

    todos_sprites = pygame.sprite.Group()

    while rodando == GAME_OVER:
        tempo_fps.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = QUIT
                 
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    rodando = GAME
            
    
        todos_sprites.update()

        janela.fill(PRETO)  
        janela.blit(plano_over, pdf_rect)

        todos_sprites.draw(janela)

        pygame.display.update()

    return rodando