# Зробіть словник де буде табличка множення додавання ділення і віднімання чисел від 2 до 9(включно).
# (так як робили на уроці). Ці значення запишіть в словник з відповідними ключами "+", "-", "/", "*"
# Коли ви підготуєте це, запитайте в користувача яку табличку він хоче побачити (додавання, віднімання, множення, ділення)
# і виведіть йому цю табличку.
operation = input("Which table (+, -, /, *) do you want to see? ")
while operation != '*' and operation != '/' and operation != '+' and operation != '-':
    operation = input("Wrong operation. Please, select: +, -, /, * ")
if operation == '*' or operation == '/' or operation == '+' or operation == '-':
    for i in range(2, 10):
        for j in range(2, 10):
            dict_multiplication = {i: j, '=': i * j}
            dict_division = {i * j: i, '=': j}
            dict_addition = {i: j, '=': i + j}
            dict_subtraction = {i + j: i, '=': j}
            if operation == '*':
                print(dict_multiplication)
            elif operation == '/':
                print(dict_division)
            elif operation == '+':
                print(dict_addition)
            else:
                print(dict_subtraction)
