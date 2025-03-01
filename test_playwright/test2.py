import unittest
from playwright.sync_api import sync_playwright
from test_actions.ClickAction import ClickAction
from test_actions.FillAction import FillAction
from test_actions.OpenUrl import OpenUrl
from test_actions.WaitAction import WaitAction

class Test2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fill_action = FillAction()
        cls.click_action = ClickAction()
        cls.wait_action = WaitAction()
        cls.open_url = OpenUrl()
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=False)
        cls.context = cls.browser.new_context()

    @classmethod
    def tearDownClass(cls):
        cls.context.close()
        cls.browser.close()
        cls.playwright.stop()

    def get_page(self):
        return self.context.new_page()

    def test_demo(self):
        page = self.get_page()
        self.open_url.runUrl(page, "https://www.saucedemo.com/")
        print("Page opened")
        self.fill_action.fillElement(page, "//input[@id='user-name']", "standard_user")
        self.fill_action.fillElement(page, "//input[@id='password']", "secret_sauce")
        self.click_action.clickOnElementByText(page, 'Login')
        self.wait_action.waitforElement(page, "text", "Sauce Labs Backpack")

        # Assertions to verify the test
        self.assertEqual(page.url, "https://www.saucedemo.com/inventory.html", "Failed to login")
        self.assertTrue(page.locator("text=Sauce Labs Backpack").is_visible(), "Sauce Labs Backpack not visible")

if __name__ == '__main__':
    unittest.main()