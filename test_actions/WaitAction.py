class WaitAction:

    def waitforElement(self, page, method, locator):
        # 'text=Sauce Labs Backpack'
        if page.wait_for_selector(method + '=' + locator).is_visible():
            print("Found an element")
