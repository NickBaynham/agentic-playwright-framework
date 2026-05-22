"""LoginPage — saucedemo landing page.

Locator decisions and source traceability live in:
``automation/reports/automation/standard_user_checkout_suite_implementation_report.md``.
"""

from __future__ import annotations

from playwright.sync_api import Locator

from framework.models.user import User
from framework.pages.base_page import BasePage


class LoginPage(BasePage):
    URL_PATH = "/"

    @property
    def username_input(self) -> Locator:
        return self.page.get_by_placeholder("Username")

    @property
    def password_input(self) -> Locator:
        return self.page.get_by_placeholder("Password")

    @property
    def login_button(self) -> Locator:
        return self.page.get_by_role("button", name="Login")

    @property
    def error_banner(self) -> Locator:
        # Conditional element — only present after a failed login.
        return self.page.locator("[data-test='error']")

    def login_as(self, user: User) -> None:
        self.username_input.fill(user.username)
        self.password_input.fill(user.password)
        self.login_button.click()
