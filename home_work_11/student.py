# 1) Створіть клас Студент, в ньому обявіть дві змінні імя де збережети імя студента, та список його оцінок.
# створіть два метода в цьому класі, перший метод який буде вітатись і при вітання використовувати імя студента.
# другий метод буде виводити оцінки. Методи виводять результат через прінти.
# Створіть два екземпляра цього класу, в другому екземплярі змніть імя на своє(не міняючи нічого в класі). Вивідіть дві
# функції цих екземплярів, що б кожен студент привітався та сказав свої оцінки.

class Student:
    name = 'Nadia'
    ratings_list = [5, 5, 5, 5]

    def say_hello(self):
        print(f"Hello, I'm {self.name}!")

    def check_ratings(self):
        for index, value in enumerate(self.ratings_list):
            if value not in (1, 2, 3, 4, 5):
                raise ValueError("5-point rating scale")
        if len(self.ratings_list) != 4:
            raise Warning("4 exams")
        else:
            for index, value in enumerate(self.ratings_list):
                if value == 5 not in (1, 2, 3, 4):
                    print(f"My rainting is {self.ratings_list}. I got Excelent!")
                elif value <= 3 and value not in (4, 5):
                    print(f"My rainting is {self.ratings_list}. I got Satisfaction!")
                elif value in (4,5):
                    print(f'My rainting is {self.ratings_list}. I got Good!')
                else:
                    print(
                        f"My raitings is {self.ratings_list}. I passed only {len(self.ratings_list)} exams and failed the session!")


student_1 = Student()
student_1.say_hello()
student_1.ratings_list = [5, 5, 5, 4]
student_1.check_ratings()

# student_2 = Student()
# student_2.name = "Ivan"
# student_2.say_hello()

#
# 2) Напишіть 5 тестів з затримкою в 2 секунди кожен, один з тестів повинен мати унікальне імя.
#  Запустіть їх за домогою pytest-xdist ліби в 5 потоків.
#  Запустіть цей ваш унікальний тест з маркером -k
#  додайте скірншоти виконання(не забудьте додавати -v, що б я бачив що ви проганяли) і біля скріншотів пропишіть команди
#  які ви використовували.

# a = [2,3,4]
# for index, value in enumerate(a):
#     my_list = []
#     my_list = my_list.extend(value)
#     print(my_list)

# >>> def even_items(iterable):
# ...     """Return items from ``iterable`` when their index is even."""
# ...     values = []
# ...     for index, value in enumerate(iterable, start=1):
# ...         if not index % 2:
# ...             values.append(value)
# ...     return values
# ...
