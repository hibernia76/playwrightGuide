# Import the necessary modules from Playwright
from playwright.sync_api import sync_playwright

# Uncomment the method below to debug the whole test
# Use the following commands to run in cmd or PowerShell with debugging
'''
To run in cmd:
$env:PWDEBUG=1; pytest test_debug.py -s

To run in PowerShell:
$env:PWDEBUG=1; pytest test_debug.py -s
'''

def test_microsoft(page):
    # Navigate to the Microsoft website and click on a locator
    page.goto("https://microsoft.com")
    page.locator("text=Shop Surface deals").click()

# Uncomment the method below to debug a section of a test
# Use the following command to run the test and pause for debugging
# Run this command in the terminal: python test_debug.py
'''
To debug a section of a test, use the page.pause() method
'''
with sync_playwright() as p:
    # Launch a Chromium browser in non-headless mode with a slight delay for debugging
    browser = p.chromium.launch(headless=False, slow_mo=500)
    # Create a new page
    page = browser.new_page()
    # Navigate to the Playwright website
    page.goto("http://playwright.dev")
    # Print the title of the page
    print(page.title())
    # Pause the execution for debugging
    page.pause()
    # Navigate to the Amazon UK website
    page.goto("https://amazon.co.uk")
    # Close the browser
    browser.close()
