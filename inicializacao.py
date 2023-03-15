import pygame
from classes import Player


def criando_grupos():
    #criando grupos
    chicken_group = pygame.sprite.Group() #grupo jogador
    jogador = Player()
    chicken_group.add(jogador)

    tronco_group = pygame.sprite.Group() #grupo tronco

    ovo_group = pygame.sprite.Group()  #grupo ovo

    return chicken_group, tronco_group, ovo_group,jogador
