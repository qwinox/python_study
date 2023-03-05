import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
x = 250
y = 250
step = 0.1
color = (255, 0, 255)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= step
    elif keys[pygame.K_RIGHT]:
        x += step
    elif keys[pygame.K_UP]:
        y -= step
    elif keys[pygame.K_DOWN]:
        y += step
    else:
        x = 250
        y = 250
    if x > 400 or x < 100:
        step = 0.05
        color = (255, 0, 0)
    else:
        step = 0.1
        color = (255, 0, 255)
    if y > 400 or y < 100:
        step = 0.05
        color = (255, 0, 0)
    else:
        step = 0.1
        color = (255, 0, 255)

    win.fill((255, 255, 255))
    pygame.draw.circle(win, color, (x, y), 50)
    pygame.display.update()