import pytest
from python_course.QA_Automation_Python.home_work_15.calculator import Calculator
from datetime import datetime


class TestClass:
    @classmethod
    def setup_class():
        start = datetime.now()
        print("\nWe started test", start)

    @classmethod
    def teardown_class():
        with open("calc_info.txt", "w") as file:
            text = str(Calculator().info())
            file.write(text)
        finish = datetime.now()
        print("\nWe have finished test", finish)

    @pytest.mark.parametrize("number_1, number_2, expected", [
            pytest.param(1, 3, 4, id="1 test"),
            pytest.param(2, 2, 4,  id="2 test"),
            pytest.param(-1, -2, -3, id="3 test"),
            pytest.param(-2.2, -2.2, -4.4, id="4 test"),
            pytest.param(5, -2, 3, id="5 test")])
    def test_addition(self, number_1, number_2, expected):
        result = Calculator().addition(number_1, number_2)
        assert result == expected

    @pytest.mark.parametrize("number_1, number_2, expected", [
            pytest.param(3, 3, 1, id="1 test"),
            pytest.param(9, 3, 3,  id="2 test"),
            pytest.param(-10, -2, 5, id="3 test"),
            pytest.param(-2.2, -2.2, 1, id="4 test"),
            pytest.param(51, -2, -25.5, id="5 test")])
    def test_division(self, number_1, number_2, expected):
        result = Calculator().division(number_1, number_2)
        assert result == expected
