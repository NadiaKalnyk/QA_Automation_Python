import pytest
from QA_Automation_Python.home_work_17_selenium.CheckboxPage import CheckboxPage
import time


@pytest.mark.usefixtures("chrome_class")
class TestCheckboxPage:
    def setup(self):
        self.page = CheckboxPage(self.driver)

    def test_page(self):
        self.page.open()
        self.page.expand_folder("home")
        self.page.mark_folder("home")
        self.page.collapse_folder("home")
        self.page.unmark_folder("home")
        pass

    def test_checkboxes(self):
        self.page.open()
        self.page.scroll_down()
        self.page.expand_folder("home")
        self.page.mark_folder("desktop")
        self.page.expand_folder("documents")
        self.page.mark_folder("office")
        actual_text = self.page.get_text_results()
        expected_text = ["desktop", "notes", "commands", "office", "public", "private", "classified", "general"]
        assert actual_text == expected_text
