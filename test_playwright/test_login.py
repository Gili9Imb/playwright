from test_actions.GetLocator import getLocator
from test_playwright.test_base import BaseTest


class TestLogin(BaseTest):

    def testLoginFoofooTest(self):
        page = self.get_page()
        self.open_url.runUrl(page, "https://www.saucedemo.com/")
        print("Page opened")
        getLocator(page,"locator", "//input[@id='user-name']").type("standard_user")
        getLocator(page,"locator", "//input[@id='password']").type("secret_sauce")
        getLocator(page,"locator", '[data-test=\"login-button\"]').click()
        getLocator(page, "text", "Sauce Labs Backpack").is_visible()
        self.assertEqual(page.url, "https://www.saucedemo.com/inventory.html", "Failed to login")
        self.assertTrue(page.locator("text=Sauce Labs Backpack").is_visible(), "Sauce Labs Backpack not visible")

    def testLoginWithWrongUserName(self):
        page = self.get_page()
        self.open_url.runUrl(page, "https://www.saucedemo.com/")
        print("Page opened")
        getLocator(page, "locator", "//input[@id='user-name']").type("standard_use")
        getLocator(page, "locator", "//input[@id='password']").type("secret_sauce")
        getLocator(page, "locator", '[data-test=\"login-button\"]').click()
        getLocator(page, "text", "Epic sadface: Username and password do not match any user in this service").is_visible()
