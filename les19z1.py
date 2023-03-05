import pygame


class Circle():
    def __init__(self, win, color, x, y, rad):
        self.win = win
        self.color = color
        self.x = x
        self.y = y
        self.rad = rad
        self.vel = 1

    def draw(self):
        pygame.draw.circle(self.win, self.color, (self.x, self.y), self.rad)

    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] == 1:
            self.y -= self.vel
        elif keys[pygame.K_DOWN] == 1:
            self.y += self.vel
        elif keys[pygame.K_LEFT] == 1:
            self.x -= self.vel
        elif keys[pygame.K_RIGHT] == 1:
            self.x += self.vel


pygame.init()
win = pygame.display.set_mode((500, 500))
new = Circle(win, (255, 255, 0), 250, 250, 30)
temp = Circle(win, (255, 0, 0), 250, 350, 70)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    temp.draw()
    new.draw()
    new.move_by_keys()

    pygame.display.update()
    win.fill((255, 255, 255))