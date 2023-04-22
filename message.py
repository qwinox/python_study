from PIL import Image
import random
import time


def image_filter(pixels, i, j):
    '''Эта функция - фильтр увеличения яркости'''

    for r in range(-5, 5, 1):
        print(pixels[i + r, j])

    if i + j > 300 and i + j < 1000:
        noise = -random.randint(20, 50)
    else:
        noise = random.randint(20, 50)

    r = pixels[i, j][0] * 2 + noise
    g = pixels[i, j][1] * 2 + noise
    b = pixels[i, j][2] * 2 + noise

    #print(pixels[i, j][0], pixels[i, j][1], pixels[i, j][2])

    return r, g, b


if __name__ == '__main__':
    start = time.time()
    im = Image.open('owl.jpeg')
    x, y = im.size
    pixels = im.load()

    for i in range(x):
        for k in range(y):
            pixels[i, k] = image_filter(pixels, i, k)

    end = time.time() - start ## собственно время работы программы
    print(end)

    im.save('res1.jpg')
