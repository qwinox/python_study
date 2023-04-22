import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

x_c = 260
y_c = 0
dir_c = -1

x_r = 0
y_r = 200
dir_r = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if dir_c == -1:
        y_c += 1
    else:
        y_c -= 1

    if y_c > 500:
        dir_c = 1
    if y_c < 0:
        dir_c = -1

    if dir_r == 1:
        x_r += 1
    else:
        x_r -= 1

    if x_r > 500:
        dir_r = -1
    if x_r < 0:
        dir_r = 1

    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 255, 0), (x_r, y_r, 100, 150))
    pygame.draw.circle(win, (255, 0, 0), (x_c, y_c), 50)
    pygame.draw.circle(win, (255, 0, 255), (x_r, y_c), 50)
    pygame.draw.circle(win, (0, 0, 255), (500 - x_r, 500 - y_c), 50)
    pygame.display.update()

    pygame.time.delay(10)