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
        print(f"My grades -> {self.ratings_list}")


student_1 = Student()
student_1.say_hello()
student_1.check_ratings()

student_2 = Student()
student_2.name = "Ivan"
student_2.say_hello()
student_2.ratings_list = [4, 3, 5, 5]
student_2.check_ratings()
