import pytest
from home_work_09 import add_three_numbers

# solution 1
def test_all_numbers_are_positive():
    assert add_three_numbers(1, 2, 3) == 6


def test_first_is_positive_other_negative():
    assert add_three_numbers(-1,2,3) == 4


def test_all_are_negative():
    assert add_three_numbers(-1, -2, -3) == -6

# solution 2
@pytest.mark.parametrize("number_1, number_2, number_3, addition_result", [
    pytest.param(1, 2, 3, 6, id="all numbers are positive"),
    pytest.param(-1, 2, 3, 4, id="first is positive, other negative"),
    pytest.param(-1, -2, -3, -6, id="all are negative")])
def test_set_1(number_1, number_2, number_3, addition_result):
    assert add_three_numbers(number_1, number_2, number_3) == addition_result

# solution 3

list_test = [(1, 2, 3, 6), (-1, 2, 3, 4), (-1, -2, -3, -6)]
@pytest.mark.parametrize("num_1, num_2, num_3, result", list_test)
def test_set_2(num_1, num_2, num_3, result):
    assert add_three_numbers(num_1, num_2, num_3) == result
