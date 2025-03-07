
class ClickAction:

    def clickOnElementByText(self, page, text):
        page.get_by_text(text).click()

    def clickOnElementByLocator(self, page, locator):
        page.locator(locator).click()