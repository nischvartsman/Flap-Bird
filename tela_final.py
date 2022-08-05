import pygame
from elementos import som_assets
from os import path
from configuracoes import ALTURA, DIR_IMG,FPS, GAME_OVER, LARGURA, QUIT, GAME, PRETO, VEL
from classes import Level

def gameover(janela):
    #carrega elementos da tela final
    tempo_fps = pygame.time.Clock()
    plano_over = pygame.image.load(path.join(DIR_IMG, 'fundo_over.png')).convert()
    plano_over = pygame.transform.scale(plano_over, (LARGURA,ALTURA))
    pdf_rect = plano_over.get_rect()
    assets = som_assets()

    rodando = GAME_OVER

    todos_sprites = pygame.sprite.Group()
    tocando = False
    while rodando == GAME_OVER: #looping da tela final
        
        if tocando == False:
            assets['game over'].play(loops = -1) #toca música da tela final
            tocando = True
        
        tempo_fps.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = QUIT
                 
            if evento.type == pygame.KEYDOWN:  #quando aperta espaço o jogo reinicia
                if evento.key == pygame.K_SPACE:
                    rodando = GAME
                    Level.level = VEL
                    assets['game over'].stop()
            
    
        todos_sprites.update() #atualiza todos os sprites 

        janela.fill(PRETO)  
        janela.blit(plano_over, pdf_rect)

        todos_sprites.draw(janela)

        pygame.display.update()

    return rodando