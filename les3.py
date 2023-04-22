name = input("Как тебя зовут?")
age = int(input("Сколько тебе лет?"))
print("Привет,", name, end='')

if age > 18:
    print("ты уже взрослый!")
else:
    print("ты ещё ребёнок")