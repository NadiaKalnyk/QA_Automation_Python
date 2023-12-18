# Дзен пайтон кому цікаво подивіться
# Простота та очевидність
# коли треба присвоювати дефотні дані в функції
# def foo(element, list_a, flag=False):
#     list_a.append(element)
#     if flag:
#         list_a = sorted(list_a)
#     return list_a
#
#
# print(foo(34, [4444,143,47], True))



# OOP. Принципи ООП:
# 1. Абстракція (це коли ми відбераємо яксь певні характеристики для того щоб створити наш клас. Наш клас по дефолту
# нічого не має, тому все що ми в нього прописуємо воно в ньому і буде, тотбто дефолтно там нічого не має, але так як це
# абстрація то ми самі створюємо)
# 2. Інкапсуляція ( це коли наш клас має в собі все необхідне + це варіант схову якихось даних)
# 3. Наслідвання (можливість передавання методу одного класу в інший клас. Всі класи в пайтоні успадковуються від
# основного класу - Object)
# 4. Поліморфізм (це коли однакові методи виконують різні функції в залежності від того до якого класу належать об'єсти
# цих методів. Наприклад, використання знаку + в рядках і числах(в арифметичному варіанті він буде обчислювати суму,
# в варіанті із рядками - конкатинацію))
# string_a = "Hi"
# print(type(string_a))

# class MyClass:
#     pass
#
# my_obj = MyClass()
#
# # print(my_obj, type(my_obj))
# # print(dir(my_obj))
#
# class NameClass:
#     name = "Taras"
#     age = 21
#
#     def say_hello(self): # self - це посилання на об'єкт, який утворюється під час ініціалізації класа
#         self.age_name = f"{self.age}-річний {self.name}"
#         self.hello_string = f"привіт {self.age_name}, як справи?"
#         print(self.hello_string)
#
#     def say_goodbay(self):
#         print(f"гарного дня {self.age_name}")
#
#
# obj_1 = NameClass()
# print(obj_1.name)
# obj_1.say_hello()
# obj_1.say_goodbay()
# print("->", obj_1.age_name)
#
# obj_2 = NameClass()
# obj_2.name = "Pavlo"
# print(obj_2.name)
# obj_2.say_hello()
# obj_2.say_goodbay()
#
#
# obj_3 = NameClass()
# print(obj_3.name)


# ----пояснення в фалі test_...
# pytest-xdist
# пайтест маркери
# approx
# linter
# ----пояснення в фалі test_...