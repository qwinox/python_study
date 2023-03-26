import pygame

BLACK = (0, ) * 3
GRAY = (100, ) * 3
WHITE = (255, ) * 3
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LIGHTGREEN = (0, 200, 200)

CROSS = '#046582'
CIRCLE = '#e4bad4'
W = 500
H = 500


class Board:
    def __init__(self, W, H, size):
        self.W, self.H = W, H
        self.size = size
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        self.move = 1


    def click(self, mouse_pos):
        x = mouse_pos[0] // self.size
        y = mouse_pos[1] // self.size
        self.board[y][x] = self.move
        self.move = -self.move


    def render(self, screen):
        pass


board = Board(W, H, 200)
screen = pygame.display.set_mode((W, H))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.click(event.pos)

    screen.fill(WHITE)
    board.render(screen)
    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        pygame.quit()
        exit()



