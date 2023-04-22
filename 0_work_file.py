import pygame

size = input("Введит 2 числа через пробел:")
size = size.split()
n, a = int(size[0]), int(size[1])
rect = n // a

pygame.init()
win = pygame.display.set_mode((n, n))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    color = (255, 255, 255)
    win.fill(color)
    pygame.display.set_caption("шахматы")

    for i in range(a):
        for j in range(a):
            if (i + j) % 2 == 0:
                pygame.draw.rect(win, (0, 0, 0), (j * rect, i * rect, (i+1) * rect, (j+1) * rect))

    pygame.display.update()




