def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


flag = True
while flag:
    flag_internal = True
    while flag_internal:
        num1 = input("Введите первое число: ")
        if is_digit(num1) == False:
            print("Некорректное значение")
            continue
        break

    while flag_internal:
        num2 = input("Введите второе число: ")
        if is_digit(num2) == False:
            print("Некорректное выражение")
            continue
        break

    while flag_internal:
        op = input("Введите операцию: ")
        if not (op == '+' or op == '-' or op == '*' or op == '/'):
            print("Некорректное значение")
            continue
        break

    if op == '+':
        print("Ответ: ", float(num1) + float(num2))

    if op == '-':
        print("Ответ: ", float(num1) - float(num2))

    if op == '*':
        print("Ответ: ", float(num1) * float(num2))

    if op == '/':
        print("Ответ: ", float(num1) / float(num2))

    input_errors = 0
    res = ''
    while flag_internal:
        res = input("Хотите начать сначала? (да/нет)")
        if res.lower() == 'да':
            break
        if input_errors >=2:
            res = 'нет'
            break
        if not (res.lower() == 'да' or res.lower() == 'нет'):
            input_errors += 1
            print("Incorrect input")
            continue
        break

    if res.lower() == 'да':
        continue
    if res.lower() == 'нет':
        break