import unittest

from pytest_playwright.pytest_playwright import page
from Infra.test_actions.GetLocator import getLocator

class Scenarios(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.open_url = None

    def login(self, page):
        self.get_page()
        self.open_url.runUrl(page, "https://www.saucedemo.com/")
        print("Page opened")
        getLocator(page, "locator", "//input[@id='user-name']").type("standard_user")
        getLocator(page, "locator", "//input[@id='password']").type("secret_sauce")
        getLocator(page, "text", 'Login').click()
