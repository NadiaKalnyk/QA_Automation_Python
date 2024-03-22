from playwright.sync_api import Page, expect


def test_text_input(page: Page):
    page.goto("http://uitestingplayground.com/textinput")
    input_field = page.get_by_placeholder("MyButton")

    text = 'ggfhdfndfkd'
    input_field.fill(text)

    btn = page.locator("button#updatingButton")
    btn.click()

    expect(btn).to_contain_text(text) #name of the button is changed after click
