# # property
# class A:
#     def __init__(self, age):
#         self.__age = age
#
#     @property
#     def our_age(self):
#         return self.__age
#
#     @our_age.setter
#     def our_age(self, value):
#         print("-->")
#         if not isinstance(value, int) or value > 100:
#             raise ValueError("Ви повинні бути молодші 100 років і воно повино бути числом.")
#         self.__age = value
#
#     def say_age(self):
#         print(self.__age)
#
# a = A(32)
# print(a.our_age)
# a.our_age = 90
# print(a.our_age)
# # a.say_age()


# staticmethod
# classmethod
# Метод класу — це метод, який прив’язаний до класу, а не до його об’єкта. Він не вимагає створення екземпляра класу,
# як і статичний метод. Він може змінювати стан класу, який застосовуватиметься до всіх екземплярів класу.
# Наприклад, він може змінити змінну класу, яка буде застосовна до всіх екземплярів.
#
# Статичний метод — це метод, який прив’язаний до класу, а не до об’єкта класу.
# Цей метод не може отримати доступ або змінити стан класу. Ми використовуємо статичні методи для створення службових
# функцій (які доступні всім, не лише об'єктам нашого класу)
#
# Різниця між статичним методом та методом класу полягає в наступному:
#  - статичні методи нічого не знають про клас і просто працюють із параметрами (метод класу приймає cls як перший
#     параметр, тоді як статичний метод не потребує конкретних параметрів);
#  - метод класу працює із класом, оскільки його параметром завжди є сам клас (метод класу може отримати доступ або
#    змінити стан класу, тоді як статичний метод не може отримати доступ або змінити його)


class Bank:
    general_message = "25 січня всі всі святкують різдво з чим ми вас і ватаємо"

    def __init__(self, name, amount, text):
        self.name = name
        self.amount = amount
        self.text = text

    @classmethod
    def change_general_message(cls, value):
        cls.general_message = value

    def print_private_message(self):
        print(self.text)

    def print_general_message(self):
        print(self.general_message)

    @staticmethod
    def view_dollar_value():
        print("8 гривень за доллар")


# a_1 = Bank("Андрій", 4500, "Твій регіон Київ")
# a_2 = Bank("Віталій", 5500, "Твій регіон Одеса")
# a_1.change_general_message("робочі дні за розкладом")
# a_1.print_private_message()
# a_2.print_private_message()
# a_1.print_general_message()
# a_2.print_general_message()

# Bank.view_dollar_value()

# dict = {
#     "a": {"b": 100}
#         }
# print(dict["a"]["b"])

# comprehantion
# list
# list_a = []
# for i in range(9):
#     list_a.append(i ** 2)
# print(list_a)
#
# list_b = [i ** 2 for i in range(9)]
# print(list_b)
#
# list_c = [i for i in range(9) if i % 2 == 0]
# print(list_c)

# dict
dict_a = {}
# for i in range(9):
#     dict_a[i] = i ** 2
#
# print(dict_a)
#
# dict_b = {i: i**2 for i in range(9)}
# print(dict_b)
#
# dict_c = {"key_1": "value_1", "key_2": "value_2", "key_3": "value_3"}
# dict_d = {value: key for key, value in dict_c.items()}
# print(dict_c)
# print(dict_d)
# print(dict_c["key_1"])
# print(dict_d["value_1"])

# set
# set_a = set()
# for i in range(9):
#     set_a.add(i)
# print(type(set_a))
# print(set_a)
#
# set_b = {i for i in range(9)}
# print(set_b)



# Iterator  #todo
# my_string = "Я звичайна стрічка"
# print(type(my_string))
# itr = iter(my_string)
# print(type(itr))
# for i in my_string:
#     print(i, end="->")
# print()

# for i in itr:
#     print(i, end="->")

# print(next(itr))
# print("fdfs")
# print(next(itr))
# print("ffds")
# print(next(itr))
# print("ffdsfs")
# print(next(itr))


# generator   #todo
def func_generator():
    print("step 1")
    yield "один"
    print("step 2")
    yield "два"
    print("step 3")
    yield "три"
    print("step 4")
    yield "чотири"

gen = func_generator()
print(next(gen))
print("dsfdfsdfds")
print(next(gen))
print("dsfdfsdfds")
print(next(gen))