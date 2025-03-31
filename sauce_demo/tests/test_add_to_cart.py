# sauce_demo/tests/test_add_to_cart.py
from Infra.test_actions.locators_methods import getLocator
from sauce_demo.tests.scenarios import Scenarios
from Infra.test_base import BaseTest

class TestAddToCart(BaseTest):

    def setUp(self):
        super().setUp()
        self.page = self.get_page()
        Scenarios.login(self, self.page)

    def testClickOnItemBackPack(self):
        getLocator(self.page, "locator", ".btn_inventory").first.click()

        badge = getLocator(self.page, "locator", '[data-test="shopping-cart-badge"]')
        assert badge.is_visible(), "Cart badge is not visible"
        assert badge.inner_text() == "1", "Cart badge does not contain the expected number"

    def testAddAllItemsToCart(self):
        global button_text
        item_count = clickOnItemsInList(self.page)

        badge = getLocator(self.page, "locator", '[data-test="shopping-cart-badge"]')
        assert badge.is_visible(), "Cart badge is not visible"
        assert int(badge.inner_text()) == item_count, f"Expected {item_count} items in the cart badge"

        buttons = getLocator(self.page, "locator", ".btn_inventory").element_handles()
        button_texts = []

        for index, button in enumerate(buttons):
            button_text_after = button.inner_text()
            button_texts.append(button_text_after)
        assert button_texts == ["Remove", "Remove", "Remove", "Remove", "Remove", "Remove"], f"The buttons texts are {button_texts}"

    def testAddAllItemsToCartAndRemove(self):
        item_count = clickOnItemsInList(self.page)

        badge = getLocator(self.page, "locator", '[data-test="shopping-cart-badge"]')
        assert badge.is_visible(), "Cart badge is not visible after adding items"
        assert int(badge.inner_text()) == item_count, f"Expected {item_count} items in the cart badge"

        clickOnItemsInList(self.page)
        assert not badge.is_visible(), "Cart badge is still visible after removing items"
        buttons = getLocator(self.page, "locator", ".btn_inventory").element_handles()

        button_texts = []

        for index, button in enumerate(buttons):
            button_text_after = button.inner_text()
            button_texts.append(button_text_after)
        assert button_texts == ["Add to cart", "Add to cart", "Add to cart", "Add to cart", "Add to cart", "Add to cart"], f"The buttons texts are {button_texts}"


def clickOnItemsInList(page):
    buttons = page.locator(".btn_inventory").element_handles()

    for button in buttons:
        button.click()

    return len(buttons)