from playwright.sync_api import Page, expect


def css_locators(page: Page):
    page.goto('https://bootswatch.com/default/')
    dropdown_menu = page.locator("button#btnGroupDrop1")
    dropdown_menu.click()
    option = page.locator("//div[contains(@class, 'dropdown-menu')]/a[contains(text(), 'Default')]:visible")
    option.click()