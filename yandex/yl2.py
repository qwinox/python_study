array_of_phenomenons = []

parameters = input()
parameters = parameters.split(": ")

n = int(input())

for i in range(n):
    result_of_check = 0
    information = input()
    information = information.split(" -> ")
    name = information[0]
    phenomenon = information[1].split("#")
    for j in range(len(parameters)):
        if abs(float(parameters[j]) - float(phenomenon[j])) > 3:
            result_of_check += 1

    if result_of_check < len(parameters) / 2:
        array_of_phenomenons.append(name)

unique = list(set(array_of_phenomenons))

for i in unique:
    print(i)
