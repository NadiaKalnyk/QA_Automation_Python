from playwright.sync_api import Page, expect


def css_locators(page: Page):
    page.goto("https://bootswatch.com/default/")
    textarea = page.locator("Example textarea")
    textarea.press("KeyW") #'w' lovercase letter is entered
    textarea.press("Shift + KeyW") #'W' uppercase letter is entered