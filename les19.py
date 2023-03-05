class Character():
    def __init__(self, character_name, name, surname, age, gender):
        self.character_name = character_name
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def nazovis(self):
        print("Hello,", self.character_name, self.name, self.surname, self.age, self.gender)

    def kick(self, hater):
        print(self.character_name, "ударил", hater)


my_character = Character("Batman", "Bruce", "Wayne", 32, "Male")
my_character.nazovis()
my_character.kick("Joker")