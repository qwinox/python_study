print("Суммируем 10 чисел")

sum = 0

for i in range(0, 10, 1):
    a = int(input("Введите число номер " + str(i + 1) + ":"))
    sum += a

print('Сумма равна', sum)