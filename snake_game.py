import pygame 
from pygame.locals import *
import random

def on_grid_random():  #função para alinhas as frutas com a cobra
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x // 10 * 10 , y // 10 * 10)

def collision(c1,c2): # colisão entre duas celulas (cobra , fruta)
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


# definição de macro para movimentação
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Tela
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('snake')

snake = [(200,200),(210,200),(220,200)] # a cobra é representada por uma lista com segmentos representados por tuplas com valores de x, y
snake_skin = pygame.Surface((10,10)) # pixel da cobra em formato de quadrado
snake_skin.fill((0,255,0)) # cor da cobra em lime green em rgb

fruit_pos = on_grid_random()
fruit = pygame.Surface((10,10)) # fruta
fruit.fill((255,0,0))

snake_direction =  LEFT # direção que a cobra começa movimentando
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0


game_over = False

while not game_over:

    clock.tick(30)  # limitar os fps

    for event in pygame.event.get():
        if event.type == QUIT: # fechar o jogo
            pygame.quit()
            exit()

         # configurando as teclas
        if event.type == KEYDOWN:

            if event.key == K_UP:
                snake_direction = UP

            if event.key == K_DOWN:
                snake_direction = DOWN

            if event.key == K_RIGHT:
                snake_direction = RIGHT

            if event.key == K_LEFT:
                snake_direction = LEFT

    if collision(snake[0],fruit_pos): # testar colisão
        fruit_pos = on_grid_random()
        snake.append((0,0))
        score += 1
    
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0: # Verifique se a cobra colidiu com os limites
        game_over = True
        break
    
    
    for i in range(1, len(snake) - 1):  # Verifique se a cobra atingiu a si mesma
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[1 - 1][1])

    if game_over:
        break

     # movimentação
    if snake_direction == UP:
        snake[0] = (snake[0][0],snake[0][1] - 10)  # (x , y )

    if snake_direction == DOWN:
        snake[0] = (snake[0][0],snake[0][1] + 10)
    
    if snake_direction == RIGHT:
        snake[0] = (snake[0][0] + 10,snake[0][1])

    if snake_direction == LEFT:
        snake[0] = (snake[0][0] - 10,snake[0][1])
     
    
    screen.fill((0,0,0)) # limpar tela

    screen.blit(fruit,fruit_pos) # plotar a fruta

    for x in range(0, 600, 10): # Desenhar linhas verticais
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10): # Desenhar linhas verticais
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))
    
    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)



    for pos in snake: # irá poltar a cobra na tela para cada posição
        screen.blit(snake_skin,pos) 

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()