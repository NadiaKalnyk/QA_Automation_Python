from playwright.sync_api import Page, expect


def test_get_started_link(page: Page):
    page.goto("https://bootswatch.com/default/")
    block_button = page.get_by_role("button", name="Block button")
    block_button.first.dblclick() #double click
    block_button.click(button="right") #right click
    block_button.click(modifiers=["Shift"]) #click + press Shift
    block_button.hover()


