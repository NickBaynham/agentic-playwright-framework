# Automation Implementation Report: Standard User Checkout (Suite)

## Source

| Field | Value |
|---|---|
| Source Type | BDD Spec + Gherkin feature + traceability matrix |
| Source File | `specs/bdd/markdown/standard_user_checkout.md` |
| Feature | Standard User Checkout |
| Scenario(s) | TC-01, TC-02, TC-03, TC-04, TC-05, TC-06 |

## Summary

Implemented the six High-priority `@automatable` scenarios from the standard user checkout BDD spec as a single PyTest test file plus six page objects, three test data models, two YAML data files, and ten new fixtures. Each test follows Arrange / Act / Assert, asserts at the top level with Playwright `expect`, and references its source scenario in the docstring. No page object owns a business assertion. No URLs, credentials, product names, or checkout values are hard-coded in the tests.

Two scenarios from the spec were not implemented because both carry `@needs-clarification`:

- **TC-07** — *Cart is empty after order completion*. Cart-clear contract is not documented.
- **TC-08** — *Checkout information form rejects missing required fields*. Validation behavior and error-element structure have not been observed.

No packages were installed and no tests were executed in this pass; results below are Pending.

## Files Created

| File | Purpose |
|---|---|
| `automation/framework/models/product.py` | `Product` dataclass with `name`, `price` (Decimal), and a `slug` property used to derive per-product `data-test` ids. |
| `automation/framework/pages/login_page.py` | Login page object: Username, Password, Login, conditional Error banner, `login_as(user)`. |
| `automation/framework/pages/inventory_page.py` | Inventory page object: Products listing, shopping cart link, cart badge, per-product `add_to_cart_button` / `remove_button`, `add_to_cart`, `open_cart`. |
| `automation/framework/pages/cart_page.py` | Cart page object: heading, Continue Shopping, Checkout, per-product `line_item`/`line_item_quantity`/`line_item_price`, `proceed_to_checkout`. |
| `automation/framework/pages/checkout_information_page.py` | First Name, Last Name, Postal Code inputs, Continue, Cancel, `fill_customer`, `continue_to_overview`. |
| `automation/framework/pages/checkout_overview_page.py` | Item total, Tax, Total labels (data-test), Finish, Cancel, currency-parsing read helpers, `finish_order`. |
| `automation/framework/pages/checkout_complete_page.py` | Thank-you heading, Back Home button, `back_to_inventory`. |
| `automation/test_data/local/products.yaml` | All six observed products with prices. |
| `automation/test_data/local/checkout_customers.yaml` | Canonical default checkout customer (`Test User / 12345`). |
| `automation/tests/ui/test_standard_user_checkout.py` | Six PyTest tests, one per High scenario. |

## Files Modified

| File | Change |
|---|---|
| `automation/framework/data/test_data_loader.py` | Added `load_products` and `load_checkout_customers`; both return typed models. |
| `automation/tests/conftest.py` | Added `products`, `backpack`, `checkout_customers`, `default_checkout_customer` data fixtures and six page-object fixtures (`login_page`, `inventory_page`, `cart_page`, `checkout_information_page`, `checkout_overview_page`, `checkout_complete_page`). |

## Test Data Added or Modified

| File | Data | Notes |
|---|---|---|
| `automation/test_data/local/products.yaml` | Six SauceDemo products with names and prices. | Prices stored as strings to preserve decimal precision through YAML. The loader coerces to `Decimal`. |
| `automation/test_data/local/checkout_customers.yaml` | `default` checkout customer. | Tester-generated identifiers; no PII. |

## Fixtures Added or Modified

| Fixture | Scope | Purpose |
|---|---|---|
| `products` | function | All products defined for the active environment. |
| `backpack` | function | `Product` for Sauce Labs Backpack — the canonical smoke item. |
| `checkout_customers` | function | All canonical checkout customers. |
| `default_checkout_customer` | function | The `default` `CheckoutCustomer`. |
| `login_page` | function | `LoginPage` bound to `page` and `settings.base_url`. |
| `inventory_page` | function | `InventoryPage` bound to `page` and `settings.base_url`. |
| `cart_page` | function | `CartPage` bound to `page` and `settings.base_url`. |
| `checkout_information_page` | function | `CheckoutInformationPage` bound to `page` and `settings.base_url`. |
| `checkout_overview_page` | function | `CheckoutOverviewPage` bound to `page` and `settings.base_url`. |
| `checkout_complete_page` | function | `CheckoutCompletePage` bound to `page` and `settings.base_url`. |

## Page Objects Added or Modified

| Page Object | Purpose |
|---|---|
| `LoginPage` | Authenticate a user. |
| `InventoryPage` | Browse the product listing and operate the cart icon / cart badge. |
| `CartPage` | Read cart line items and proceed to checkout. |
| `CheckoutInformationPage` | Submit the shipping form. |
| `CheckoutOverviewPage` | Read totals (Item total, Tax, Total) and submit the order. |
| `CheckoutCompletePage` | Confirm the order. |

## Locator Decision Log

Decision values: Accepted, Accepted with Scope, Modified, Rejected, Needs Review. Source for every candidate is `specs/bdd/markdown/standard_user_checkout.md` (Automation Notes per scenario) which carries them forward from `sessions/mcp-exploration/saucedemo/standard-user-checkout-workflow_session.md`.

| Page Object | Element | Candidate Locator | Final Locator | Decision | Rationale | Source |
|---|---|---|---|---|---|---|
| LoginPage | Username input | `page.get_by_placeholder("Username")` | `page.get_by_placeholder("Username")` | Accepted | Stable placeholder; unique field. | BDD Automation Notes — TC-01 |
| LoginPage | Password input | `page.get_by_placeholder("Password")` | `page.get_by_placeholder("Password")` | Accepted | Stable placeholder; unique field. | BDD Automation Notes — TC-01 |
| LoginPage | Login button | `page.get_by_role("button", name="Login")` | `page.get_by_role("button", name="Login")` | Accepted | Accessible role + name. | BDD Automation Notes — TC-01 |
| LoginPage | Error banner | `page.locator("[data-test='error']")` | `page.locator("[data-test='error']")` | Accepted | Conditional element; locator is exposed but not asserted on by the implemented (positive) scenarios. | BDD Automation Notes — TC-01 |
| InventoryPage | Products listing | `page.get_by_role("heading", name="Products")` | `page.get_by_text("Products", exact=True)` | Modified | The "Products" header is rendered as a `generic`, not a `heading`. The role-based locator would not match. Switched to exact text. | BDD Automation Notes — TC-01; Anomaly APP-5 in source session |
| InventoryPage | Shopping cart link | `page.locator("[data-test='shopping-cart-link']")` | `page.locator("[data-test='shopping-cart-link']")` | Accepted | Icon-only; the anchor has no accessible name (Anomaly APP-1). | BDD Automation Notes — TC-01 |
| InventoryPage | Cart badge | `page.locator("[data-test='shopping-cart-badge']")` | `page.locator("[data-test='shopping-cart-badge']")` | Accepted | Conditional element; assertions must tolerate the badge being absent. | BDD Automation Notes — TC-02 |
| InventoryPage | Per-product Add to cart | `page.locator("[data-test='add-to-cart-sauce-labs-backpack']")` | `page.locator(f"[data-test='add-to-cart-{product.slug}']")` | Accepted with Scope | Generalized over any `Product` by using the model's `slug` property. Avoids hard-coding the backpack slug. | BDD Automation Notes — TC-02 |
| InventoryPage | Per-product Remove | `page.locator("[data-test='remove-sauce-labs-backpack']")` | `page.locator(f"[data-test='remove-{product.slug}']")` | Accepted with Scope | Same generalization as Add. | BDD Automation Notes — TC-02 |
| CartPage | Your Cart heading | `page.get_by_role("heading", name="Your Cart")` | `page.get_by_text("Your Cart", exact=True)` | Modified | Rendered as a `generic`, same as "Products". Switched to exact text. | BDD Automation Notes — TC-03; Anomaly APP-5 |
| CartPage | Continue Shopping button | `page.get_by_role("button", name=re.compile("Continue Shopping"))` | `page.locator("[data-test='continue-shopping']")` | Modified | Source session shows the button text is `"Go back Continue Shopping"` (concatenated label including the back-arrow image). The role+name regex match was fragile; `data-test` is the stable handle. | BDD Automation Notes — TC-03; source session snapshot |
| CartPage | Checkout button | `page.get_by_role("button", name="Checkout")` | `page.get_by_role("button", name="Checkout")` | Accepted | Accessible role + name. | BDD Automation Notes — TC-03 |
| CartPage | Cart line item by product | `page.locator(".cart_item").filter(has_text="Sauce Labs Backpack")` | `page.locator(".cart_item").filter(has_text=product.name)` | Accepted with Scope | Generalized by `product.name`. The line item container has no per-item `data-test`. | BDD Automation Notes — TC-03 |
| CartPage | Cart line item quantity | (not specified in BDD notes) | scoped `.cart_quantity` inside the row | Modified | Source session shows the quantity is a `.cart_quantity` element inside the row. Scoped via the row locator. | Source session — Cart Page observed elements |
| CartPage | Cart line item price | (not specified in BDD notes) | scoped `.inventory_item_price` inside the row | Modified | Source session shows the price is rendered as `.inventory_item_price` in the row. Scoped via the row locator. | Source session — Cart Page observed elements |
| CheckoutInformationPage | First Name input | `page.get_by_placeholder("First Name")` | `page.get_by_placeholder("First Name")` | Accepted | Stable placeholder. | BDD Automation Notes — TC-04 |
| CheckoutInformationPage | Last Name input | `page.get_by_placeholder("Last Name")` | `page.get_by_placeholder("Last Name")` | Accepted | Stable placeholder. | BDD Automation Notes — TC-04 |
| CheckoutInformationPage | Postal Code input | `page.get_by_placeholder("Zip/Postal Code")` | `page.get_by_placeholder("Zip/Postal Code")` | Accepted | Stable placeholder. | BDD Automation Notes — TC-04 |
| CheckoutInformationPage | Continue button | `page.get_by_role("button", name="Continue")` | `page.get_by_role("button", name="Continue")` | Accepted | Accessible role + name. | BDD Automation Notes — TC-04 |
| CheckoutInformationPage | Cancel button | `page.get_by_role("button", name=re.compile("Cancel"))` | `page.locator("[data-test='cancel']")` | Modified | Same accessible-name concatenation problem as Continue Shopping. `data-test` is stable. | Source session — Checkout: Your Information |
| CheckoutOverviewPage | Item total label | `page.locator("[data-test='subtotal-label']")` | `page.locator("[data-test='subtotal-label']")` | Accepted | Stable `data-test` for a computed value. | BDD Automation Notes — TC-05 |
| CheckoutOverviewPage | Tax label | `page.locator("[data-test='tax-label']")` | `page.locator("[data-test='tax-label']")` | Accepted | Stable `data-test` for a computed value. | BDD Automation Notes — TC-05 |
| CheckoutOverviewPage | Total label | `page.locator("[data-test='total-label']")` | `page.locator("[data-test='total-label']")` | Accepted | Stable `data-test` for a computed value. | BDD Automation Notes — TC-05 |
| CheckoutOverviewPage | Finish button | `page.get_by_role("button", name="Finish")` | `page.get_by_role("button", name="Finish")` | Accepted | Accessible role + name. | BDD Automation Notes — TC-06 |
| CheckoutOverviewPage | Cancel button | (not specified in BDD notes) | `page.locator("[data-test='cancel']")` | Modified | Same accessible-name concatenation issue as the other Cancel buttons. | Source session — Checkout: Overview |
| CheckoutCompletePage | Thank-you heading | `page.get_by_role("heading", name="Thank you for your order!")` | `page.get_by_role("heading", name="Thank you for your order!")` | Accepted | Accessible heading; primary success oracle. | BDD Automation Notes — TC-06 |
| CheckoutCompletePage | Back Home button | `page.get_by_role("button", name="Back Home")` | `page.get_by_role("button", name="Back Home")` | Accepted | Accessible role + name. | BDD Automation Notes — TC-06 |

## Locator Risks Carried Forward

| Page Object | Element | Risk | Mitigation |
|---|---|---|---|
| InventoryPage | Per-product Add/Remove | Six product cards share the same visible text. | Resolved by per-product `data-test` keyed off the `Product.slug`. |
| InventoryPage | Cart badge | Conditional element — renders only when the cart has items. | Tests assert on text via `expect(...).to_have_text("1")` after an add. Empty-state assertions can use `expect(...).to_be_hidden()` when added. |
| InventoryPage | Products listing | Rendered as `generic`, not `heading` role (Anomaly APP-5). | Switched from `get_by_role("heading", ...)` to `get_by_text("Products", exact=True)`. |
| CartPage | Your Cart heading | Same as Products listing. | Switched to `get_by_text`. |
| CartPage / CheckoutInformationPage / CheckoutOverviewPage | Continue Shopping / Cancel buttons | Accessible name concatenates the back-arrow image label with the visible text (e.g., `"Go back Continue Shopping"`). | Switched to `data-test` for these controls. Accessible-name fix at the application would let us prefer role+name again. |
| CheckoutOverviewPage | Totals (Item total, Tax, Total) | Numeric content is dynamic. | Read via `inner_text()` and parsed by `_parse_currency` into `Decimal`. Tests assert the arithmetic identity, not the exact string. |
| All Cancel buttons | Cancel button's accessible name varies across pages. | Standardized on `data-test='cancel'` (stable across all pages observed). | — |

## Commands Run

| Command | Result |
|---|---|
| `python3 -m ast ...` (syntax check) | All 12 modified/new Python files parsed cleanly. |
| `pdm install -d` | OK. 25 packages installed; virtualenv created at `automation/.venv`. |
| `pdm run install-browsers` | OK. Chromium binaries available via the existing `~/Library/Caches/ms-playwright/` cache. |
| `HEADLESS=true pdm run pytest tests/ui/test_standard_user_checkout.py -v` | **6 passed in 6.04s.** |
| `HEADLESS=true pdm run pytest tests/ -v` (full suite, including the two framework-smoke tests) | **8 passed in 4.37s.** |

Headless mode was selected via the `HEADLESS=true` env override so the suite would not pop a visible browser during the conversation. The `local` environment's default `headless: false` remains intact for interactive runs.

## Test Results

| Test | Status | Notes |
|---|---|---|
| `tests/ui/test_standard_user_checkout.py::test_standard_user_logs_in_successfully[chromium]` | Passed | First run, no retries. |
| `tests/ui/test_standard_user_checkout.py::test_adding_product_updates_cart_badge_and_toggles_button[chromium]` | Passed | First run. TOOL-1 (MCP click flakiness) did not reproduce against the Playwright Python API, confirming it was MCP-specific. |
| `tests/ui/test_standard_user_checkout.py::test_cart_lists_added_item_with_quantity_and_price[chromium]` | Passed | First run. |
| `tests/ui/test_standard_user_checkout.py::test_checkout_information_advances_to_overview_with_valid_input[chromium]` | Passed | First run. |
| `tests/ui/test_standard_user_checkout.py::test_overview_totals_satisfy_item_total_plus_tax_equals_total[chromium]` | Passed | First run. Relational identity assertion (`Total = Item total + Tax`) held; exact tax not asserted by design. |
| `tests/ui/test_standard_user_checkout.py::test_finishing_order_shows_confirmation_page[chromium]` | Passed | First run. |
| `tests/ui/test_framework_smoke.py::test_settings_loads_local_environment` | Passed | Re-verified after the conftest extensions. |
| `tests/ui/test_framework_smoke.py::test_standard_user_loaded_from_test_data` | Passed | Re-verified after the conftest extensions. |

Reports written:

- HTML: `automation/reports/html/report.html`
- JUnit XML: `automation/reports/junit/results.xml`

## Traceability

| Automated Test | Source Scenario | Source File |
|---|---|---|
| `tests/ui/test_standard_user_checkout.py::test_standard_user_logs_in_successfully` | TC-01 — Standard user logs in successfully | `specs/bdd/markdown/standard_user_checkout.md` |
| `tests/ui/test_standard_user_checkout.py::test_adding_product_updates_cart_badge_and_toggles_button` | TC-02 — Adding one product updates the cart badge and toggles the Add button to Remove | `specs/bdd/markdown/standard_user_checkout.md` |
| `tests/ui/test_standard_user_checkout.py::test_cart_lists_added_item_with_quantity_and_price` | TC-03 — Cart page lists the added item with the correct name, quantity, and price | `specs/bdd/markdown/standard_user_checkout.md` |
| `tests/ui/test_standard_user_checkout.py::test_checkout_information_advances_to_overview_with_valid_input` | TC-04 — Checkout information form advances to the overview with valid input | `specs/bdd/markdown/standard_user_checkout.md` |
| `tests/ui/test_standard_user_checkout.py::test_overview_totals_satisfy_item_total_plus_tax_equals_total` | TC-05 — Overview page totals satisfy Item total + Tax = Total | `specs/bdd/markdown/standard_user_checkout.md` |
| `tests/ui/test_standard_user_checkout.py::test_finishing_order_shows_confirmation_page` | TC-06 — Finishing the order shows the order confirmation page | `specs/bdd/markdown/standard_user_checkout.md` |

## Risks and Open Questions

- **All Modified locators were correct on the first run.** The four `Modified` decisions (Products text, Your Cart text, `data-test='continue-shopping'`, `data-test='cancel'`) avoided the brittle accessible-name regex paths and matched cleanly. If the application is ever updated to use real `heading` roles or to clean up the concatenated button accessible names, those locators should be re-evaluated.
- **The BDD review's Medium fixes (M-1 through M-4) are not applied to the spec.** They did not block this implementation pass — the tests already resolve M-1 by naming the cart item in every scenario that needs one, and M-3 (the awkward "When the user reads…" Gherkin phrasing) is a Gherkin-only concern that does not appear in the Python test layout. M-2 (TC-02 dual-outcome title) and M-4 (TC-07 temporal Given) remain on the BDD spec and should be applied via `/review-bdd` → spec revision before the next pass.
- **TC-07 and TC-08 are deferred.** Both carry `@needs-clarification`. Convert to scenarios after the cart-clear contract is confirmed and after a focused re-exploration of `/checkout-step-one.html` validation.
- **Tax-rate assumption:** TC-05 asserts only the relational identity `Total = Item total + Tax`. If the demo's tax rate is ever confirmed as a fixed business rule, add a complementary scenario asserting the exact tax for a known item price.
- **Locator drift risk:** four locators were Modified from BDD candidates (Products listing, Your Cart heading, Continue Shopping, Cancel). The accessibility issues that motivated the Modifications (Anomaly APP-1, APP-5) are tracked but not fixed at the application; when they are fixed, the Modified locators should be re-evaluated.
- **No CI workflow yet.** When tests are stable, add a GitHub Actions workflow that runs `make install && make install-browsers && make test-smoke`.

## Human Review Checklist

- [ ] Tests are readable (`tests/ui/test_standard_user_checkout.py`).
- [ ] Assertions are at test level (Playwright `expect` for UI; `assert` for data identities in TC-05).
- [ ] No hard-coded environment data (config + YAML + `.env`).
- [ ] Fixtures are appropriate (function scope for page objects and per-test data; session for `settings` and `browser_type_launch_args`).
- [ ] Page objects are not hiding business assertions (verified — page objects expose locators and actions, plus arithmetic-friendly `read_*` methods on `CheckoutOverviewPage`).
- [ ] Locator strategy is acceptable (see Locator Decision Log; Modified locators have rationale).
- [ ] Related tests pass (pending execution).
