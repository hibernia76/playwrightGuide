from playwright.sync_api import sync_playwright

# Using Playwright to create browser contexts and navigate pages

# Start Playwright and obtain a Playwright object
with sync_playwright() as p:
    # Define a device configuration for iPhone 13 Pro
    iphone_13 = p.devices["iPhone 13 Pro"]

    # Launch a WebKit browser with specific settings
    browser = p.webkit.launch(headless=False, slow_mo=5000)

    # Create a browser context with iPhone 13 Pro settings
    context1 = browser.new_context(
        **iphone_13,
        locale='ie-EN',  # Set locale to Ireland - English
        geolocation={'longitude': 12.492507, 'latitude': 41.889938},  # Set geolocation to a specific location
        permissions=['geolocation']  # Grant geolocation permission
    )

    # Create another browser context without specific settings
    context2 = browser.new_context()

    # Create pages within the respective contexts
    page1 = context1.new_page()
    page11 = context1.new_page()
    page2 = context2.new_page()

    # Navigate the pages to different websites
    page1.goto("https://youtube.com")
    page11.goto("https://google.ie")
    page2.goto("https://amazon.co.uk")

    # Close the entire browser
    browser.close()

    '''The provided code demonstrates the use of Playwright to create multiple browser contexts with specific 
    settings, and it's a simplified example for educational purposes. There are scenarios where this kind of code 
    might be useful:

    Cross-Browser and Cross-Device Testing: By creating browser contexts with different devices (like iPhone 13 Pro 
    in this case), developers and testers can ensure that web applications are responsive and work well across 
    various devices and browsers.

    Localization and Internationalization Testing: Setting different locales allows testing the application's 
    behavior with respect to different languages and regions. It helps ensure that the user interface and content are 
    correctly displayed for users in different locales.

    Geolocation Testing: The code sets specific geolocation coordinates for one of the contexts. This is useful for 
    testing location-based features or verifying that the application behaves correctly when accessed from different 
    geographical locations.

    Permissions Testing: The code grants geolocation permission explicitly. This can be useful when testing features 
    that rely on permissions, ensuring that the application behaves as expected when granted or denied specific 
    permissions.

    Parallel Testing: Creating multiple browser contexts allows for parallel testing of different scenarios. Each 
    context operates independently, making it easier to run tests concurrently.

    Headless and Non-Headless Modes: The code demonstrates launching the browser in non-headless mode (
    headless=False). This can be helpful during development and debugging to observe the browser's behavior.

    While the specific settings and configurations in this code may not be necessary for every test scenario, 
    they illustrate how Playwright can be used to handle different aspects of browser behavior, especially in scenarios 
    involving diverse user environments and scenarios. Real-world testing scenarios might involve a combination of these 
    settings based on the application's requirements and the desired test coverage.

    '''

