
class ClickAction:

    def clickOnElementByText(self,page, locator):
        page.get_by_text(locator).click()
