from playwright.sync_api import Page, expect


def test_get_started_link(page: Page):
    page.goto("https://bootswatch.com/default/")
    page.get_by_role("button", "Default button").highlight()  # role->button, button's name -> Default button
    page.get_by_role("heading", "Heading 2")
    page.get_by_role("radio", "Option one is this and that—be sure to include why it's great")
    page.get_by_role("checkbox", "Default checkbox").check()
    page.get_by_label("Valid input").highlight()


