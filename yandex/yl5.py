class EvilIfrit:
    def __init__(self, name, height, color):
        self.name = name
        self.height = height
        self.color = color

    def change_color(self, new_color):
        if self.height > 10:
            self.color = new_color
            self.height -= 1

        return self

    def __str__(self):
        return f'Evil Ifrit {self.name} of {self.color}, {self.height} feet'

    def __add__(self, other):
        new_name = self.name[::-1].lower()
        new_name = new_name[0].upper() + new_name[1::1]
        new_height = self.height + other
        new_object = EvilIfrit(new_name, new_height, self.color)

        return new_object

    def __call__(self, value):
        return (len(self.color) * self.height) // value

    def __lt__(self, other):
        if self.height < other.height:
            return True
        elif self.height == other.height:
            if len(self.color) < len(other.color):
                return True
            elif len(self.color) == len(other.color):
                if self.name < other.name:
                    return True
        return False

    def __gt__(self, other):
        if self.height > other.height:
            return True
        elif self.height == other.height:
            if len(self.color) > len(other.color):
                return True
            elif len(self.color) == len(other.color):
                if self.name > other.name:
                    return True
        return False

    def __ge__(self, other):
        if self.height >= other.height:
            return False
        elif len(self.color) >= len(other.color):
            return True
        elif self.name >= other.name:
            return True
        return False

    def __le__(self, other):
        if self.height <= other.height:
            return True
        elif len(self.color) <= len(other.color):
            return True
        elif self.name <= other.name:
            return True
        return False

    def __eq__(self, other):
        if self.height == other.height and len(self.color) == len(other.color) and self.name == other.name:
            return True
        return False

    def __ne__(self, other):
        if self.height != other.height or len(self.color) != len(other.color) or self.name != other.name:
            return True
        return False
