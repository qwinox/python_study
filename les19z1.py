import random
import pygame

FPS = 30
clock = pygame.time.Clock()

class Circle():
    def __init__(self, win, color, x, y, rad):
        self.win = win
        self.color = color
        self.x = x
        self.y = y
        self.rad = rad
        self.vel = 5
        self.dir = 'right'

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

    def horizontal_movement(self):
        if self.dir == 'right':
            self.x += 50
            if self.x > 500:
                self.dir = 'left'
        else:
            self.x -= 50
            if self.x < 0:
                self.dir = 'right'


pygame.init()
win = pygame.display.set_mode((500, 500))

list_circles = []
for i in range(100):
    color = random.choices(range(256), k=3)
    list_circles.append(Circle(win, color, i * 10, i*5, 30))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS)

    for i in list_circles:
        i.draw()
        i.horizontal_movement()

    pygame.display.update()
    win.fill((255, 255, 255))