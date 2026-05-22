"""SauceDemo login example test.

Source:
    BDD Spec: specs/bdd/markdown/saucedemo_login.md
    Feature:  specs/bdd/features/saucedemo_login.feature
    Scenario: Standard user logs in successfully

Demonstrates preferred patterns:
    - Top-level expect assertions.
    - Page objects exposing locators as properties.
    - User data injected through a fixture, not literal strings.
    - PyTest markers for `ui` and `smoke`.
"""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.smoke
def test_standard_user_logs_in_successfully(
    login_page,
    inventory_page,
    standard_user,
):
    """Standard user reaches the inventory page after a successful login."""
    # Arrange
    login_page.open()

    # Act
    login_page.login_as(standard_user)

    # Assert
    expect(inventory_page.products_heading).to_be_visible()
    expect(inventory_page.shopping_cart_link).to_be_visible()
    expect(login_page.page).to_have_url(lambda url: url.endswith("/inventory.html"))
