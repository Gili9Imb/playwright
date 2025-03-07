import unittest

from pytest_playwright.pytest_playwright import page
from playwright.sync_api import sync_playwright
from test_actions.ClickAction import ClickAction
from test_actions.FillAction import FillAction
from test_actions.OpenUrl import OpenUrl
from test_actions.WaitAction import WaitAction


class Scenarios(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.wait_action = None
        self.click_action = None
        self.fill_action = None
        self.open_url = None

    def login(self, page):
        self.get_page()
        self.open_url.runUrl(page, "https://www.saucedemo.com/")
        print("Page opened")
        self.fill_action.fillElement(page, "//input[@id='user-name']", "standard_user")
        self.fill_action.fillElement(page, "//input[@id='password']", "secret_sauce")
        self.click_action.clickOnElementByLocator(page, '[data-test=\"login-button\"]')
        self.wait_action.waitforElement(page, "text", "Sauce Labs Backpack")