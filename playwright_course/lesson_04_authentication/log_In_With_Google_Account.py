from playwright.sync_api import sync_playwright, Playwright


def run(playwright: Playwright):
    firefox = playwright.firefox # or "chromium" or "webkit".
    browser = firefox.launch(headless=False,
                                         slow_mo=500)  # запуск браузера, якщо headless=False, то буде видно
    page = browser.new_page()
    page.goto('https://accounts.google.com/')
    dismiss_btn = page.get_by_role("button", name="Dismiss")
    dismiss_btn.click()
    email_input = page.locator("//input[contains(@aria-label, 'Email or phone')]")
    email_input.fill('kalnuk.2016.nadiya@gmail.com')
    next_btn = page.get_by_role("button", name="Next")
    next_btn.click()
    password_input = page.get_by_label("Enter your password")
    password_input.fill('my_pass')
    next_btn.click()



with sync_playwright() as playwright:
    run(playwright)