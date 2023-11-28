from playwright.sync_api import Page, expect


# Test to check if the "Search settings" text is present after interacting with the page
def test_submitted(page: Page) -> None:
    # Navigate to Google
    page.goto("https://www.google.com")

    # Perform actions to dismiss a hypothetical "Reject all" button and access settings
    page.get_by_role("button", name="Reject all").click()
    page.locator("div[role=\"button\"]:has-text(\"Settings\")").click()

    # Assert that the "Search settings" text is present on the page
    expect(page.locator("text=Search settings")).to_have_text("Search settings")


# Test to check if the "Business" text is visible after interacting with the page
def test_visible(page: Page) -> None:
    # Navigate to Google
    page.goto("https://google.com")

    # Perform actions to dismiss a hypothetical "Reject all" button and access settings
    page.get_by_role("button", name="Reject all").click()
    page.locator("div[role=\"button\"]:has-text(\"Settings\")").click()

    # Assert that the "Business" text is visible on the page
    expect(page.locator("text=Business")).to_be_visible()


# pytest test_assertions.py --browser firefox --headed --slowmo 4000 -v

    """
    Commented Options for Expectations:

    The following lines are commented options for various expectations you can use in Playwright tests.
    You can uncomment and customize them based on your testing needs.

    For example:
    - Uncomment `expect(locator).to_be_visible(**kwargs)` to check if an element is visible.
    - Uncomment `expect(locator).to_contain_text(expected, **kwargs)` to check if an element contains specific text.

    The options cover various expectations related to element properties, attributes, states, and page-related expectations.
    You can choose and use the ones that fit your specific test scenarios.

    expect(locator).not_to_be_checked(**kwargs)
    expect(locator).not_to_be_disabled(**kwargs)
    expect(locator).not_to_be_editable(**kwargs)
    expect(locator).not_to_be_empty(**kwargs)
    expect(locator).not_to_be_enabled(**kwargs)
    expect(locator).not_to_be_focused(**kwargs)
    expect(locator).not_to_be_hidden(**kwargs)
    expect(locator).not_to_be_visible(**kwargs)
    expect(locator).not_to_contain_text(expected, **kwargs)
    expect(locator).not_to_have_attribute(name, value, **kwargs)
    expect(locator).not_to_have_class(expected, **kwargs)
    expect(locator).not_to_have_count(count, **kwargs)
    expect(locator).not_to_have_css(name, value, **kwargs)
    expect(locator).not_to_have_id(id, **kwargs)
    expect(locator).not_to_have_js_property(name, value, **kwargs)
    expect(locator).not_to_have_text(expected, **kwargs)
    expect(locator).not_to_have_value(value, **kwargs)
    expect(locator).not_to_have_values(values, **kwargs)
    expect(locator).to_be_checked(**kwargs)
    expect(locator).to_be_disabled(**kwargs)
    expect(locator).to_be_editable(**kwargs)
    expect(locator).to_be_empty(**kwargs)
    expect(locator).to_be_enabled(**kwargs)
    expect(locator).to_be_focused(**kwargs)
    expect(locator).to_be_hidden(**kwargs)
    expect(locator).to_be_visible(**kwargs)
    expect(locator).to_contain_text(expected, **kwargs)
    expect(locator).to_have_attribute(name, value, **kwargs)
    expect(locator).to_have_class(expected, **kwargs)
    expect(locator).to_have_count(count, **kwargs)
    expect(locator).to_have_css(name, value, **kwargs)
    expect(locator).to_have_id(id, **kwargs)
    expect(locator).to_have_js_property(name, value, **kwargs)
    expect(locator).to_have_text(expected, **kwargs)
    expect(locator).to_have_value(value, **kwargs)
    expect(locator).to_have_values(values, **kwargs)
    expect(page).not_to_have_title(title_or_reg_exp, **kwargs)
    expect(page).not_to_have_url(url_or_reg_exp, **kwargs)
    expect(page).to_have_title(title_or_reg_exp, **kwargs)
    expect(page).to_have_url(url_or_reg_exp, **kwargs)
    expect(api_response).not_to_be_ok()
    expect(api_response).to_be_ok()

    """
