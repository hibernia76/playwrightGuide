def test_auth(page):
    # Navigate to the GitHub login page
    page.goto("https://github.com/login")

    # Click on the login input field and fill in the username
    page.locator("input[name=\"login\"]").click()
    page.locator("input[name=\"login\"]").fill("hibernia76")

    # Click on the password input field and fill in the password
    page.locator("input[name=\"password\"]").click()
    page.locator("input[name=\"password\"]").fill("G1tHub$1_Abc_123$")

    # Click on the "Sign in" button
    page.locator("input:has-text(\"Sign in\")").click()

    # Wait for the page to navigate to the GitHub home page
    page.wait_for_url("https://github.com/")
