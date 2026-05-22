"""CheckoutInformationPage — checkout step one at /checkout-step-one.html."""

from __future__ import annotations

from playwright.sync_api import Locator

from framework.models.checkout_customer import CheckoutCustomer
from framework.pages.base_page import BasePage


class CheckoutInformationPage(BasePage):
    URL_PATH = "/checkout-step-one.html"

    @property
    def first_name_input(self) -> Locator:
        return self.page.get_by_placeholder("First Name")

    @property
    def last_name_input(self) -> Locator:
        return self.page.get_by_placeholder("Last Name")

    @property
    def postal_code_input(self) -> Locator:
        return self.page.get_by_placeholder("Zip/Postal Code")

    @property
    def continue_button(self) -> Locator:
        return self.page.get_by_role("button", name="Continue")

    @property
    def cancel_button(self) -> Locator:
        return self.page.locator("[data-test='cancel']")

    def fill_customer(self, customer: CheckoutCustomer) -> None:
        self.first_name_input.fill(customer.first_name)
        self.last_name_input.fill(customer.last_name)
        self.postal_code_input.fill(customer.postal_code)

    def continue_to_overview(self) -> None:
        self.continue_button.click()
