# 2) Напишіть 5 тестів з затримкою в 2 секунди кожен, один з тестів повинен мати унікальне імя.
#  Запустіть їх за домогою pytest-xdist(pip install pytest-xdist)
#  ліби в 5 потоків -> pytest .\test_home_work_11.py -v -n=5
#  Запустіть цей ваш унікальний тест з маркером -k -> pytest .\test_home_work_11.py -k "last_sleep"
#  додайте скірншоти виконання(не забудьте додавати -v, що б я бачив що ви проганяли) і біля
#  скріншотів пропишіть команди, які ви використовували.
import time


def test_sleep():
    print("Sleep 2 sec")
    time.sleep(2)


def test_wait():
    print("Wait 2 sec")
    time.sleep(2)


def test_double_sleep():
    print("Double sleep 2 sec")
    time.sleep(2)


def test_double_wait():
    print("Double wait 2 sec")
    time.sleep(2)


def test_last_sleep():
    print("The last sleep 2 sec")
    time.sleep(2)
