import pygame
import random

FPS = 60
W, H = 500, 500

clock = pygame.time.Clock()
pygame.init()
win = pygame.display.set_mode((W, H))
win.fill((255, 255, 255))
size = 200
flag = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    clock.tick(FPS)

    pos = pygame.mouse.get_pos()
    pygame.draw.circle(win, (random.choices(range(256), k=3)), pos, size)
    size += flag
    if size > 200:
        flag = flag * (-1)
    if size < 50:
        flag = flag * (-1)

    pygame.display.update()