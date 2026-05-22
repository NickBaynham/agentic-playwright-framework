"""Template for a Playwright component object.

Components model reusable UI regions: nav bars, menus, modals, product
cards, cart drawers. They scope to a root locator and do not perform
full-page navigation or business assertions.
"""

from playwright.sync_api import Locator, Page


class <ComponentName>:
    def __init__(self, page: Page, root: Locator):
        self.page = page
        self.root = root

    @property
    def <element_name>(self) -> Locator:
        return self.root.get_by_role("link", name="<Visible Name>")

    def <action_name>(self) -> None:
        self.<element_name>.click()
