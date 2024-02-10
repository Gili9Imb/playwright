from test_actions.ClickAction import ClickAction
from test_actions.FillAction import FillAction
from test_actions.WaitAction import WaitAction


class Test:

    fill_action = FillAction()
    click_action = ClickAction()
    wait_action = WaitAction()
    def test_demo(self, page):
        page.goto("https://www.saucedemo.com/")
        print("Page opened")
        Test.fill_action.fillElement(page, "//input[@id='user-name']", "standard_user")
        Test.fill_action.fillElement(page, "//input[@id='password']", "secret_sauce")
        Test.click_action.clickOnElementByText(page, 'Login')
        Test.wait_action.waitforElement(page, "text", "Sauce Labs Backpack")




