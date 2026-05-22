"""CheckoutOverviewPage — order overview at /checkout-step-two.html.

Item total, tax, and total are read via stable ``data-test`` labels. The
displayed strings contain a label and a currency value; helpers parse the
trailing currency amount as a ``Decimal`` so tests can assert relational
identities (``total = item_total + tax``) without exact-string matching.
"""

from __future__ import annotations

import re
from decimal import Decimal

from playwright.sync_api import Locator

from framework.pages.base_page import BasePage

_CURRENCY_PATTERN = re.compile(r"\$\s*([0-9]+(?:\.[0-9]+)?)")


def _parse_currency(text: str) -> Decimal:
    """Return the trailing currency amount in ``text`` as a Decimal.

    Raises ``ValueError`` when no currency value is found, which surfaces
    a parsing failure at the test layer rather than silently returning a
    misleading default.
    """
    match = _CURRENCY_PATTERN.search(text)
    if match is None:
        raise ValueError(f"No currency amount found in: {text!r}")
    return Decimal(match.group(1))


class CheckoutOverviewPage(BasePage):
    URL_PATH = "/checkout-step-two.html"

    @property
    def item_total_label(self) -> Locator:
        return self.page.locator("[data-test='subtotal-label']")

    @property
    def tax_label(self) -> Locator:
        return self.page.locator("[data-test='tax-label']")

    @property
    def total_label(self) -> Locator:
        return self.page.locator("[data-test='total-label']")

    @property
    def finish_button(self) -> Locator:
        return self.page.get_by_role("button", name="Finish")

    @property
    def cancel_button(self) -> Locator:
        return self.page.locator("[data-test='cancel']")

    def read_item_total(self) -> Decimal:
        return _parse_currency(self.item_total_label.inner_text())

    def read_tax(self) -> Decimal:
        return _parse_currency(self.tax_label.inner_text())

    def read_total(self) -> Decimal:
        return _parse_currency(self.total_label.inner_text())

    def finish_order(self) -> None:
        self.finish_button.click()
