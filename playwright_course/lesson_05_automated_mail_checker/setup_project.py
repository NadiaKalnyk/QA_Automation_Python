from playwright.sync_api import sync_playwright


with (sync_playwright() as playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(storage_state="/Users/user/PycharmProjects/QA_Automation_Python/playwright/"
                                                "04_authentication/auth/storage_state.json")
    page = context.new_page()
    page.goto("https://app.acceptance.s-trust.de")