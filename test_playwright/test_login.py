from test_playwright.test_base import BaseTest


class TestLogin(BaseTest):

    def testLoginFooFooTest(self):
        page = self.get_page()
        self.open_url.runUrl(page, "https://www.saucedemo.com/")
        print("Page opened")
        self.fill_action.fillElement(page, "//input[@id='user-name']", "standard_user")
        self.fill_action.fillElement(page, "//input[@id='password']", "secret_sauce")
        self.click_action.clickOnElementByLocator(page, '[data-test=\"login-button\"]')
        self.wait_action.waitforElement(page, "text", "Sauce Labs Backpack")
        self.assertEqual(page.url, "https://www.saucedemo.com/inventory.html", "Failed to login")
        self.assertTrue(page.locator("text=Sauce Labs Backpack").is_visible(), "Sauce Labs Backpack not visible")

    def testLoginWrongEmail(self):
        page = self.get_page()
        self.open_url.runUrl(page, "https://www.saucedemo.com/")
        print("Page opened")
        self.fill_action.fillElement(page, "//input[@id='user-name']", "standard")
        self.fill_action.fillElement(page, "//input[@id='password']", "secret_sauce")
        self.click_action.clickOnElementByLocator(page, '[data-test=\"login-button\"]')
        self.wait_action.waitforElement(page, "text", "Epic sadface: Username and password do not match any user in this service")
