from playwright.sync_api import Page, expect


def test_check_text(page: Page):
    page.goto("http://uitestingplayground.com/verifytext")

    text = page.locator("//div/span[contains(@class, 'badge-secondary')]")

    expect(text).to_have_text('Welcome UserName!')
