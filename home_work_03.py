# Задача 1
#
# Уявимо що до нас прийшов наш друг або подруга і попросили написати додаток для покупок в магазині
# що б можна було скласти список продуктів та коли купуєш викреслювати(для викреслення питайте номер елемента,
# що б видалити по індексу треба його передати в pop list_a.pop(0) - видалить нульовий індекс, памятайте що користувач
# не знає що в нас індекси починаються з нуля)
# Також нам відомо що цей список має завжди пять елементів.
# Після кожного видалення елементу виводьте наш оновлений список.
# Після 5 видалень перевірте чи список пустий якщо не пустий напишіть що ось ще є продукти, якщо пусти то напишіть про це.
# Також після цього кроку запропонуйте користувачу написати ще продуктів та додати його в кошик. і виведіть їх на екран.
# Але цього разу вже без видалень.
# кроки:
# Спочатку пропонуємо користувачу ввести продукти.
# Робимо 5 запитів на видалення
# Перевіряємо корзину
# Пропонуємо додати продукти
# Виводмо список і прощаємось
print("Which products do you want to buy?")
product_list = input().split()
print(f"You have entered products for your purchase: {product_list}")
del_element = input(
    "Which product have you already purchased? I need to know the product number to remove it from the product list: ")
del_element = int(del_element)
basket = []
if del_element >= 1 and del_element <= len(product_list):
    product_1 = product_list.pop(del_element - 1)
    basket.append(product_1)
    print(product_list)
else:
    print(f"Wrong number. There is no product with {del_element} in the list {product_list}")
del_element = input(
    "Which product have you already purchased? ")
del_element = int(del_element)
if del_element >= 1 and del_element <= len(product_list):
    product_2 = product_list.pop(del_element - 1)
    basket.append(product_2)
    print(product_list)
else:
    print(f"Wrong number. There is no product with {del_element} in the list {product_list}")
del_element = input(
    "Which product have you already purchased? ")
del_element = int(del_element)
if del_element >= 1 and del_element <= len(product_list):
    product_3 = product_list.pop(del_element - 1)
    basket.append(product_3)
    print(product_list)
else:
    print(f"Wrong number. There is no product with {del_element} in the list {product_list}")
del_element = input(
    "Which product have you already purchased? ")
del_element = int(del_element)
if del_element >= 1 and del_element <= len(product_list):
    product_4 = product_list.pop(del_element - 1)
    basket.append(product_4)
    print(product_list)
else:
    print(f"Wrong number. There is no product with {del_element} in the list {product_list}")
del_element = input(
    "Which product have you already purchased? ")
del_element = int(del_element)
if del_element >= 1 and del_element <= len(product_list):
    product_5 = product_list.pop(del_element - 1)
    basket.append(product_5)
    print(f"We need to buy {product_list}")
else:
    print(f"Wrong number. There is no product with {del_element} in the list {product_list}")
print(f"You have already bought {basket}. There are {len(basket)} products in the basket")
add_product = input("Which product do you want to add to your purchase? ")
print(f"Your purchase was updated: {product_list.append(add_product)}")
