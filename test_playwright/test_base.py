import unittest
from playwright.sync_api import sync_playwright
from test_actions.ClickAction import ClickAction
from test_actions.FillAction import FillAction
from test_actions.OpenUrl import OpenUrl
from test_actions.WaitAction import WaitAction

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.fill_action = FillAction()
        self.click_action = ClickAction()
        self.wait_action = WaitAction()
        self.open_url = OpenUrl()
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False, slow_mo=1200)
        self.context = self.browser.new_context()

    def tearDown(self):
        self.context.close()
        self.browser.close()
        self.playwright.stop()

    def get_page(self):
        return self.context.new_page()