from  playwright.sync_api import Page, expect


def test_login(page: Page):
    page.goto("http://uitestingplayground.com/sampleapp")

    username_field = page.locator("//input[contains(@placeholder, 'User Name')]")
    pass_field = page.locator("//input[contains(@name, 'Password')]")
    login_btn = page.locator("button#login")
    login_result = page.locator("label.text-success")

    valid_username = 'username'
    valid_pass = 'pwd'
    success_text = f'Welcome, {valid_username}!'

    username_field.fill(valid_username)
    pass_field.fill(valid_pass)
    login_btn.click()

    expect(login_result).to_contain_text(success_text)