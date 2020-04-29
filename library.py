config = open("/Users/kolesnikovtimofej/Downloads/conf.txt", 'r')
dictionary = {}

for line in config:
    if line[0] == '#' or line[0] == ';' or line[0] == '\n':
        continue
    key = line.split()[0]
    val = ""
    try:
        val = line.split()[1]
    except IndexError:
        val = "параметр {" + key + "} не имеет значения"
    dictionary.update({key: val})

flag = True
while flag:
    command = input()
    try:
        if command.split()[0] == "get" and command.split()[1] == "param" :
            try:
                print(command.split()[2] + " : " + dictionary[command.split()[2]])
            except KeyError:
                print("параметр {" + command.split()[2] + "} не найден")
    except IndexError:
        print("команда {" + command + "} не может быть выполнена")
    flag_internal = True
    s = ''
    while flag_internal:
        s = input("хотите продолжить? (y/n)")
        if not (s == 'n' or s == 'y'):
            continue
        else:
            break
    if s == 'n':
        break
    if s == 'y':
        continue

