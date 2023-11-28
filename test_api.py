# Import necessary modules and types
from typing import Generator
import pytest
from playwright.sync_api import Playwright, Page, APIRequestContext, expect

# Initialise GitHub API credentials
GITHUB_API_TOKEN = "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"
assert GITHUB_API_TOKEN, "GITHUB_API_TOKEN is not set"

# GitHub username
GITHUB_USER = "hibernia76"
assert GITHUB_USER, "GITHUB_USER is not set"

# Name of the GitHub repository to be used for testing
GITHUB_REPO = "Test_API"


# Fixture for creating and disposing the API request context for each test session
@pytest.fixture(scope='session')
def api_request_context(
        playwright: Playwright
) -> Generator[APIRequestContext, None, None]:
    # Define headers for GitHub API requests
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {GITHUB_API_TOKEN}",
    }

    # Create a new context for API requests using Playwright
    request_context = playwright.request.new_context(
        base_url="https://api.github.com", extra_http_headers=headers
    )

    # Yield the API request context for use in tests
    yield request_context

    # Dispose of the context after the tests are done
    request_context.dispose()


# Fixture for creating and deleting a test repository for the entire session
@pytest.fixture(scope="session", autouse=True)
def create_test_repo(
        api_request_context: APIRequestContext,
) -> Generator[None, None, None]:
    # Create a new repository on GitHub for testing
    new_repo = api_request_context.post("/user/repos", data={"name": GITHUB_REPO})

    # Print details of the create repository response
    print("Create Repo Response:")
    print(f"  Status Code: {new_repo.status}")
    print(f"  Response Body: {new_repo.text()}")

    # Assert that the repository creation was successful
    assert new_repo.ok

    # Yield control to the tests
    yield

    # Delete the test repository after the tests are completed
    delete_repo = api_request_context.delete(f"/repos/{GITHUB_USER}/{GITHUB_REPO}")

    # Print details of the delete repository response
    print(f"Test Result: PASSED")
    print("Delete Repo Response:")
    print(f"  Status Code: {delete_repo.status}")
    print(f"  Response Body: {delete_repo.text()}")

    # Assert that the repository deletion was successful
    assert delete_repo.ok


# Test function for creating a bug report
def test_bug_report(api_request_context: APIRequestContext) -> None:
    # Define data for creating a bug report issue
    data = {
        "title": "[Bug] report 1",
        "body": "Bug description",
    }

    # Create a new issue for the bug report
    new_issue = api_request_context.post(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues", data=data
    )

    # Assert that the issue creation was successful
    assert new_issue.ok

    # Retrieve and assert details of the created issue
    issues = api_request_context.get(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues")
    assert issues.ok
    issues_response = issues.json()
    issue = list(
        filter(lambda issue: issue["title"] == "[Bug] report 1",
               issues_response)
    )[0]
    assert issue
    assert issue["body"] == "Bug description"


# Test function for creating a feature request
def test_feature(api_request_context: APIRequestContext) -> None:
    # Define data for creating a feature request issue
    data = {
        "title": "[Feature] request 1",
        "body": "Feature description",
    }

    # Create a new issue for the feature request
    new_issue = api_request_context.post(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues", data=data
    )

    # Assert that the issue creation was successful
    assert new_issue.ok

    # Retrieve and assert details of the created issue
    issues = api_request_context.get(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues")
    assert issues.ok
    issues_response = issues.json()
    issue = list(
        filter(lambda issue: issue["title"] == "[Feature] request 1",
               issues_response)
    )[0]
    assert issue
    assert issue["body"] == "Feature description"

# This  code structure can be adapted to test APIs on other web services or webpages. The key components that you
# might need to modify are the URL endpoints, request payloads, and response validations based on the specifics of
# the API you are testing.
#
# Here are the parts you would likely need to adjust:
#
#     API Endpoint URLs: Replace the GitHub-specific URLs with the URLs of the API you are testing. For example, update the URLs used in the post, get, and delete requests.
#
#     Request Payloads: Modify the data structures and content used in the post requests (new_issue creation) to match the expected payload format for the API you are testing.
#
#     Response Validations: Adjust the response validations based on the expected structure and content of the responses from the API you are testing. The assertions in the test functions (test_bug_report and test_feature) should be adapted accordingly.
#
#     Authentication: If the API you are testing requires authentication, you might need to adjust the authentication headers or mechanisms.
#
# Below is a simplified example with comments indicating where you might make changes:
#
#
#     from typing import Generator
#     import pytest
#     from playwright.sync_api import Playwright, APIRequestContext
#
#     # Replace with your API endpoint and authentication details
#     API_BASE_URL = "https://api.example.com"
#     API_TOKEN = "your_api_token"
#
#
#     # ...
#
#     @pytest.fixture(scope='session')
#     def api_request_context(
#             playwright: Playwright
#     ) -> Generator[APIRequestContext, None, None]:
#         headers = {
#             "Authorization": f"Bearer {API_TOKEN}",
#             # Add other headers as needed for your API
#         }
#         request_context = playwright.request.new_context(
#             base_url=API_BASE_URL, extra_http_headers=headers
#         )
#         yield request_context
#         request_context.dispose()
#
#
#     # Replace with your API-specific endpoint and payload
#     def test_api_function(api_request_context: APIRequestContext) -> None:
#         data = {
#             "key": "value",
#             # Add other fields based on your API requirements
#         }
#         response = api_request_context.post(
#             "/your/api/endpoint", data=data
#         )
#         assert response.ok
#         # Add assertions based on the expected response structure of your API
#
#
# Keep in mind that the specifics depend on the API you are testing. You should refer to the API documentation to
# understand the expected endpoints, request payloads, and response structures.
