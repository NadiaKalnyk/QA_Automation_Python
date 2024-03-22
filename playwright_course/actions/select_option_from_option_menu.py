from playwright.sync_api import Page, expect


def css_locators(page: Page):
    page.goto('https://bootswatch.com/default/')
    select = page.get_by_label("Example select")
    select.select_option("4") # '4' is selected option in the context menu
    multi_select = page.get_by_label("Example multiple select")
    multi_select.select_option(["2", "4"]) # two options are selected in the CM