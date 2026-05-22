"""SauceDemo inventory page object example."""

from playwright.sync_api import Page


class InventoryPage:
    URL_PATH = "/inventory.html"

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    @property
    def products_heading(self):
        return self.page.get_by_role("heading", name="Products")

    @property
    def shopping_cart_link(self):
        return self.page.get_by_test_id("shopping-cart-link")

    @property
    def cart_badge(self):
        return self.page.locator(".shopping_cart_badge")

    def add_to_cart(self, product_name: str) -> None:
        card = self.page.get_by_role("link", name=product_name).locator("..").locator("..")
        card.get_by_role("button", name="Add to cart").click()
