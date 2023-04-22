import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

x = 200
y = 200
v = 5
color = (0, 255, 0)
rad = 60

main_character = pygame.image.load("image/enemy.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= v
    elif keys[pygame.K_RIGHT]:
        x += v
    elif keys[pygame.K_UP]:
        y -= v
    elif keys[pygame.K_DOWN]:
        y += v
    else:
        if x > 200:
            x -= v
        elif x < 200:
            x += v
        if y > 200:
            y -= v
        elif y < 200:
            y += v

    if y < 100 or y > 400 or x < 100 or x > 400:
        color = (255, 0, 0)
        v = 1
        rad = 40
    else:
        color = (0, 255, 0)
        v = 5
        rad = 60



    win.fill((255, 255, 255))

    pygame.draw.circle(win, color, (x + 50, y + 50), rad)
    win.blit(main_character, (x, y))

    pygame.display.update()
    pygame.time.delay(10)
