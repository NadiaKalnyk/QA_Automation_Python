from playwright.sync_api import sync_playwright, Playwright


def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto('https://playwright.dev/python/docs/intro')
    link_option = page.locator("a.dropdown-item")
    link_option.click(timeout=2_000) # wait for the page to load (loader in the browser tab)

    browser.close()


with sync_playwright() as playwright:
    run(playwright)