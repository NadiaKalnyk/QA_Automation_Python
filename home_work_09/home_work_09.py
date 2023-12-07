# 1) додайте requirements.txt на ваш гіт
# 2) Виберіть будь-яку помилку яка вам подобається і зробіть функцію яка перевіряє на цю помилку(в функції try except)

def delete_element(i : int, list_a : list) -> list:
    try:
        list_a.pop(i)
    except LookupError:
        print("Element is NOT removed. Index out of bound")
    return list_a
try:
    result = delete_element(10, list_a = [8, 6, 5, 3, 0])
    print(result)
except (NameError, TypeError):
    print("Invalid type of element")


# 3) зробіть функцію як ми робили з додаванням тільки замість двох чисел зробіть три числа і протестуйте її всіма трьома
# методами

def add_three_numbers(n_1 : int|float, n_2 : int|float, n_3 : int|float) -> int|float:
    result = n_1 + n_2 + n_3
    return result

# 4) перепишіть декоратор який заміряє час з уроку в домашку, можете його поклацати, як він працює
from datetime import datetime
def func_wrapper_time(func):
    def wrapper(*arg, **kwargs):
        start = datetime.now()
        print("Real time: ", start)
        result = func(*arg, **kwargs)
        delta_time = datetime.now() - start
        print("Measure time: ", delta_time)
        result
    return  wrapper

import time
@func_wrapper_time
def foo_1(*args, **kwargs):
    print("foo_1")
    time.sleep(1)

@func_wrapper_time
def foo_2(*args, **kwargs):
    print("foo_2")
    time.sleep(2)

foo_1()
foo_2()