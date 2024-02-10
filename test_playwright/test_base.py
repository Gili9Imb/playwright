# import pytest
# from playwright.sync_api import sync_playwright
#
#
# class BaseTest:
#
#     def __init__(self):
#         self.playwright = None
#         self.browser = None
#         self.page = None
#
#     def setup(self):
#         self.playwright = sync_playwright().start()
#         self.browser = self.playwright.chromium.launch(headless=False, slow_mo=3*1000)
#         self.page = self.browser.new_page()
#
#
#
#
