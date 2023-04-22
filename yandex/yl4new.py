from PIL import Image


def alien_scientist(filename, new_filename, **colors):
    temp = Image.open(filename)
    temp = temp.rotate(180)
    temp.save(new_filename, quality=95)


