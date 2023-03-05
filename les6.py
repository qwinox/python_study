c = (input('Введите пароль:'))
flag = True

while flag:
    if len(c)<8:
        print('короткий')
        c = (input('Введите пароль:'))
    elif "123" in c:
        print('простой')
        c = (input('Введите пароль:'))
    else:
        print('правильно')
        flag = False