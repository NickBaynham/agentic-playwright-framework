"""Test data model for a SauceDemo product."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Product:
    name: str
    price: Decimal

    @property
    def slug(self) -> str:
        """Slug used inside per-product ``data-test`` attributes.

        SauceDemo encodes the product slug as the lowercase name with spaces
        replaced by hyphens — for example ``Sauce Labs Backpack`` becomes
        ``sauce-labs-backpack``. The slug is consumed by the inventory and
        cart pages to disambiguate repeated Add to cart and Remove buttons.
        """
        return self.name.lower().replace(" ", "-")
