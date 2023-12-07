from QA_Automation_Python.home_work_07.home_work_07 import ascending_sorting
from QA_Automation_Python.home_work_07.home_work_07 import descending_sorting
from QA_Automation_Python.home_work_07.home_work_07 import sorting_by_letters_in_words


def test_ascending_sorting():
    assert ascending_sorting  == [-100, -94, 0, 0.3, 1, 20, 34]

def test_descending_sorting():
    assert descending_sorting == [34, 20, 1, 0.3, 0, -94, -100]

def test_sorting_by_letters_in_words():
    assert (sorting_by_letters_in_words ==
            ['is', 'of', 'and', 'the', 'text', 'type', 'dummy', 'ipsum', 'lorem', 'simply', 'industry', 'printing'])