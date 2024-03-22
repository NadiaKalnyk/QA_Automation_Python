from playwright.sync_api import sync_playwright, Playwright


def on_dialog(dialog):
    dialog.accept() #autoclick on the 'Ok' button in alert
    dialog.dismiss() #autoclick on the 'Cancel' button in alert

def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto('https://testpages.eviltester.com/styled/alerts/alert-test.html')
    page.on("dialog", on_dialog)

    show_alert_btn = page.locator("//input[contains(@onclick, 'show_confirm()')]")
    show_alert_btn.click()

    browser.close()


with sync_playwright() as playwright:
    run(playwright)