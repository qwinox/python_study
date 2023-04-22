def hex_to_rgb(s):
    s = s.lstrip("#")
    return tuple([int(s[i:i + 2], 16) for i in range(0, 5, 2)])


def rgb_to_hex(rgb):
    r, g, b = rgb
    return f"#{hex(r)[2:].rjust(2, '0')}" f"{hex(g)[2:].rjust(2, '0')}" f"{hex(b)[2:].rjust(2, '0')}"


def alien_scientist(filename, new_filename, **colors):
    image = open("image/" + filename, "rb")
    data = image.read()
    #print(data)

    hex_string = ' '.join('{:02x}'.format(x) for x in data)
    print(hex_string)  # Получили строку 4D 5A ...

    # # Преобразуем байты в список шестнадцатеричных чисел
    # hex_list = [hex(b)[2:] for b in data]
    #
    # # Выведем список на экран
    # print(hex_list)


colors = {
    "#bbe05f": (164, 232, 241),
    "#4783a1": (19, 93, 138),
    "#b7cfd6": (235, 216, 247),
    "#b83dba": (0, 100, 247)
}

alien_scientist("philosopher.png", "professor.png", **colors)