from QA_Automation_Python.home_work_17_selenium.DynamicPropertiesPage import PageDynamicProperties
from selenium.webdriver.remote.webelement import WebElement


class TestDynamicProperties:

    def test_is_button_enable(self, chrome):
        page = PageDynamicProperties(chrome).open()
        button: WebElement = page.disable_enable_button()
        button.click()

    def test_is_button_shown(self, chrome):
        page = PageDynamicProperties(chrome).open()
        button: WebElement = page.invisible_visible_button()
        button.click()
