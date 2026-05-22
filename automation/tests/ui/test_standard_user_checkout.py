"""Standard User Checkout — smoke automation.

Implements the High-priority, ``@automatable`` scenarios from
``specs/bdd/features/standard_user_checkout.feature``.

Scenarios skipped in this pass (tagged ``@needs-clarification``):
- TC-07 Cart is empty after order completion
- TC-08 Checkout information form rejects missing required fields

See ``automation/reports/automation/standard_user_checkout_suite_implementation_report.md``
for the Locator Decision Log, locator risks, and traceability summary.
"""

from __future__ import annotations

import re
from decimal import Decimal

import pytest
from playwright.sync_api import expect

from framework.models.checkout_customer import CheckoutCustomer
from framework.models.product import Product
from framework.models.user import User
from framework.pages.cart_page import CartPage
from framework.pages.checkout_complete_page import CheckoutCompletePage
from framework.pages.checkout_information_page import CheckoutInformationPage
from framework.pages.checkout_overview_page import CheckoutOverviewPage
from framework.pages.inventory_page import InventoryPage
from framework.pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.login
def test_standard_user_logs_in_successfully(
    login_page: LoginPage,
    inventory_page: InventoryPage,
    standard_user: User,
) -> None:
    """TC-01: A standard user signs in and lands on the products page.

    Source:
        BDD Spec: specs/bdd/markdown/standard_user_checkout.md
        Feature:  specs/bdd/features/standard_user_checkout.feature
        Scenario: TC-01 — Standard user logs in successfully
    """
    # Arrange
    login_page.open()

    # Act
    login_page.login_as(standard_user)

    # Assert
    expect(login_page.page).to_have_url(re.compile(r".*/inventory\.html$"))
    expect(inventory_page.products_listing).to_be_visible()


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.cart
def test_adding_product_updates_cart_badge_and_toggles_button(
    login_page: LoginPage,
    inventory_page: InventoryPage,
    standard_user: User,
    backpack: Product,
) -> None:
    """TC-02: Adding a product places it in the cart.

    Verifies both observable consequences of the single add-to-cart action:
    the cart badge increments to 1 and the per-product action button toggles
    from "Add to cart" to "Remove".

    Source:
        BDD Spec: specs/bdd/markdown/standard_user_checkout.md
        Feature:  specs/bdd/features/standard_user_checkout.feature
        Scenario: TC-02 — Adding a product places it in the cart
    """
    # Arrange
    login_page.open()
    login_page.login_as(standard_user)

    # Act
    inventory_page.add_to_cart(backpack)

    # Assert
    expect(inventory_page.cart_badge).to_have_text("1")
    expect(inventory_page.remove_button(backpack)).to_be_visible()
    expect(inventory_page.add_to_cart_button(backpack)).to_have_count(0)


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.cart
def test_cart_lists_added_item_with_quantity_and_price(
    login_page: LoginPage,
    inventory_page: InventoryPage,
    cart_page: CartPage,
    standard_user: User,
    backpack: Product,
) -> None:
    """TC-03: The cart shows the added item with the correct name, quantity, and price.

    Source:
        BDD Spec: specs/bdd/markdown/standard_user_checkout.md
        Feature:  specs/bdd/features/standard_user_checkout.feature
        Scenario: TC-03 — Cart page lists the added item with the correct name, quantity, and price
    """
    # Arrange
    login_page.open()
    login_page.login_as(standard_user)
    inventory_page.add_to_cart(backpack)

    # Act
    inventory_page.open_cart()

    # Assert
    expect(cart_page.page).to_have_url(re.compile(r".*/cart\.html$"))
    expect(cart_page.line_item(backpack)).to_have_count(1)
    expect(cart_page.line_item_quantity(backpack)).to_have_text("1")
    expect(cart_page.line_item_price(backpack)).to_have_text(f"${backpack.price}")
    expect(cart_page.checkout_button).to_be_visible()


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.checkout
def test_checkout_information_advances_to_overview_with_valid_input(
    login_page: LoginPage,
    inventory_page: InventoryPage,
    cart_page: CartPage,
    checkout_information_page: CheckoutInformationPage,
    standard_user: User,
    backpack: Product,
    default_checkout_customer: CheckoutCustomer,
) -> None:
    """TC-04: Submitting valid checkout information advances to the overview page.

    Source:
        BDD Spec: specs/bdd/markdown/standard_user_checkout.md
        Feature:  specs/bdd/features/standard_user_checkout.feature
        Scenario: TC-04 — Checkout information form advances to the overview with valid input
    """
    # Arrange
    login_page.open()
    login_page.login_as(standard_user)
    inventory_page.add_to_cart(backpack)
    inventory_page.open_cart()
    cart_page.proceed_to_checkout()

    # Act
    checkout_information_page.fill_customer(default_checkout_customer)
    checkout_information_page.continue_to_overview()

    # Assert
    expect(checkout_information_page.page).to_have_url(
        re.compile(r".*/checkout-step-two\.html$")
    )


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.checkout
def test_overview_totals_satisfy_item_total_plus_tax_equals_total(
    login_page: LoginPage,
    inventory_page: InventoryPage,
    cart_page: CartPage,
    checkout_information_page: CheckoutInformationPage,
    checkout_overview_page: CheckoutOverviewPage,
    standard_user: User,
    backpack: Product,
    default_checkout_customer: CheckoutCustomer,
) -> None:
    """TC-05: The displayed Total equals Item total plus Tax.

    The tax rate is not a documented business rule, so the assertion is on
    the relational identity rather than an exact tax value.

    Source:
        BDD Spec: specs/bdd/markdown/standard_user_checkout.md
        Feature:  specs/bdd/features/standard_user_checkout.feature
        Scenario: TC-05 — Overview page totals satisfy Item total + Tax = Total
    """
    # Arrange
    login_page.open()
    login_page.login_as(standard_user)
    inventory_page.add_to_cart(backpack)
    inventory_page.open_cart()
    cart_page.proceed_to_checkout()
    checkout_information_page.fill_customer(default_checkout_customer)
    checkout_information_page.continue_to_overview()

    # Act
    expect(checkout_overview_page.item_total_label).to_be_visible()
    expect(checkout_overview_page.tax_label).to_be_visible()
    expect(checkout_overview_page.total_label).to_be_visible()
    item_total = checkout_overview_page.read_item_total()
    tax = checkout_overview_page.read_tax()
    total = checkout_overview_page.read_total()

    # Assert
    assert item_total == backpack.price
    assert total == item_total + tax
    assert tax >= Decimal("0")


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.checkout
def test_finishing_order_shows_confirmation_page(
    login_page: LoginPage,
    inventory_page: InventoryPage,
    cart_page: CartPage,
    checkout_information_page: CheckoutInformationPage,
    checkout_overview_page: CheckoutOverviewPage,
    checkout_complete_page: CheckoutCompletePage,
    standard_user: User,
    backpack: Product,
    default_checkout_customer: CheckoutCustomer,
) -> None:
    """TC-06: Finishing the order shows the confirmation page with the thank-you heading.

    Source:
        BDD Spec: specs/bdd/markdown/standard_user_checkout.md
        Feature:  specs/bdd/features/standard_user_checkout.feature
        Scenario: TC-06 — Finishing the order shows the order confirmation page
    """
    # Arrange
    login_page.open()
    login_page.login_as(standard_user)
    inventory_page.add_to_cart(backpack)
    inventory_page.open_cart()
    cart_page.proceed_to_checkout()
    checkout_information_page.fill_customer(default_checkout_customer)
    checkout_information_page.continue_to_overview()

    # Act
    checkout_overview_page.finish_order()

    # Assert
    expect(checkout_complete_page.page).to_have_url(
        re.compile(r".*/checkout-complete\.html$")
    )
    expect(checkout_complete_page.thank_you_heading).to_be_visible()
