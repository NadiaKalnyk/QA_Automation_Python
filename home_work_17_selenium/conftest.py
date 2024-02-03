import pytest
from selenium import webdriver


@pytest.fixture
def chrome():
    driver = webdriver.Chrome()
    driver.get("C:/Users/admin/PycharmProjects/python_course/QA_Automation_Python/home_work_17_selenium/chromedriver")
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def firefox(request):
    driver = webdriver.Firefox()
    driver.get("C:/Users/admin/PycharmProjects/python_course/QA_Automation_Python/home_work_17_selenium/geckodriver")
    request.cls.driver = driver
    # driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def chrome_class(request):
    driver = webdriver.Chrome()
    driver.get("C:/Users/admin/PycharmProjects/python_course/QA_Automation_Python/home_work_17_selenium/chromedriver")
    request.cls.driver = driver
    yield driver
    driver.quit()
