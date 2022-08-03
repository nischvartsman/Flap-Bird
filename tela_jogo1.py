import pygame
from configuracoes import *
from classes import Player

chicken_group = pygame.sprite.Group()
jogador = Player()
chicken_group.add(jogador)

def gameplay(janela):
    #janela = pygame.display.set_mode((LARGURA,ALTURA))
    plano_jogo = pygame.image.load(path.join(DIR_IMG, 'fundo_fazenda.jpg')).convert()
    plano_jogo = pygame.transform.scale(plano_jogo, (LARGURA,ALTURA))


    while True:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:

                    jogador.fly()



        janela.blit(plano_jogo,(0,0))

        chicken_group.update()

        chicken_group.draw(janela)

        pygame.display.update()