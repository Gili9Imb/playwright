from pytest_playwright.pytest_playwright import page


class OpenUrl:

    def runUrl(self,page,text):
        page.goto(text)
