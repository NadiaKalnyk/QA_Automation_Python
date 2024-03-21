#delete screenshot before runing test
from playwright.sync_api import Page

DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_page_has_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")
    page.screenshot(path='/Users/user/PycharmProjects/QA_Automation_Python/playwright/'
                         '09_playwright_tools/screenshot/page_screen.png')

    link = page.get_by_role("link", name="GET STARTED")
    page.screenshot(path='/Users/user/PycharmProjects/QA_Automation_Python/playwright/'
                         '09_playwright_tools/screenshot/full_page.jpg', full_page=True)
    link.screenshot(path='/Users/user/PycharmProjects/QA_Automation_Python/playwright/'
                    '09_playwright_tools/screenshot/get_started_button.png')
    link.click()

    assert page.url == DOCS_URL