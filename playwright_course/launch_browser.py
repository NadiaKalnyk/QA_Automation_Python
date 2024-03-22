from playwright.sync_api import sync_playwright, Playwright


def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch(headless=False,
                                         slow_mo=500)  # запуск браузера, якщо headless=False, то буде видно
    page = browser.new_page()
    page.goto('https://playwright.dev/python/docs/intro')
    # other actions...
    # Locate a link element with "Docs" text
    docs_button = page.get_by_role("link", name="Docs")
    docs_button.click()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
