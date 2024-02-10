from pytest_playwright.pytest_playwright import page


class FillAction:

    def fillElement(self, page, locator, text):
        page.fill(locator, text)
