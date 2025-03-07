from test_actions.Scenarios import Scenarios
from test_playwright.test_base import BaseTest


class TestAddToCart(BaseTest):  # Fixed typo in class name

    def testClickOnItemBackPack(self):
        page = self.get_page()  # Get the Playwright page instance once
        Scenarios.login(self, page)  # Pass the existing page variable
        self.click_action.clickOnElementByLocator(page, '[data-test="add-to-cart-sauce-labs-backpack"]')
