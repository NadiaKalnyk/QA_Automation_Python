# Задача 1
# 1) Напишіть 10 тестів(можна що б просто повертали Тру(щоб проходили)) імена тестів повині йти підряд
# test_1, test_2 ... . Повішайти на них три декоратора old, main, new. кожен декоратор повинен бути на 3 функціях
# на одній з функцій повино бути повішано два декоратора old i main.
# додайти їх в python.ini що б були правильні виводи
#
# Зробіть такі прогони
# 1) всі тексти де немає лейби old -> pytest -m "not old" -v
# 2) тест де пересікаються old i main. -> pytest -m "old and main" -v
# 3) тести з маркерами main, new -> pytest -m "main or new" -v
import pytest

@pytest.mark.old
def test_1():
    assert True

@pytest.mark.old
def test_2():
    assert True

@pytest.mark.main
def test_3():
    assert True

@pytest.mark.new
def test_4():
    assert True

@pytest.mark.main
def test_5():
    assert True

@pytest.mark.old
@pytest.mark.main
def test_6():
    assert True

def test_7():
    assert True

@pytest.mark.new
def test_8():
    assert True

@pytest.mark.main
def test_9():
    assert True

@pytest.mark.new
def test_10():
    assert True

