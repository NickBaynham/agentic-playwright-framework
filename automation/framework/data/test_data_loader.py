"""YAML-backed test data loaders.

The active environment is resolved by ``config.settings.load_settings`` and
the resulting ``test_data_path`` is passed in here. Loaders return typed
domain models so tests do not pass raw dicts around.
"""

from __future__ import annotations

from decimal import Decimal
from pathlib import Path

import yaml

from framework.models.checkout_customer import CheckoutCustomer
from framework.models.product import Product
from framework.models.user import User


def _read_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def load_users(test_data_path: Path) -> dict[str, User]:
    """Return a dict of users keyed by their YAML key (e.g. ``standard_user``)."""
    data = _read_yaml(test_data_path / "users.yaml")
    raw_users = data.get("users", {})
    return {
        key: User(
            username=entry["username"],
            password=entry["password"],
            role=entry.get("role", "standard"),
        )
        for key, entry in raw_users.items()
    }


def load_products(test_data_path: Path) -> dict[str, Product]:
    """Return a dict of products keyed by their YAML key (e.g. ``sauce_labs_backpack``)."""
    data = _read_yaml(test_data_path / "products.yaml")
    raw_products = data.get("products", {})
    return {
        key: Product(name=entry["name"], price=Decimal(str(entry["price"])))
        for key, entry in raw_products.items()
    }


def load_checkout_customers(test_data_path: Path) -> dict[str, CheckoutCustomer]:
    """Return a dict of checkout customers keyed by their YAML key (e.g. ``default``)."""
    data = _read_yaml(test_data_path / "checkout_customers.yaml")
    raw_customers = data.get("checkout_customers", {})
    return {
        key: CheckoutCustomer(
            first_name=entry["first_name"],
            last_name=entry["last_name"],
            postal_code=str(entry["postal_code"]),
        )
        for key, entry in raw_customers.items()
    }
