def getLocator(page, method, locator):
    locators = {
        "text": lambda: page.get_by_text(locator),
        "role": lambda: page.get_by_role(locator),
        "placeholder": lambda: page.get_by_placeholder(locator),
        "label": lambda: page.get_by_label(locator),
        "test_id": lambda: page.get_by_test_id(locator),
        "title": lambda: page.get_by_title(locator),
        "alt_text": lambda: page.get_by_alt_text(locator),
        "locator": lambda: page.locator(locator),  # Regular CSS selector
        "xpath": lambda: page.locator(f"xpath={locator}"),  # XPath selector
    }

    if method in locators:
        return locators[method]()  # Call the function stored in the dictionary
    else:
        raise ValueError(f"Unsupported method: {method}")



