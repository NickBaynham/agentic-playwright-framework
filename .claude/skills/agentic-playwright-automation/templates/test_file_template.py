"""Template for a Playwright/PyTest test file.

Keep business assertions at the top level of the test function. Use
Playwright `expect` for UI assertions so auto-waiting applies. Do not
hard-code URLs, credentials, or environment-specific data; receive them
through fixtures.
"""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.smoke
def test_<behavior_name>(
    login_page,
    inventory_page,
    standard_user,
):
    """<One-line behavior summary.>

    Source:
        BDD Spec: specs/bdd/markdown/<feature>.md
        Feature:  specs/bdd/features/<feature>.feature
        Scenario: <Scenario name or Scenario ID>
    """
    # Arrange
    login_page.open()

    # Act
    login_page.login_as(standard_user)

    # Assert
    expect(inventory_page.products_heading).to_be_visible()
    expect(inventory_page.shopping_cart_link).to_be_visible()


@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.parametrize("user_fixture", ["standard_user", "problem_user"])
def test_<parameterized_behavior_name>(request, login_page, inventory_page, user_fixture):
    """Parameterized variant. Test data must come from fixtures, not literals."""
    user = request.getfixturevalue(user_fixture)

    login_page.open()
    login_page.login_as(user)

    expect(inventory_page.products_heading).to_be_visible()
