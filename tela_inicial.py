from asyncore import loop
import pygame
from os import path
from configuracoes import *
from elementos import *

def tela_inicial(janela):
    
    # definindo configuracoes da tela inicial
    
    assets = som_assets()
    tempo_fps = pygame.time.Clock()
    plano_de_fundo = pygame.image.load(path.join(DIR_IMG,'fundo_inicial.jpg')).convert()
    plano_de_fundo = pygame.transform.scale(plano_de_fundo,(LARGURA,ALTURA))
    pdf_rect = plano_de_fundo.get_rect()
    fonte = pygame.font.SysFont("comicsansms", 60)
    titulo = fonte.render('Flappy Chicken', True, (0,0,0))
    titulo = pygame.transform.scale(titulo,(300,100))
    integrante1 = fonte.render('Nina Schvartsman', True, (0,0,0))
    integrante1 = pygame.transform.scale(integrante1,(200,28))
    integrante2 = fonte.render('Mariana Albuquerque', True, (0,0,0))
    integrante2 = pygame.transform.scale(integrante2, (220,30))
    trabalho =  fonte.render('Aperte espaço para iniciar', True, (0,0,0))
    trabalho = pygame.transform.scale(trabalho, (230,45))

    todos_sprites = pygame.sprite.Group()
    grupo = {}
    grupo['todos_sprites'] = todos_sprites

    rodando = True
    tocando = False
    while rodando:
        if tocando == False:
            assets['fazendinha'].play(loops = -1)
            tocando = True
        
        tempo_fps.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                estado = QUIT
                rodando = False
            
            if evento.type == pygame.KEYUP:

                if evento.key == pygame.K_SPACE:

                    estado = GAME
                    rodando = False
                    assets['fazendinha'].stop()
                    
                        
                        
        todos_sprites.update()

        janela.fill(PRETO)  
        janela.blit(plano_de_fundo, pdf_rect)
        janela.blit(titulo, (520,300))
        janela.blit(integrante1, (0,655))
        janela.blit(integrante2, (0,685))
        janela.blit(trabalho, (560,420))

        todos_sprites.draw(janela)

        pygame.display.update()

    return estado