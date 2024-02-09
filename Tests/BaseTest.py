from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3*1000)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    print("Page opened")
    page.fill("//input[@id='user-name']", "standard_user")
    page.fill("//input[@id='password']", "secret_sauce")
    page.get_by_text('Login').click()

    if page.wait_for_selector('text=Sauce Labs Backpack').is_visible():
        print("element found")

