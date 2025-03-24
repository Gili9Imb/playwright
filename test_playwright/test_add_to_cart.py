from test_actions.GetLocator import getLocator
from test_actions.Scenarios import Scenarios
from test_playwright.test_base import BaseTest

class TestAddToCart(BaseTest):

    def testClickOnItemBackPack(self):
        page = self.get_page()
        Scenarios.login(self, page)
        getLocator(page, "locator", ".btn_inventory").first.click()

        badge = getLocator(page, "locator", '[data-test="shopping-cart-badge"]')
        assert badge.is_visible(), "Cart badge is not visible"
        assert badge.inner_text() == "1", "Cart badge does not contain the expected number"

    def testAddAllItemsToCart(self):
        global button_text
        page = self.get_page()
        Scenarios.login(self, page)
        item_count = clickOnItemsInList(page)

        badge = getLocator(page, "locator", '[data-test="shopping-cart-badge"]')
        assert badge.is_visible(), "Cart badge is not visible"
        assert int(badge.inner_text()) == item_count, f"Expected {item_count} items in the cart badge"

        buttons = getLocator(page,"locator",".btn_inventory").element_handles()
        button_texts = []

        for index, button in enumerate(buttons):
            button_text_after = button.inner_text()
            button_texts.append(button_text_after)
        assert button_texts == ["Remove", "Remove", "Remove", "Remove", "Remove", "Remove"],f"The buttons texts are {button_texts}"

    def testAddAllItemsToCartAndRemove(self):
        page = self.get_page()
        Scenarios.login(self, page)

        item_count = clickOnItemsInList(page)

        badge = getLocator(page, "locator", '[data-test="shopping-cart-badge"]')
        assert badge.is_visible(), "Cart badge is not visible after adding items"
        assert int(badge.inner_text()) == item_count, f"Expected {item_count} items in the cart badge"

        clickOnItemsInList(page)
        assert not badge.is_visible(), "Cart badge is still visible after removing items"
        buttons = getLocator(page,"locator",".btn_inventory").element_handles()

        button_texts = []

        for index, button in enumerate(buttons):
            button_text_after = button.inner_text()
            button_texts.append(button_text_after)
        assert button_texts == ["Add to cart", "Add to cart", "Add to cart", "Add to cart", "Add to cart", "Add to cart"],f"The buttons texts are {button_texts}"


def clickOnItemsInList(page):
    buttons = page.locator(".btn_inventory").element_handles()

    for button in buttons:
        button.click()

    return len(buttons)
