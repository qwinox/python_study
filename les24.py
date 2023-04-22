import pygame


def load_img(name):
    img = pygame.image.load(name)
    img = img.convert()
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey)
    return img

FPS = 30
clock = pygame.time.Clock()

win = pygame.display.set_mode((500, 500))

main_character = pygame.image.load("image/enemy.png")
main_character = main_character.convert()
colorkey = main_character.get_at((0, 0))
main_character.set_colorkey(colorkey)

img = load_img("image/gg.png")
img1 = pygame.transform.scale(img, (50, 50))
img2 = pygame.transform.scale(img, (700, 700))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    clock.tick(FPS)
    win.blit(main_character, (0, 0))

    win.blit(img1, (0, 0))
    win.blit(img2, (100, 100))

    pygame.display.update()