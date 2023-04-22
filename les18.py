class Character:
    def __init__(self, name, super_hero_name, age, height, ):
        self.name = name
        self.super_hero_name = super_hero_name
        self.age = age
        self.height = height
        print("Я был рождён и геройское имя моё", super_hero_name)

    def hit(self, enemy_name):
        print(self.super_hero_name, "ударил кулаком персонажа", enemy_name)


my_hero = Character("Брюс", "Бэтмен", 32, 188)
enemy = Character("Неизвестно", "Джокер", 36, 176)

my_hero.hit(enemy.super_hero_name)
enemy.hit(my_hero.super_hero_name)




