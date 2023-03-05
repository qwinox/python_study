a = input()

list = a.split()

sum = 0

for i in list:
    sum = sum + int(i)

print(sum/len(list))