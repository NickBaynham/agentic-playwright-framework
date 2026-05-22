"""SauceDemo login page object example."""

from playwright.sync_api import Page

from framework.models.user import User


class LoginPage:
    URL_PATH = "/"

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def open(self) -> None:
        self.page.goto(f"{self.base_url}{self.URL_PATH}")

    @property
    def username_field(self):
        return self.page.get_by_placeholder("Username")

    @property
    def password_field(self):
        return self.page.get_by_placeholder("Password")

    @property
    def login_button(self):
        return self.page.get_by_role("button", name="Login")

    @property
    def error_banner(self):
        return self.page.get_by_test_id("error")

    def login_as(self, user: User) -> None:
        self.username_field.fill(user.username)
        self.password_field.fill(user.password)
        self.login_button.click()
