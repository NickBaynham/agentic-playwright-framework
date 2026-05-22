"""Factory helpers for generated test data.

Use factories when a test needs a fresh entity rather than a fixture from
YAML (for example, a uniquely named customer for an isolation test). Always
mark generated values so they are distinguishable from canonical seed data.
"""

from __future__ import annotations

import uuid

from framework.models.checkout_customer import CheckoutCustomer


def make_checkout_customer(
    first_name: str = "Test",
    last_name: str | None = None,
    postal_code: str = "12345",
) -> CheckoutCustomer:
    return CheckoutCustomer(
        first_name=first_name,
        last_name=last_name or f"User-{uuid.uuid4().hex[:8]}",
        postal_code=postal_code,
    )
