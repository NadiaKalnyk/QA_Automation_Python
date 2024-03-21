from playwright.sync_api import Page, expect


def test_get_started_link(page: Page):
    page.goto("https://bootswatch.com/default/")
    radio_btn = page.locator('input#optionsRadios1').check() #enable/disable radiobutton


    checkbox_btn = page.get_by_label("Default checkbox")
    checkbox_btn.check() # if checkbox_btn.is_checked() == True
    checkbox_btn.uncheck() # if checkbox_btn.is_checked() == False
    checkbox_btn.set_checked(True) # the same as checkbox_btn.check()
    checkbox_btn.set_checked(False) # the same as checkbox_btn.uncheck()
    checkbox_btn.click() #enable/disable checkbox

    switches_btn = page.locator("input#flexSwitchCheckDefault")
    switches_btn.check()
    switches_btn.uncheck()

