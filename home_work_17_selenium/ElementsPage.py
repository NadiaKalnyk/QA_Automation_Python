from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ElementsPage:
    def __init__(self, driver: WebDriver):
        self.url = "https://demoqa.com/elements"
        self.driver = driver
        self.element_categries = (By.XPATH, "//div[contains(@class, show)]//li")

    def open(self) -> "ElementsPage":
        self.driver.get(self.url)
        return self

    def get_elements_page_categories(self):
        categories = [cat.text for cat in self.driver.find_elements(*self.element_categries)]
        return categories
