from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

URL = "https://demoqa.com/checkbox"


class CheckboxPage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self):
        self.driver.get(URL)
        return self

    def expand_folder(self, name) -> None:
        versatile_checkbox_button = self.driver.find_element(By.XPATH,
                                                             f"//label[contains(@for, 'tree-node-{name}')]//ancestor::span/button")
        try:
            expand = versatile_checkbox_button.find_element(By.XPATH, "//li[contains(@class, 'rct-node-collapsed')]")
            if expand.is_displayed():
                expand.click()
        except NoSuchElementException:
            pass
        versatile_checkbox_button.click()

    def collapse_folder(self, name) -> None:
        versatile_checkbox_button = self.driver.find_element(By.XPATH,
                                                             f"//label[contains(@for, 'tree-node-{name}')]//ancestor::span/button")
        try:
            expand = versatile_checkbox_button.find_element(By.XPATH, "//li[contains(@class, 'rct-node-expanded')]")
            if expand.is_displayed():
                expand.click()
        except NoSuchElementException:
            pass
        versatile_checkbox_button.click()

    def mark_folder(self, name):
        versatile_checkbox_button = self.driver.find_element(By.XPATH,
                                                             f"//label[contains(@for, 'tree-node-{name}')]/span[contains(@class, 'checkbox')]")
        input_field = self.driver.find_element(By.XPATH, f"//label[contains(@for, 'tree-node-{name}')]/input")
        if not input_field.is_selected():
            versatile_checkbox_button.click()

    def unmark_folder(self, name):
        versatile_checkbox_button = self.driver.find_element(By.XPATH,
                                                             f"//label[contains(@for, 'tree-node-{name}')]/span[contains(@class, 'checkbox')]")
        try:
            input_field = self.driver.find_element(By.XPATH, "//*[contains(@class, 'uncheck')]")
            if not input_field.is_displayed():
                input_field.click()
        except NoSuchElementException:
            pass
        versatile_checkbox_button.click()

    def get_text_results(self):
        list_message = []
        messages = [message.text for message in self.driver.find_elements(By.XPATH, "//span[@class='text-success']")]
        list_message.extend(messages)  # Додаємо всі текстові повідомлення до списку
        return list_message

    def scroll_down(self) -> None:
        self.driver.execute_script("window.scrollBy(0, 200);")

        # //*[contains(@class, "expand-open")] - відкрито
        # //*[@class="rct-icon rct-icon-expand-close"]
