# CSS selectors:
# - Tagname
# - Classname
# - ID
# - Attribute/Value
from playwright.sync_api import Page, expect


def css_locators(page: Page):
    page.goto('https://bootswatch.com/default/')
    page.locator("css= p button.btn-success.disabled").highlight() #p -parent tag, tagname.classname
    page.locator("button#btnGroupDrop1") #tagname#ID
    page.locator("div.col-sm-10 input[readonly]") #div.col-sm-10 - parant tagname.classname tagname[attribute]
    page.locator("input[value='correct value']") # tagname[value='valueName']
    page.locator("nav.bg-dark a.nav-link.active") #nav.bg-dark - found parent element, a.nav-link.active - found dotherEl
    page.locator(":nth-match(button.btn-primary, 4)")  #вибір 4-го ел по локатору button.btn-primary зі списку 74 ел

    page.locator("//h1[@id='navbars']") #h1 - tagname
    page.locator("//div/input[@readonly]") #parentTagName/tagname[@attribute]
    page.locator("//input[@value='wrong value']")
    page.locator("//h1[contains(text(), 'Head')]")
    page.locator("//button[contains(@class, 'btn-primary btn-lg')]")
    page.locator("//input[contains(@value, 'correct')]")

    page.get_by_role("button", name="Primary").locator("nth=1") # select 1 Primary button from buttons list