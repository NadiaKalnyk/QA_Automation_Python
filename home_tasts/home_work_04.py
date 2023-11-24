# Задача 1
#
# Напишіть програму яка запитує в користувача вартість покупок, він їх вводе через пробіл, точна кількість не вказана.
# Вам потрібно до вартості покупок додати 6,5 відсотки податків.
#
# Потім питаєте чи є в користувача купон на знижку якщо є то питаєте це на суму чи на відсоток і потім віднімаєте суму
# або відсоток відповідно від ціни яку отримали раніше і пишете користувачу кінцеву суму.
#
# * завдання з зірочкою не впливає на бал. Округліть суму якщо копійок більше ніж 44 то це буде + 1 гривня, якщо менше.
# то тоді просто відкидаємо копійки від ціни.
# print("Write price for each product")
# price_list = input().split()
# s = 0
# tax = 0.065
# for i in price_list:
#     i = float(i)
#     s = s + i
# sum_plus_tax = round(s + s * tax, 2)
# have_discount = input(f"You need to pay {sum_plus_tax} including 6.5% tax. Do you have discount? yes/no ")
# while have_discount.lower() != 'yes' and have_discount.lower() != 'no':
#     have_discount = input("Sorry, I didn't understand. Do you have discount? yes/no ")
# if have_discount.lower() == 'yes':
#     my_discount = input("Is your discount amount or percentage? amount/per ")
#     while my_discount.lower() != 'amount' and my_discount.lower() != 'per':
#         my_discount = input("Sorry, I didn't understand. Is your discount amount or percentage? amount/per ")
#     if my_discount.lower() == 'amount':
#         amount = int(input("Enter your discount amount "))
#         result = sum_plus_tax - amount
#         if result >= 0:
#             print(f"Your pay including {amount} discount is {result} UAH")
#         else:
#             print(f"Your pay including discount is 0 UAH. Balance on the discount is {result*(-1)} UAH")
#     else:
#         percentage = int(input("Enter your discount percentage "))
#         per = round(sum_plus_tax * percentage/100, 2)
#         print(f"Your pay including {percentage}% discount is {sum_plus_tax - per} UAH")
# else:
#     print(f"{sum_plus_tax} UAH please")

# Задача 2
# Переробіть задачу з попереднього уроку враховуючи ваші знання з цього уроку, використайте цикл for in або while.
# кроки:
# Спочатку пропонуємо користувачу ввести продукти.
# Робимо 5 запитів на видалення
# Перевіряємо корзину
# Пропонуємо додати продукти
# Виводмо список і прощаємось
# print("Which products do you want to buy?")
# product_list = input().split()
# print(f"You have entered products for your purchase: {product_list}")
# basket = []
# deletion_request = 5
# i = 0
# while i<= deletion_request:
#     i = i + 1
#     del_element = int(input(
#         "Which product have you already purchased? "))
#     if del_element >= 1 and del_element <= len(product_list):
#         product_1 = product_list.pop(del_element - 1)
#         basket.append(product_1)
#         print(product_list)
#     else:
#         print(f"Wrong number. There is no product with {del_element} in the list {product_list}")
# print(f"You have already bought {basket}. There are {len(basket)} products in the basket")
# import copy
# product_list_2 = copy.deepcopy(product_list)
# add_product = input("Which product do you want to add to your purchase? ")
# product_list_2.append(add_product)
# print(f"Your purchase was updated: {product_list_2}")

# Задача 3
# Напишіть програму Банкомат. Втсановіть пін код для користувача(зробимо це константою).
# Запитайте в користувача Пін якщо він введе три рази не вірно то напишіть що карта заблокована.
# Використовуйте цикл while.
# real_pin = 1111
# i = 0
# pin = int(input("Enter your PIN: "))
# while pin != real_pin:
#     i += 1
#     if pin != real_pin:
#         if i != 3:
#             pin = int(input(f"Invalid PIN. You have {3 - i} attempts left. Enter your PIN: "))
#         else:
#             print("You have been blocked!")
#             break
# else:
#     print("Success! You are logged in")

# Задача 4
# Напишіть за допомогою f-string та format. Дві стрічки де буде підставлятись імя та вік з зміних
# name = "оLеnА"
# age = 21
# f_string = тут ваш код формата ф-стрінг. | повино вийти -> Я Олена, мені 21 рік
# format_string = тут ваш код формата формат стрінг | повино вийти -> Я Олена, мені 21 рік
# print(f_string)
# print(format_string)
# name = "оЛенА"
# age = 21
# print(f"I'm {name.capitalize()}, I'm {age} years old")
# format_string= """I'm {0}, I'm {1} years old""".format(name.capitalize(), age)
# print(format_string)

