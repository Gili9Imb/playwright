from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3*1000)
    page = browser.new_page()
    page.goto("http:www.google.com")
    print("Open google with chrome")
    page.fill("//input[@id='input']", "something")
