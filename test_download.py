def test_download(page):
    # Navigate to the Mozilla Firefox download page
    page.goto("https://www.mozilla.org/en-GB/firefox/")

    # Use the 'expect_download' context manager to capture download information
    with page.expect_download() as download_info:
        # Click on the download link for Firefox
        page.get_by_role("link", name="Download Firefox").click()

    # Access information about the downloaded file
    download = download_info.value

    # Print the path of the downloaded file
    print(download.path())

    # Save the downloaded file to a specified location
    download.save_as("C:/Users/admin/Desktop/Tools/playwright/section3/playwrightGuide/ffox.exe")
