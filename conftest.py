import pytest


# Define a fixture for browser context arguments with session scope
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Custom fixture to set up browser context arguments.

    Args:
        browser_context_args (dict): Default browser context arguments.

    Returns:
        dict: Updated browser context arguments.
    """
    # Merge default arguments with additional ones
    return {
        **browser_context_args,
        "ignore_https_errors": True,  # Ignore HTTPS errors during testing
        "viewport": {
            "width": 1280,  # Set the viewport width to 1280 pixels
            "height": 780,  # Set the viewport height to 780 pixels
        }
    }
