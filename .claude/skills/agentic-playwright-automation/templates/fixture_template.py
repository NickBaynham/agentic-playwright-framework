"""Template for PyTest fixtures.

Fixtures are named for the resource they provide. Default scope is
`function`; broaden only for expensive, safe-to-share resources. Do not
embed secrets; read from environment variables.
"""

from __future__ import annotations

import pytest
from playwright.sync_api import Page

from framework.data.test_data_loader import load_users
from framework.models.user import User
from framework.pages.login_page import LoginPage
from framework.pages.inventory_page import InventoryPage
from config.settings import Settings, load_settings


@pytest.fixture(scope="session")
def settings() -> Settings:
    return load_settings()


@pytest.fixture
def users(settings: Settings) -> dict[str, User]:
    return load_users(settings.test_data_path)


@pytest.fixture
def standard_user(users: dict[str, User]) -> User:
    return users["standard_user"]


@pytest.fixture
def login_page(page: Page, settings: Settings) -> LoginPage:
    return LoginPage(page, base_url=settings.base_url)


@pytest.fixture
def inventory_page(page: Page, settings: Settings) -> InventoryPage:
    return InventoryPage(page, base_url=settings.base_url)
