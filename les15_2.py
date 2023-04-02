import pygame
pygame.init()

a = input("Введите 2 числа, разделённые пробелом:")
a = a.split()
num1 = int(a[0])
num2 = int(a[1])

a = num1 // num2

win = pygame.display.set_mode((num1, num1))
print(num1, num2)
print()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    color = (255, 255, 255)
    win.fill(color)
    for i in range(a):
        for j in range(a):
            if (i+j) % 2 == 0:
                pygame.draw.rect(win, (0, 0, 0), (i, j, num1/num2, num1/num2))
                print(i, j, num1, num2)
    pygame.display.update()
