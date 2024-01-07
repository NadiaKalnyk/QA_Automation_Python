import pytest
from datetime import datetime
from python_course.QA_Automation_Python.home_work_15.calculator import Calculator


@pytest.fixture(scope="class")
def test_time():
    Calculator().info()
    start = datetime.now()
    print("\nWe started test", start)
    yield
    finish = datetime.now()
    print("\nWe have finished test", finish)
    print("Time spent on testing", finish - start)
