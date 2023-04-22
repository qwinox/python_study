class Button:
    def __init__(self):
        self.click_cout = 0
    def click(self):
        self.click_cout += 1
    def say(self):
        print("Колличество нажатий", self.click_cout)
    def reset(self):
        self.click_cout = 0


my_button = Button()
my_button.say()
for i in range(5):
    my_button.click()
my_button.say()
my_button.reset()
my_button.say()



