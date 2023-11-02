# 1 Арифметичні операції:
# Написати програму, яка зчитує два числа та виводить їхню суму, різницю, добуток та частку.
# first_number = 2
# second_number = 4
# sum = int (first_number+second_number)
# print ("sum of two numbers is ", sum)

# 2 Залишок від ділення:
# Користувач вводить два числа. Вивести залишок від ділення першого числа на друге.
# print("Enter first number")
# first_number = float(input())
# print("Enter second number")
# second_number = float(input())
# remainder_from_division = first_number % second_number
# print("remainder from division is ", remainder_from_division)

# 3 Цілочисельне ділення:
# Користувач вводить два числа. Вивести, скільки разів перше число ділиться на друге без залишку.
# print("Enter first number")
# first_number = float(input())
# print("Enter second number")
# second_number = float(input())
# int_part_from_division = first_number // second_number
# print("Integer part from division ", int_part_from_division)

# 4 Перетворення стрічки у число:
# Користувач вводить рядок, який складається з цифр. Програма повинна перетворити його на число та вивести.
# print("Enter a string consisting of numbers")
# string = input()
# print ("Your string has  ", type(string), " type")
# string = int(string)
# print ("Type of string has changed. Now sring has", type(string), " type")

# 5 Стрічкова конкатенація + математика:
# Користувач вводить два числа. Програма повинна вивести два прінти: перший — їхню суму,
# другий об'єднати їх. Якщо в нас числа 5 та 4, то результат повинен бути 9 та 54.
# print("Enter the first integer")
# first_number = input()
# print ("Enter the second integer")
# second_number = input()
# first_number = int(first_number)
# second_number = int(second_number)
# sum = first_number + second_number
# first_number = str(first_number)
# second_number = str(second_number)
# concatenation = first_number+second_number
# print("Sum of numbers = ", sum, ", string concatenation - ", concatenation)

# 6 Вік користувача:
# Запитати у користувача його рік народження, ім'я та який зараз рік (три змінні)
# та вивести на екран два прінти: ім'я та скільки років користувачу.
# print("What year were you born? What is your name? What year is it? ")
# birth_year = input()
# name = input()
# current_year = input()
# birth_year = int(birth_year)
# current_year = int(current_year)
# your_year = current_year - birth_year
# print("Result: Your name is", name, ", you are ", your_year, "years old.")

# 7 Перевод з цельсія в фаренгейт:
# Напишіть програму, яка запитує в користувача кількість градусів в цельсіях і повертає в фаренгейтах.
# print("Enter degrees Celsius")
# celsius = input()
# celsius = float(celsius)
# fahrenheit = celsius * 9 / 5 + 32
# celsius = str(celsius)
# print(celsius, "degrees Celsius is ", fahrenheit, " degrees Fahrenheit")

# 8 Перевод з фаренгейта в цельсій:
# Напишіть програму, яка запитує в користувача кількість градусів в фаренгейтах і повертає в цельсіях.
# Вам може здатися, що ця задача така ж, як попередня, але будьте уважні і перевірте результат вручну.
# print("Enter degrees Fahrenheit")
# fahrenheit = input()
# fahrenheit = float(fahrenheit)
# celsius = 5 * (fahrenheit-32) / 9
# fahrenheit = str(fahrenheit)
# print (fahrenheit, "degrees Fahrenheit is ", celsius, "degrees Celsius")

# 9 Теорема Піфагора:
# Запитайте у користувача довжини катетів та виведіть на екран довжину гіпотенузи.
# Трикутник рівнобедрений. Що б взвести в степінь ставимо два рази множення
# два в степені три буде так 2**3, квадратний корінь з двух буде 2**(1/2)
# print ("The triangle is isosceles. Enter the length of the cathetus")
# cathetus = input()
# cathetus = float(cathetus)
# hypotenuse = (cathetus**2 + cathetus**2)**(1/2)
# print("Length of the hypotenuse - ", hypotenuse)

# 10 Школярі та яблука
# n школярів ділять k яблук порівну, недільний залишок залишається в кошику.
# Скільки яблук дістанеться кожному школярові та скільки залишиться в кошику?
# Програма отримує на вхід числа n і k - цілі, додатні, не перевищують 10000.
# print("Enter the number of children")
# children = input()
# print("Enter the numbers of the apples")
# apples = input()
# children = int(children)
# apples = int(apples)
# get_apples = apples // children
# apples_rest = apples % children
# print (get_apples, "apples will get each children and", apples_rest, " will remain in the basket")

# 11 Магазин канцелярських товарів
# Одного разу, відвідавши магазин канцелярських товарів, Вася купив X олівців, Y ручок та Z фломастерів. Відомо,
# що ціна ручки на 2 гривні більше ціни олівця та на 7 гривень менше ціни фломастера. Також відомо,
# що вартість олівця становить 3 гривні. Потрібно визначити загальну вартість покупки.
# Вхідні дані
# просимо користувача ввести три змінні
# кожне з яких не перевищує 109.
# Вихідні дані
# виведіть одне ціле число – вартість покупки в гривнях.
# приклад для перевірки програми 1
# ввів: 1 1 1
# отримав: 20
# print ("How many pens do you want to buy?")
# pens = input()
# print("How many pencils do you want to buy?")
# pencils = input()
# print ("How many markers do you want to buy?")
# markers = input()
# pens = int(pens)
# pencils = int(pencils)
# markers = int(markers)
# price = 3 * pens + 5 * pencils + 12 * markers
# print("The total cost of the purchase is ", price, " UAH")

# 12 Циферблад
# Запитайте в користувача скільки хвилин пройшло з початку доби.
# Визначте, скільки годин і хвилин покаже електронний годинник в цей момент і поверніть йому результат (формататування тексту при ввиводі не важливе).
# приклад для перевірки програми 1
# користувач ввів:150
# користувач отримує: 2, 30
# приклад для перевірки програми 2
# користувач ввів:1441
# користувач отримує: 0, 1
# print("How many minutes have passed since the beginning of the day?")
# min = input()
# min = int(min)
# hours = min // 60
# time_rest = min - hours * 60
# print (hours, "hours and", time_rest, "min")

# 13 Журавлики
# Петро, Катя та Сергій роблять з паперу журавликів. Разом вони зробили S журавликів.
# Скільки журавликів зробила кожна дитина, якщо відомо, що Петро та Сергій зробили однакову кількість журавликів,
# а Катя зробила в два рази більше журавликів, ніж Петро та Сергій разом.
# Вхідні дані
# Юзер вводить загальну кількість журавликів. Отримує три значення скільки зробив кожен (Петро, Катя та Сергій).
# print ("Enter the number of the cranes (integer multiple of 6)")
# cranes = input()
# cranes = int(cranes)
# each_boy = cranes // 6
# print ("Petro - ", each_boy, "Sergiy - ", each_boy, "Katya - ", 4 * each_boy)

# 14 Податки
# Прийшов час податків і вам треба написати програму що б допомогти відділу бугалтерії
# програма приймає від користувача його зарплату за 3 місяці та відсоток який він має сплатити.
# Виведіть на екран скільки треба сплатити податків за 3 місяці. Не забудьте ЄСВ(4422)
# print("Enter the salary for the first month")
# first_month = input()
# print("Enter the salary for the second month")
# second_month = input()
# print("Enter the salary for the first month")
# third_month = input()
# print("Enter percentage")
# percentage = input()
# first_month = float(first_month)
# second_month = float(second_month)
# third_month = float(third_month)
# percentage = float(percentage)
# amount_of_tax = (first_month + second_month + third_month) * percentage / 100 + 4422
# print(amount_of_tax, "UAH you need to pay taxes for 3 months")
