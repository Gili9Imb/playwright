from playwright.sync_api import sync_playwright
from test_actions.ClickAction import ClickAction
from test_actions.FillAction import FillAction
from test_actions.WaitAction import WaitAction


class Test2:
    fill_action = FillAction()
    click_action = ClickAction()
    wait_action = WaitAction()

    def test_demo(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, slow_mo=3 * 1000)
            page = browser.new_page()
            page.goto("https://www.saucedemo.com/")
            print("Page opened")

            # Actions performed on the page
            Test2.fill_action.fillElement(page, "//input[@id='user-name']", "standard_user")
            Test2.fill_action.fillElement(page, "//input[@id='password']", "secret_sauce")
            Test2.click_action.clickOnElementByText(page, 'Login')
            Test2.wait_action.waitforElement(page, "text", "Sauce Labs Backpack")


# Create a Test object and run the test
test_instance = Test2
