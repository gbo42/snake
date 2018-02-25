import pygame
import random
from core import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

grid = makeGrid(WIDTH//Wpadded, HEIGHT//Wpadded)
snake = Snake(10, 10)
direct = (0, 0)

clock = pygame.time.Clock()

food = Block(random.randint(0, hor-1), random.randint(0, ver-1), RED)

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True
            if event.key == pygame.K_RIGHT:
                direct = (1, 0)
            if event.key == pygame.K_LEFT:
                direct = (-1, 0)
            if event.key == pygame.K_UP:
                direct = (0, -1)
            if event.key == pygame.K_DOWN:
                direct = (0, 1)

    if not (snake.dir[0] + direct[0] == 0 and snake.dir[1] + direct[1] == 0):
        snake.dir = direct

    if snake.head.x == food.x and snake.head.y == food.y:
        snake.tail.append(Block(food.x, food.y, GREEN))
        clear = False
        while not clear:
            clear = True
            x = random.randint(0, hor-1)
            y = random.randint(0, ver-1)
            if(snake.head.actx == x and snake.head.acty == y):
                clear = False
            for part in snake.tail:
                if (part.actx == x and part.acty == y):
                    clear = False
        food.updateXY(x, y)

    if snake.checkHit():
        snake.tail = []
        direct = (0, 0)
        snake.dir = direct

    screen.fill(GRAY)
    snake.move()
    snake.draw(screen)
    food.draw(screen)
    pygame.display.flip()
    clock.tick_busy_loop(10)

pygame.quit()
