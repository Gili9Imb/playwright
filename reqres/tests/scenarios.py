import unittest

from pytest_playwright.pytest_playwright import page
from Infra.test_actions.locators_methods import getLocator

class Scenarios(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.open_url = None

    def openPage(self, page):
        self.get_page()
        self.open_url.runUrl(page, "https://reqres.in/")
        print("Page opened")