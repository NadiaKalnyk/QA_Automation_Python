import pytest
from selenium import webdriver


@pytest.fixture
def chrome():
    driver = webdriver.Chrome()
    driver.get("C:/Users/admin/PycharmProjects/python_course/QA_Automation_Python/home_work_17_selenium/chromedriver")
    yield driver
    driver.quit()
