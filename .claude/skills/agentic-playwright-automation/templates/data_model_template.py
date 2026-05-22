"""Template for test data models.

Use stdlib `dataclasses` for simple structured test data. Switch to
`pydantic.BaseModel` only when validation or coercion is required.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    username: str
    password: str
    role: str = "standard"


@dataclass(frozen=True)
class Product:
    name: str
    price: float


@dataclass(frozen=True)
class CheckoutCustomer:
    first_name: str
    last_name: str
    postal_code: str
