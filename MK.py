import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

red = (212, 44, 25)
yellow = (216, 235, 52)
green = (52, 235, 52)
blue = (52, 235, 226)

red_pressed = (158, 87, 79)
yellow_pressed = (148, 156, 104)
green_pressed = (109, 156, 104)
blue_pressed = (104, 156, 153)

pygame.mixer.music.load('resource/main-menu-1.mp3')
pygame.mixer.music.play()

sound1 = pygame.mixer.Sound('resource/poluchenie-bonusa.mp3')
sound2 = pygame.mixer.Sound('resource/promah-pri-boe-na-mechah.mp3')
sound3 = pygame.mixer.Sound('resource/ryik-lva-korotkiy-zvuk-30857.mp3')
sound4 = pygame.mixer.Sound('resource/ryik-pri-napadenii-dikoy-koshki.mp3')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        pygame.draw.rect(win, red_pressed, (0, 0, 250, 250))
        sound1.play()
    elif keys[pygame.K_w]:
        pygame.draw.rect(win, yellow_pressed, (250, 0, 250, 250))
        sound2.play()
    elif keys[pygame.K_a]:
        pygame.draw.rect(win, green_pressed, (0, 250, 250, 250))
        sound3.play()
    elif keys[pygame.K_s]:
        pygame.draw.rect(win, blue_pressed, (250, 250, 250, 250))
        sound4.play()
    else:
        pygame.draw.rect(win, red, (0, 0, 250, 250))
        pygame.draw.rect(win, yellow, (250, 0, 250, 250))
        pygame.draw.rect(win, green, (0, 250, 250, 250))
        pygame.draw.rect(win, blue, (250, 250, 250, 250))
        sound1.stop()
        sound2.stop()
        sound3.stop()
        sound4.stop()

    pygame.display.update()