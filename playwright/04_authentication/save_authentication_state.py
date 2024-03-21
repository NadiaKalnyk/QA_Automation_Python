from playwright.sync_api import sync_playwright


with (sync_playwright() as playwright):

    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    page = context.new_page()

    # Visit google accounts
    page.goto("https://app.acceptance.s-trust.de/app/#/login")

    # Enter email address
    email_input = page.locator("//input[contains(@focus-on-event, 'FOCUS_LOGIN_USERNAME')]")
    email_input.fill("hartley.jozie@meshfor.com")

    # Enter password
    password_input = page.locator("//input[@type='password']")
    password_input.fill('123456qQ.123')

    login_btn = page.locator("//span[@translate='BUTTON_LOGIN']")
    login_btn.click()

    # Pause if your account has two-factor authentication
    # then complete the same before resuming
    # page.pause()

    # Save authentication state
    context.storage_state(
        path="/Users/user/PycharmProjects/QA_Automation_Python/playwright/04_authentication/auth/storage_state.json")
    browser.close()
