"""Template for a Playwright page object.

Page objects expose locators as properties and user actions as methods.
They do not own business assertions. They do not embed environment-specific
data; that comes from fixtures or method arguments.
"""

from playwright.sync_api import Page


class <PageName>Page:
    URL_PATH = "/<path>"

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def open(self) -> None:
        self.page.goto(f"{self.base_url}{self.URL_PATH}")

    @property
    def <element_name>(self):
        return self.page.get_by_role("button", name="<Visible Name>")

    @property
    def <field_name>(self):
        return self.page.get_by_label("<Field Label>")

    def <action_name>(self, value: str) -> None:
        self.<field_name>.fill(value)
        self.<element_name>.click()
