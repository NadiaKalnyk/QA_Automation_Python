from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.page.goto("http://uitestingplayground.com/sampleapp")
        self.username_field = self.page.locator("//input[contains(@placeholder, 'User Name')]")
        self.pass_field = self.page.locator("//input[contains(@name, 'Password')]")
        self.login_btn = self.page.locator("button#login")
        self.login_message_result = self.page.locator("label.text-success")

    def fill_login_form(self, username_value, password_value):
        self.username_field.fill(username_value)
        self.pass_field.fill(password_value)

    def click_login_button(self):
        self.login_btn.click()

