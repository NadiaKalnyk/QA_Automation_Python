from playwright.sync_api import Page, expect
from playwright_course.lesson_13_page_object_model.LoginPage01 import LoginPage

valid_username = 'username'
valid_pass = 'pwd'
success_text = f'Welcome, {valid_username}!'


def test_successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.fill_login_form(valid_username, valid_pass)
    login_page.click_login_button()
    expect(login_page.login_message_result).to_contain_text(success_text)