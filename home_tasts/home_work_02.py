# Задача 1:
# Напишіть программу "Касир в кінотеватрі", яка попросить користувача ввести свій вік (можна використати константу або
# функцію input(), на екран має бути виведено лише одне повідомлення).
# - якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
# - якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
# - якщо від 16 до 65 то зробіть якесь вітальне повідомлення, на ваш розсуд.
# - якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"
# user_age = 100
# if user_age < 16:
#     print("This film is for adults!")
#     if user_age <= 7:
#         print("Where is your parents?")
# elif user_age >= 16 and  user_age <65:
#     print("Here are your ticket! Enjoy your time!")
# else:
#     print("Please, show your document!")
#
# Задача 2
# Текстова в чому різниця між is та ==?
# == це оператор присвоєння, який перевіряє чи мають змінні однакові значення
# is це оператор, який перевряє рівність ID у змінних (чи посилаються змінні на однакову комірку пам'яті)

# Задача 3
# Напишіть програму яка в користувача запитує два числа(можуть бути числа типу інт, а можуть бути в стр).
# Потім запитує це стр чи інт і в залежності від відповіді конкатенує їх або додає і повертає результат перемножений на три.
# якщо після конкатенації отримали 10 то перемноживши на 3 отримаємо 30.
# print("Enter integer or text")
# first_data = input()
# print("Enter integer or text again")
# second_data = input()
# print("Choose input type: 'str' or 'int' ")
# number_type = input()
# if number_type.lower() == "str":
#     print ("String concatenation -> ", first_data + second_data)
# elif number_type.lower() == "int":
#     first_data = int(first_data)
#     second_data = int(second_data)
#     print ("Arithmetic operation -> ", (first_data+second_data)*3)
# else:
#     print("Wrong input type. Please, select 'str' or 'int'")

# Задача 4
# Напишіть програму яка буде приймати квадратне рівняння і розвязувати його. Памятайте що там є декілька випадків по іксам.
# Завдання не складне але обьємне. Подумайте як прийняти дані від користувача, ну і над рештою).
# a = input("Enter a = ")
# a = float(a)
# b = input("Enter b = ")
# b = float(b)
# c = input("Enter c = ")
# c = float(c)
# d = b**2 - 4 * a * c
# if d >= 0:
#     x_1 = (-b - d**0.5) / (2 * a)
#     x_2 = (-b + d**0.5) / (2 * a)
#     print("x1= ", x_1, ",", "x2= ", x_2)
# else:
#     print("D<0. The equation has no solution")
