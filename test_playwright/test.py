from test_playwright.test_base import BaseTest


class Test(BaseTest):

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