from playwright.sync_api import sync_playwright, Playwright


def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto('https://www.scrapethissite.com/pages/ajax-javascript/')
    link = page.get_by_role("link", name="2015")
    link.click()
    page.wait_for_selector(selector='td.film-title')# wait for the elements on the page to load (loader on the page)
    browser.close()


with sync_playwright() as playwright:
    run(playwright)