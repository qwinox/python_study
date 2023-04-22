magic_dictionary = {}

while True:
    try:
        string = input()
        information = string.split(' - ')
        name = information[0]
        what_can_do = information[1]
        magic_dictionary[name] = what_can_do
    except EOFError:
        break

print(magic_dictionary)