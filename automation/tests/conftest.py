"""Root conftest for the SauceDemo automation suite.

Fixtures here are intentionally shallow. Page-object fixtures construct
their page from the pytest-playwright ``page`` fixture and the resolved
``Settings``. Test-data fixtures load YAML through
``framework.data.test_data_loader``.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

# Make `config.*` and `framework.*` importable when running pytest from the
# automation/ directory. This is the canonical entry point for `make test`.
AUTOMATION_ROOT = Path(__file__).resolve().parents[1]
if str(AUTOMATION_ROOT) not in sys.path:
    sys.path.insert(0, str(AUTOMATION_ROOT))

from playwright.sync_api import Page

from config.settings import Settings, load_settings
from framework.data.test_data_loader import (
    load_checkout_customers,
    load_products,
    load_users,
)
from framework.models.checkout_customer import CheckoutCustomer
from framework.models.product import Product
from framework.models.user import User
from framework.pages.cart_page import CartPage
from framework.pages.checkout_complete_page import CheckoutCompletePage
from framework.pages.checkout_information_page import CheckoutInformationPage
from framework.pages.checkout_overview_page import CheckoutOverviewPage
from framework.pages.inventory_page import InventoryPage
from framework.pages.login_page import LoginPage
from framework.utils.evidence import save_screenshot


@pytest.fixture(scope="session")
def settings() -> Settings:
    """Resolved environment configuration. Session-scoped because it is read-only."""
    return load_settings()


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: dict, settings: Settings) -> dict:
    """Bridge the resolved ``Settings.headless`` into pytest-playwright.

    Without this override, the ``headless`` value in ``config/environments.yaml``
    has no effect: pytest-playwright defaults to headless regardless. Browser
    name is selected by pytest-playwright's ``--browser`` CLI flag; the
    ``browser`` field in ``environments.yaml`` is currently advisory.
    """
    return {**browser_type_launch_args, "headless": settings.headless}


# --- Test data fixtures --------------------------------------------------


@pytest.fixture
def users(settings: Settings) -> dict[str, User]:
    """All users defined for the active environment."""
    return load_users(settings.test_data_path)


@pytest.fixture
def standard_user(users: dict[str, User]) -> User:
    """The canonical standard_user account used by smoke tests."""
    return users["standard_user"]


@pytest.fixture
def products(settings: Settings) -> dict[str, Product]:
    """All products defined for the active environment."""
    return load_products(settings.test_data_path)


@pytest.fixture
def backpack(products: dict[str, Product]) -> Product:
    """The Sauce Labs Backpack product used by the smoke suite."""
    return products["sauce_labs_backpack"]


@pytest.fixture
def checkout_customers(settings: Settings) -> dict[str, CheckoutCustomer]:
    """All canonical checkout customers for the active environment."""
    return load_checkout_customers(settings.test_data_path)


@pytest.fixture
def default_checkout_customer(
    checkout_customers: dict[str, CheckoutCustomer],
) -> CheckoutCustomer:
    """The canonical checkout customer used by the smoke suite."""
    return checkout_customers["default"]


# --- Page object fixtures ------------------------------------------------


@pytest.fixture
def login_page(page: Page, settings: Settings) -> LoginPage:
    return LoginPage(page, base_url=settings.base_url)


@pytest.fixture
def inventory_page(page: Page, settings: Settings) -> InventoryPage:
    return InventoryPage(page, base_url=settings.base_url)


@pytest.fixture
def cart_page(page: Page, settings: Settings) -> CartPage:
    return CartPage(page, base_url=settings.base_url)


@pytest.fixture
def checkout_information_page(
    page: Page, settings: Settings
) -> CheckoutInformationPage:
    return CheckoutInformationPage(page, base_url=settings.base_url)


@pytest.fixture
def checkout_overview_page(page: Page, settings: Settings) -> CheckoutOverviewPage:
    return CheckoutOverviewPage(page, base_url=settings.base_url)


@pytest.fixture
def checkout_complete_page(page: Page, settings: Settings) -> CheckoutCompletePage:
    return CheckoutCompletePage(page, base_url=settings.base_url)


# --- Failure-evidence hook -----------------------------------------------


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture a screenshot when a test that uses the ``page`` fixture fails.

    No-op for tests that do not consume ``page`` (such as the framework-smoke
    tests). The screenshot is written under ``reports/screenshots/`` via
    ``framework.utils.evidence.save_screenshot``.
    """
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return
    page = item.funcargs.get("page")
    if page is None:
        return
    save_screenshot(page, item.name)
