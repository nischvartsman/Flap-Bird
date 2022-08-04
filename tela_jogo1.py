from email.headerregistry import Group
from matplotlib.pyplot import hist
import pygame
from configuracoes import *
from classes import Level, Player, Tronco, Pontuacao, Ovo
import time
import random

def gameplay(janela):
    clock = pygame.time.Clock()
    #janela = pygame.display.set_mode((LARGURA,ALTURA))
    plano_jogo = pygame.image.load(path.join(DIR_IMG, 'fundo_fazenda.jpg')).convert()
    plano_jogo = pygame.transform.scale(plano_jogo, (LARGURA,ALTURA))

    fonte = pygame.font.SysFont("comicsansms", 60)

    chicken_group = pygame.sprite.Group()
    jogador = Player()
    chicken_group.add(jogador)

    tronco_group = pygame.sprite.Group()

    ovo_group = pygame.sprite.Group()
    #ovo = Ovo()
    #ovo_group.add(ovo)
    

    tempo_inicial = time.time()

    tempo_espera = 0

    estado = GAME

    Pontuacao.pontos = 0

    while estado == GAME:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                estado = QUIT

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jogador.fly()
        
        colisao = pygame.sprite.spritecollide(jogador,ovo_group,True,pygame.sprite.collide_mask)
        hits = pygame.sprite.spritecollide(jogador,tronco_group,True,pygame.sprite.collide_mask)
        
        if len(colisao) > 0:
            Pontuacao.pontos += 500*len(colisao)
            print('pegou ovo')
        
        if len(hits) > 0:
            Pontuacao.pontos -= 1000*len(hits)
            print('Bateu')

        tempo_final = time.time()

        if tempo_final - tempo_inicial > tempo_espera:
        
            tempo_espera = random.uniform(1,3)
            tempo_inicial = tempo_final
            tronco1  = Tronco(False)
            tronco2 = Tronco(True)
            tronco_group.add(tronco1)
            tronco_group.add(tronco2)
            
            if random.uniform(0,1) < 0.3:
                ymin = tronco2.rect[1] + tronco2.rect[3]
                ymax = tronco1.rect[1]
                ovo = Ovo(ymin,ymax)
                ovo_group.add(ovo)


        janela.blit(plano_jogo,(0,0))

        pontos = fonte.render('{:04d}'.format(Pontuacao.pontos) , True, (0,0,0))

        janela.blit(pontos,(100,100))

        chicken_group.update()

        chicken_group.draw(janela)

        tronco_group.update()

        tronco_group.draw(janela)

        ovo_group.update()

        ovo_group.draw(janela)

        pygame.display.update()

        

        if Pontuacao.pontos < 0:
            print('perdeu')
            estado = GAME_OVER

    return estado 