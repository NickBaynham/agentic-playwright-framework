"""InventoryPage — product listing at /inventory.html.

Per-product Add to cart and Remove buttons are disambiguated by the
product slug (``data-test='add-to-cart-<slug>'`` / ``remove-<slug>'``).
The shopping cart link is icon-only with no accessible name, so the
``data-test='shopping-cart-link'`` attribute is the stable locator.
The cart badge is conditional; it only renders when the cart has items.
"""

from __future__ import annotations

from playwright.sync_api import Locator

from framework.models.product import Product
from framework.pages.base_page import BasePage


class InventoryPage(BasePage):
    URL_PATH = "/inventory.html"

    @property
    def products_listing(self) -> Locator:
        # "Products" header is rendered as a generic element, not a heading role.
        return self.page.get_by_text("Products", exact=True)

    @property
    def shopping_cart_link(self) -> Locator:
        return self.page.locator("[data-test='shopping-cart-link']")

    @property
    def cart_badge(self) -> Locator:
        return self.page.locator("[data-test='shopping-cart-badge']")

    def add_to_cart_button(self, product: Product) -> Locator:
        return self.page.locator(f"[data-test='add-to-cart-{product.slug}']")

    def remove_button(self, product: Product) -> Locator:
        return self.page.locator(f"[data-test='remove-{product.slug}']")

    def add_to_cart(self, product: Product) -> None:
        self.add_to_cart_button(product).click()

    def open_cart(self) -> None:
        self.shopping_cart_link.click()
