from os import path
import pygame


DIR_IMG = path.join(path.dirname(__file__), 'imagens')

DT = 1.5
LARGURA = 1400
ALTURA = 780
FPS = 120

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
VEL = 3
GRAVIDADE = 0.1
V_TELA = 4.2
F_TRONCO = 1450
ULT_TRONCO = pygame.time.get_ticks() - F_TRONCO





