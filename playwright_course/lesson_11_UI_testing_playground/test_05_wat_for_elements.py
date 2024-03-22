from playwright.sync_api import Page, expect


def test_ajaks_data(page: Page):
    page.goto("http://uitestingplayground.com/ajax")
    btn = page.locator("button.btn-primary")
    btn.click()

    text_appears = page.locator("p.bg-success")
    text_appears.wait_for()

    expect(text_appears).to_be_visible()
