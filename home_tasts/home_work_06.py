# Візьміть дві задачі з попередніх уроків, перша легка по вирішенню(декілька стрічок), друга більш складна і перепишіть
# їх на функції. Памятайте про Атамарність та god object. Там де написано що користувач має щось ввести то перероблюємо
# на функція приймає. Подивіться може можна за допомогою функції спростити код. В домашку вставте будь ласка опис задачі

# Задача 1
# Напишіть за допомогою f-string та format. Дві стрічки де буде підставлятись імя та вік з зміних
# name = "оLеnА"
# age = 21
# f_string = тут ваш код формата ф-стрінг. | повино вийти -> Я Олена, мені 21 рік
# format_string = тут ваш код формата формат стрінг | повино вийти -> Я Олена, мені 21 рік
#
# def format_string(name="оLеnА", age=21): -> None
#     print("""I'm {0}, I'm {1} years old""".format(name.capitalize(), age))
#
#
# format_string()
#
#
# def f_string(name : str, age : int):
#     new_string = f"I'm {name.capitalize()}, I'm {age} years old"
#     return new_string
#
#
# print(f_string(name="оLеnА", age=21))

# Задача 3
# Напишіть програму Банкомат. Втсановіть пін код для користувача(зробимо це константою).
# Запитайте в користувача Пін якщо він введе три рази не вірно то напишіть що карта заблокована.
# Використовуйте цикл while.

# REAL_PIN = 1111
# my_pin_code = 1113
# failed_attempts_number = 2
# def comparing_pin_cods(result : bool):
#     result = my_pin_code != REAL_PIN
#     if result == False:
#         return False
#     else:
#         return True
#
# def bankomat(message : str):
#     if comparing_pin_cods(result=False):
#         if failed_attempts_number != 3 and 3 - failed_attempts_number > 0:
#             message = f"Invalid PIN. You have {3 - failed_attempts_number}  attempts left."
#         else:
#             message = "You have been blocked!"
#     else:
#         message = "Success! You are logged in"
#     return message
# message_result = bankomat(comparing_pin_cods(False))
# message_result = bankomat(comparing_pin_cods(True))
# print(message_result)


# Задача 3 (2)
# Напишіть програму яка в користувача запитує два числа(можуть бути числа типу інт, а можуть бути в стр).
# Потім запитує це стр чи інт і в залежності від відповіді конкатенує їх або додає і повертає результат перемножений
# на три. Якщо після конкатенації отримали 10 то перемноживши на 3 отримаємо 30.

# first_number = 2
# second_number = 3
# number_type = 'STR'
#
# def select_operation(message : str):
#     if message == True:
#         if number_type.lower() == "str":
#             message = f"String concatenation ->  {first_number+second_number}"
#         elif number_type.lower() == "int":
#             message = f"Arithmetic operation ->  {(first_number+second_number)*3}"
#         else:
#             message = f"Wrong input type. Please, select 'str' or 'int'"
#     return message
# result = select_operation(True)
# print(result)

# інший варіант розв'язання Задачі 3 (2)
def select_operation(first_number: str|int, second_number: str|int) -> str:
    if isinstance(first_number, str) and (second_number, str):
        message = f"String concatenation ->  {first_number+second_number}"
    elif isinstance(first_number, int) and (second_number, int):
        message = f"Arithmetic operation ->  {(first_number+second_number)*3}"
    else:
        message = f"Wrong input type. Please, select 'str' or 'int'"
    return message

result = select_operation(2, 3)
result2 = select_operation("2", "3")
print(result)
print(result2)