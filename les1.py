from struct import unpack


def hex_to_rgb(s):
    s = s.lstrip("#")
    return tuple([int(s[i:i + 2], 16) for i in range(0, 5, 2)])


def rgb_to_hex(rgb):
    r, g, b = rgb
    return f"#{hex(r)[2:].rjust(2, '0')}" f"{hex(g)[2:].rjust(2, '0')}" f"{hex(b)[2:].rjust(2, '0')}"


    # with open(filename, 'rb') as f:
    #     data = f.read()
def remove_spell(filename, new_filename, **colors):
    image = open("image/" + filename, "rb")
    data = image.read()

    hex_string = ' '.join(format(x, '02X') for x in data)
    print(hex_string)  # Получили строку 4D 5A ...

    # # Преобразуем байты в список шестнадцатеричных чисел
    # hex_list = [hex(b)[2:] for b in data]
    #
    # # Выведем список на экран
    # print(hex_list)


colors = {
    "#9dd6f3": "#ccf197",
    "#e3bdfa": "#87c6ee",
    "#ec1c24": "#af2cb6",
    "#985a2e": "#0f5682"
}

remove_spell("photo_2023-04-06_15-13-45.jpg", "up_and_down.png", **colors)


def __le__(self, other):
    if self.height <= other.height:
        return True
    elif len(self.color) <= len(other.color):
        return True
    elif self.name <= other.name:
        return True
    return False


def __ge__(self, other):
    if self.height >= other.height:
        return True
    elif len(self.color) >= len(other.color):
        return True
    elif self.name >= other.name:
        return True
    return False