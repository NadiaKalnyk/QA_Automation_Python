from python_course.QA_Automation_Python.home_work_17_selenium import TextBoxPage


class TestTextBox:

    def test_username_fill_and_check(self, chrome):
        page = TextBoxPage.TextBoxPage(chrome)
        page.open()
        page.fill_full_name_field("Pavlo")
        page.scroll_down()
        page.click_submit()
        name_field = page.get_result_fullname()
        assert name_field.replace("Name:", "") == "Pavlo"

    def test_email_fill_and_check(self, chrome):
        page = TextBoxPage.TextBoxPage(chrome)
        page.open()
        page.fill_email_field("pavlo1001@gmail.com")
        page.scroll_down()
        page.click_submit()
        result = page.get_result_email()
        assert result.replace("Email:", "") == "pavlo1001@gmail.com"

    def test_curr_addr_fill_and_check(self, chrome):
        page = TextBoxPage.TextBoxPage(chrome)
        page.open()
        page.fill_current_address_field("Poltava")
        page.scroll_down()
        page.click_submit()
        result = page.get_result_current_address()
        assert result.replace("Current Address :", "") == "Poltava"

    def test_perm_addr_fill_and_check(self, chrome):
        page = TextBoxPage.TextBoxPage(chrome)
        page.open()
        page.fill_permanent_address_field("Poltava")
        page.scroll_down()
        page.click_submit()
        result = page.get_result_permanent_address()
        assert result == "Permananet Address :Poltava"
