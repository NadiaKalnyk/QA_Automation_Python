from QA_Automation_Python.home_work_07.home_work_07 import ascending
from QA_Automation_Python.home_work_07.home_work_07 import descending
from QA_Automation_Python.home_work_07.home_work_07 import sorting_by_letters


def test_ascending_sorting():
    assert ascending(sort=[1, 20, 0, -100, 34, -94, 0.3]) == [-100, -94, 0, 0.3, 1, 20, 34]


def test_descending_sorting():
    assert descending(sort=[1, 20, 0, -100, 34, -94, 0.3]) == [34, 20, 1, 0.3, 0, -94, -100]


def test_sorting_by_letters_in_words():
    assert sorting_by_letters(sort=
                              ['lorem', 'ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the', 'printing',
                               'and', 'type', 'industry']) == ['is', 'of', 'and', 'the', 'text', 'type',
                                                               'dummy', 'ipsum', 'lorem', 'simply', 'industry',
                                                               'printing']
