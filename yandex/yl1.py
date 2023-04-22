string = len(input())
count = 0

n = int(input())
for i in range(n):
    temp = int(input())
    if temp % string == 0:
        count += 1

m = int(input())
for i in range(m):
    temp = int(input())
    if temp % string == 0:
        count -= 1

if count == 0:
    print("Нет предпочтений")
elif count > 0:
    print("Классика больше на", count)
else:
    print("Модерн больше на", abs(count))