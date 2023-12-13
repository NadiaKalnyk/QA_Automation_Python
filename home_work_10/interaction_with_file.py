# Задача 2
# Візьміть задачу з минулого уроку(3) модернізуйте її так що кожний раз коли ми її запускаємо те що ми
# туди передаєм та результат повинно записуватись в файл log.txt

# Зверніть увагу на те що в файл повинно дозаписуватись, а не затератись.
# Уявіть що ця функція являється легасі кодом і ви її не можете змінювати,тому потрібно використовувати декоратор.

# Я хотів би бачити таку реалізацію в домашці три функції:
# 1. функція з минулого уроку
# 2. функція що записую текст
# 3. декоратор

# Home_wokr_9 -> task_3:
# зробіть функцію як ми робили з додаванням тільки замість двох чисел зробіть три числа і
# протестуйте її всіма трьома методами

def func_wrapper_sum(func):
    def wrapper(n_1 : int|float, n_2 : int|float, n_3 : int|float) -> int|float:
        result = n_1 + n_2 + n_3
        return n_1, n_2, n_3, result
    return wrapper
@func_wrapper_sum
def foo_1(n_1 : int|float, n_2 : int|float, n_3 : int|float) -> int|float:
    result = n_1 + n_2 + n_3
    return result

all_positive = foo_1(-1, 2, 3)

with open("log.txt", "a") as file:
    file.write(f'You added numbers: {all_positive[0]}, {all_positive[1]}, {all_positive[2]}. ')
    file.write(f' Their sum = {all_positive[-1]}.   ')


