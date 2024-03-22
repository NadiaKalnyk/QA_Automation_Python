from playwright.sync_api import Page, expect


def css_locators(page: Page):
    page.goto("https://bootswatch.com/default/")
    choose_file_btn = page.locator("//input[contains(@type, 'file')]")
    choose_file_btn.set_input_files("info.txt") # info.txt - file that lacates in the folder 'playwright'
    choose_file_btn.set_input_files(['file01.txt', 'file02.txt']) # uploads multiple files

    with page.expect_file_chooser() as fc_info:
        file_chooser = fc_info.value
        file_chooser.set_files("info.txt")
