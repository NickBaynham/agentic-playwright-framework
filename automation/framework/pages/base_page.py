"""Base class for page objects.

Subclasses set ``URL_PATH`` and expose locators as ``@property``. They must
not own business assertions. Environment-specific values (URLs, credentials,
test data) are passed in by the test layer via fixtures.
"""

from __future__ import annotations

from playwright.sync_api import Page


class BasePage:
    URL_PATH: str = "/"

    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url

    @property
    def url(self) -> str:
        return f"{self.base_url}{self.URL_PATH}"

    def open(self) -> None:
        self.page.goto(self.url)
