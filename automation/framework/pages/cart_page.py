"""CartPage — cart contents at /cart.html.

Cart line items repeat (one row per product) and the row container has no
per-item ``data-test``; rows are scoped by product name.
"""

from __future__ import annotations

from playwright.sync_api import Locator

from framework.models.product import Product
from framework.pages.base_page import BasePage


class CartPage(BasePage):
    URL_PATH = "/cart.html"

    @property
    def your_cart_heading(self) -> Locator:
        # Rendered as a generic, not a heading role.
        return self.page.get_by_text("Your Cart", exact=True)

    @property
    def continue_shopping_button(self) -> Locator:
        return self.page.locator("[data-test='continue-shopping']")

    @property
    def checkout_button(self) -> Locator:
        return self.page.get_by_role("button", name="Checkout")

    def line_item(self, product: Product) -> Locator:
        return self.page.locator(".cart_item").filter(has_text=product.name)

    def line_item_quantity(self, product: Product) -> Locator:
        return self.line_item(product).locator(".cart_quantity")

    def line_item_price(self, product: Product) -> Locator:
        return self.line_item(product).locator(".inventory_item_price")

    def proceed_to_checkout(self) -> None:
        self.checkout_button.click()
