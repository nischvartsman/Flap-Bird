from os import path
import pygame
pygame.init()

DIR_IMG = path.join(path.dirname(__file__), 'imagens')

DT = 1.5
LARGURA = 1400
ALTURA = 780
FPS = 40

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

INIC = 0
GAME = 1
GAME_OVER = 2
QUIT = 3
VOANDO = False
V_TELA = 4.2
F_TRONCO = 1450
ULT_TRONCO = pygame.time.get_ticks() - F_TRONCO
PONTUACAO = 0

DESVIO = False


