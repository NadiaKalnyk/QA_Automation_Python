import pytest
from python_course.QA_Automation_Python.home_work_17_selenium import ElementsPage


class TestElements:

    def test_check_number_of_elements(self, chrome):
        page = ElementsPage.ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        assert len(elements) == 33

    @pytest.mark.parametrize("element_names",
                             ["Text Box", "Check Box", "Radio Button", "Web Tables", "Buttons", "Links",
                              "Broken Links - Images", "Upload and Download", "Dynamic Properties", "", "", "", "", "",
                              "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""])
    def test_check_element_names(self, chrome, element_names):
        page = ElementsPage.ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        assert element_names in elements
