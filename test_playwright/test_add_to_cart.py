from test_actions.Scenarios import Scenarios
from test_playwright.test_base import BaseTest


class TestAddToCart(BaseTest):

    def testClickOnItemBackPack(self):
        page = self.get_page()
        Scenarios.login(self, page)
        page.locator(".btn_inventory").first.click()
        badge = page.locator('[data-test="shopping-cart-badge"]')
        assert badge.is_visible(), "Cart badge is not visible"
        assert badge.inner_text() == "1", "Cart badge does not contain the expected number"

    def testAddAllItemsToCart(self):
        page = self.get_page()
        Scenarios.login(self, page)
        buttons = page.locator(".btn_inventory").element_handles()
        for button in buttons:
            button.click()

        badge = page.locator('[data-test="shopping-cart-badge"]')
        button_count = len(buttons)
        assert badge.is_visible(), "Cart badge is not visible"
        assert int(
            badge.inner_text()) == button_count, f"Cart badge does not contain the expected number {button_count}"

    def testAddAllItemsToCartAndRemove(self):
        page = self.get_page()
        Scenarios.login(self, page)

        item_count = clickOnItemsInList(page)

        badge = page.locator('[data-test="shopping-cart-badge"]')
        assert badge.is_visible(), "Cart badge is not visible after adding items"
        assert int(badge.inner_text()) == item_count, f"Expected {item_count} items in the cart badge"

        clickOnItemsInList(page)
        assert not badge.is_visible(), "Cart badge is still visible after removing items"


def clickOnItemsInList(page):
    buttons = page.locator(".btn_inventory").element_handles()

    for button in buttons:
        button.click()

    return len(buttons)
