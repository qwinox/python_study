import pygame

a = int(input("Введите 1 число:"))
b = int(input("Введите 2 число:"))

pygame.init()
win = pygame.display.set_mode((a, a))

win.fill((255, 255, 255))
for i in range(b):
    for j in range(b):
        if i % 2 == 0:
            if j % 2 == 0:
                pygame.draw.rect(win, (0, 0, 0), (i * (a // b), j * (a // b), a // b, a // b ))
        if i % 2 == 1:
            if j % 2 == 1:
                pygame.draw.rect(win, (0, 255, 0), (i * (a // b), j * (a // b), a // b, a // b))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
