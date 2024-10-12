import pygame
import sys
import random

largura = 1280
altura = 800

corpo_cobra = []
max_len_cobra = 0

score = 0

pygame.init()


y_size = 5/100 * altura
x_size = y_size
velocidade = x_size

x_controler = 0
y_controler = 0

def aumentar_cobra(corpo_cobra):
    for XeY in corpo_cobra:
        snake = pygame.draw.rect(tela, color_snake, (XeY[0], XeY[1], x_size, y_size))
    if len(corpo_cobra) > max_len_cobra:
        del corpo_cobra[0]

snake_x = 0
snake_y = 0
color_snake = (0, 255, 0)

maca_x = maca_x = random.randint(1, 19) * x_size
maca_y = maca_x = random.randint(1, 19) * x_size
color_maca = (255, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake Game")

relogio = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 20, True, True)


while True:
    message = font.render(f"Score:{score}", True, (0, 0, 0))
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

    snake = pygame.draw.rect(tela, color_snake, (snake_x, snake_y, x_size, y_size))
    maca = pygame.draw.rect(tela, color_maca, (maca_x, maca_y, x_size, y_size))

    if snake.colliderect(maca):
        maca_x = random.randint(1, 19) * y_size
        maca_y = random.randint(1, 19) * y_size
        max_len_cobra += 2
        score = max_len_cobra / 2

    snake_x += x_controler
    snake_y += y_controler

    if snake_x - x_size > largura:
        snake_x = 0
    if snake_x < 0:
        snake_x = largura - x_size
    if snake_y - y_size > altura:
        snake_y = 0
    if snake_y < 0:
        snake_y = altura - y_size

    cabeca_cobra = []
    cabeca_cobra.append(snake_x)
    cabeca_cobra.append(snake_y)
    corpo_cobra.append(cabeca_cobra)
    aumentar_cobra(corpo_cobra)
    

    tela.blit(message, (x_size, x_size))

    pygame.display.update()