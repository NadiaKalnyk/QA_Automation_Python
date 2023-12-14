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
    def write_file(n_1: int | float, n_2: int | float, n_3: int | float) -> None:
        with open("log.txt", "a") as file:
            result = func(n_1, n_2, n_3)
            file.write(f'You numbers: {n_1}, {n_2}, {n_3}.  ')
            file.write(f' Their sum = {result}')
            return result
    return write_file
@func_wrapper_sum
def add_three_numbers(n_1 : int|float, n_2 : int|float, n_3 : int|float) -> int|float:
    result = n_1 + n_2 + n_3
    return result
add_three_numbers(1, 2, 3)


