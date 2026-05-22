"""Test data model for a SauceDemo checkout customer."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CheckoutCustomer:
    first_name: str
    last_name: str
    postal_code: str
