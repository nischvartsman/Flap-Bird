#from email.headerregistry import Group
#from matplotlib.pyplot import hist
import pygame
from configuracoes import *
from elementos import *
from classes import Level, Player, Tronco, Pontuacao, Ovo
import time
import random

def gameplay(janela):
    
    clock = pygame.time.Clock()
    
    plano_jogo = pygame.image.load(path.join(DIR_IMG, 'fundo_fazenda.jpg')).convert()
    plano_jogo = pygame.transform.scale(plano_jogo, (LARGURA,ALTURA))

    fonte = pygame.font.SysFont("comicsansms", 60)
    assets = som_assets()
    
    #criando grupos
    chicken_group = pygame.sprite.Group() #grupo jogador
    jogador = Player()
    chicken_group.add(jogador)

    tronco_group = pygame.sprite.Group() #grupo tronco

    ovo_group = pygame.sprite.Group()  #grupo ovo

    

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
        
        colisao = pygame.sprite.spritecollide(jogador,ovo_group,True,pygame.sprite.collide_mask) #colisao tronco e galinha
        hits = pygame.sprite.spritecollide(jogador,tronco_group,True,pygame.sprite.collide_mask) #colisao galinha e ovo
        
        if len(colisao) > 0:  #caso haja colisao com o ovo
            Pontuacao.pontos += 500*len(colisao)
            assets['galinha'].play()
            print('pegou ovo')
        
        if len(hits) > 0:  #caso haja colisao com o tronco
            Pontuacao.pontos -= 1000*len(hits)
            assets['colisao'].play()
            print('Bateu')

        tempo_final = time.time()

        if tempo_final - tempo_inicial > tempo_espera:
            #definindo velocidade do jogo 
            max = 3
            if Level.level > 5:
                max = 2
            if Level.level > 6:
                max = 1.5
            if Level.level > 7:
                max = 1
            if Level.level > 8:
                max = 0.8
            
            #gerando troncos
            tempo_espera = random.uniform(0.5,max)
            tempo_inicial = tempo_final
            tronco1  = Tronco(False)
            tronco2 = Tronco(True)
            tronco_group.add(tronco1)
            tronco_group.add(tronco2)
            
            #gerando ovos
            if random.uniform(0,1) < 0.3:
                ymin = tronco2.rect[1] + tronco2.rect[3]
                ymax = tronco1.rect[1]
                ovo = Ovo(ymin,ymax)
                ovo_group.add(ovo)


        janela.blit(plano_jogo,(0,0))

        pontos = fonte.render('{:04d}'.format(Pontuacao.pontos) , True, (0,0,0)) #imprime pontuação

        janela.blit(pontos,(100,100))

        #update dos grupos
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