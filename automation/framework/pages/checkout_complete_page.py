"""CheckoutCompletePage — order confirmation at /checkout-complete.html."""

from __future__ import annotations

from playwright.sync_api import Locator

from framework.pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    URL_PATH = "/checkout-complete.html"

    @property
    def thank_you_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="Thank you for your order!")

    @property
    def back_home_button(self) -> Locator:
        return self.page.get_by_role("button", name="Back Home")

    def back_to_inventory(self) -> None:
        self.back_home_button.click()
