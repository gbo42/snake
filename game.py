import pygame

HEIGHT = 400
WIDTH = 600
finished = False

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True

    screen.fill((51, 51, 51))
    pygame.display.flip()

pygame.quit()
