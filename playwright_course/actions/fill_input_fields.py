from playwright.sync_api import Page, expect


def test_get_started_link(page: Page):
    page.goto("https://bootswatch.com/default/")
    input = page.locator('input#exampleInputEmail1')
    input.fill("email@gmail.com") # enter data from input field
    input.clear() # delete data from input field