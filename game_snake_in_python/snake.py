import pygame
import sys
import random
import os

import pygame.locals

largura = 1280
altura = 800

corpo_cobra = []
max_len_cobra = 0
morreu = True
score = 0

pygame.mixer.init() 
pygame.init()





musica_de_fundo = pygame.mixer.Sound(os.path.join(os.getcwd() , 'Jogo-da-cobrinha', 'sounds', 'music_background.mp3'))
update_musica = pygame.mixer.Sound(os.path.join(os.getcwd() , 'Jogo-da-cobrinha', 'sounds', 'update.wav'))
gameover_musica = pygame.mixer.Sound(os.path.join(os.getcwd() , 'Jogo-da-cobrinha', 'sounds', 'gameover.wav'))

#TOCAR MUSICA DE FUNDO
def tocar_musica_de_fundo(tocar):
    if tocar:  
        pygame.mixer.Channel(0).play(musica_de_fundo, -1)
        pygame.mixer.Channel(0).set_volume(0.2)
    else:
        pygame.mixer.Channel(0).stop()

def sound_efects(efeito):
    efeito_sonoro = pygame.mixer.Sound(efeito)
    efeito_sonoro.play()

y_size = 5 /100 * altura
x_size = y_size
velocidade = x_size

x_controler = 0
y_controler = 0

def aumentar_cobra(corpo_cobra):
    # Apenas desenhar a cobra se tiver mais segmentos que o permitido por max_len_cobra
    if len(corpo_cobra) > max_len_cobra:
        del corpo_cobra[0]
    
    for XeY in corpo_cobra:
        # Desenhar a borda preta
        pygame.draw.rect(tela, (0, 0, 0), (XeY[0], XeY[1], x_size, y_size))
        # Desenhar o preenchimento verde da cobra, um pouco menor para caber dentro da borda
        pygame.draw.rect(tela, color_snake, (XeY[0] + 1, XeY[1] + 1, x_size - 2, y_size - 2))


snake_x = 40
snake_y = 40
color_snake = (0, 255, 0)

maca_x = largura/2 - x_size
maca_y = altura/2 - y_size
color_maca = (255, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake Game")

relogio = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 20, True, True)

def reiniciar_jogo():
    global score, corpo_cobra, snake_x, snake_y, maca_x, maca_y, max_len_cobra, morreu, cabeca_cobra, x_controler, y_controler
    tocar_musica_de_fundo(True)
    score = 0
    snake_x = largura / 2
    snake_y = altura / 2
    corpo_cobra = []
    maca_x = random.randint(1, 19) * y_size
    maca_y = random.randint(1, 19) * y_size
    max_len_cobra = 0
    x_controler = 0
    y_controler = 0
    morreu = False

tocar_musica_de_fundo(True)

while True:

    message = font.render(f"Score: {score}", True, (0, 0, 0))
    relogio.tick(10)
    tela.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and x_controler != velocidade:
                y_controler = 0
                x_controler = -velocidade
                break
            if event.key == pygame.K_d and x_controler != -velocidade:
                y_controler = 0
                x_controler = velocidade
                break
            if event.key == pygame.K_w and y_controler != velocidade:
                x_controler = 0
                y_controler = -velocidade
                break
            if event.key == pygame.K_s and y_controler != -velocidade:
                x_controler = 0
                y_controler = velocidade
                break

    snake = pygame.draw.rect(tela, (0, 0, 0), (snake_x, snake_y, x_size, y_size))

    pygame.draw.rect(tela, color_snake, (snake_x + 1, snake_y + 1, x_size - 2, y_size - 2))

    maca = pygame.draw.rect(tela, (0, 0, 0), (maca_x, maca_y, x_size, y_size))
    pygame.draw.rect(tela, (color_maca), (maca_x + 2, maca_y + 2, x_size - 4, y_size - 4))

    if snake.colliderect(maca):
        maca_x = random.randint(1, 19) * y_size
        maca_y = random.randint(1, 19) * y_size
        max_len_cobra += 2
        score = max_len_cobra // 2
        sound_efects(update_musica)

    snake_x += x_controler
    snake_y += y_controler

    if snake_x + x_size > largura:
        snake_x = 0
    if snake_x < 0:
        snake_x = largura - x_size
    if snake_y + y_size > altura:
        snake_y = 0
    if snake_y < 0:
        snake_y = altura - y_size

    cabeca_cobra = []
    cabeca_cobra.append(snake_x)
    cabeca_cobra.append(snake_y)
    corpo_cobra.append(cabeca_cobra)

    aumentar_cobra(corpo_cobra)

    tela.blit(message, (x_size, x_size))

    if corpo_cobra.count(cabeca_cobra) > 1:
        morreu = True
        tocar_musica_de_fundo(False)
        sound_efects(gameover_musica)

        font2 = pygame.font.SysFont('Arial', 40, True, True)
        message_font2 = "Aperte a tecla R para reiniciar o jogo"
        text2_formatado = font2.render(message_font2, True, (0, 0, 0))
        ret_tex2 = text2_formatado.get_rect()

        while morreu:
            tela.fill('White')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        reiniciar_jogo()

            ret_tex2.center = (largura // 2, altura // 2)

            tela.blit(text2_formatado, ret_tex2)

            pygame.display.update()

    pygame.display.update()
