# Створіть два файли в 1-му напишіть такі функції:
#
# 1) сортування списка по зростанню числа, від меншого до більшого. Функція приймає список з чисел і повертає відсортований список.
# 2) сортування списка на спад, від  більшого до меншого. Функція приймає список з чисел і повертає відсортований список.
# 3) сортування за кількістю букв у слові. Функція приймає список з слів і повертає відсортований список.
#
#  2-ий файл з трьома тестами який буде тестити ці три функції. В кожному тесті 1 тест.
#
# В тестових функціях ми ставимо типізацію. В першому файлі в всіх функціях проставляємо що приймає і що повертає.
# Встановіть собі пайтест і прораньте. До домашки отрім кода додайте скріншот прогона тестів.

list_1 = [1, 20, 0, -100, 34, -94, 0.3]
list_2 = ['lorem', 'ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the', 'printing', 'and', 'type', 'industry']


def sorting_by_abc(list_3: list) -> list:
    import copy
    list_3 = copy.deepcopy(list_2)
    if list_2 != []:
        list_3.sort()
    return list_3


def sorting_by_letters(sort: list) -> list:
    sort = sorted(sorting_by_abc(list_2), key=len)
    return sort


def ascending(sort: list) -> list:
    sort = sorted(list_1)
    return sort


def descending(sort: list) -> list:
    sort = sorted(list_1, reverse=True)
    return sort


ascending_sorting = ascending(sort=list_1)
descending_sorting = descending(sort=list_1)
sorting_by_letters_in_words = sorting_by_letters(sort=list_2)
print(ascending_sorting)
print(descending_sorting)
print(sorting_by_letters_in_words)
