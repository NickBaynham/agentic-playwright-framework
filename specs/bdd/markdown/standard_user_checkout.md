# Feature: Standard User Checkout

## Business Goal

A returning standard user can sign in to the Swag Labs (saucedemo) storefront, add a product to the cart, complete checkout, and receive an order confirmation. This is the primary purchase path; if it breaks, customers cannot transact.

## Source Material

- Exploration session: `sessions/mcp-exploration/saucedemo/standard-user-checkout-workflow_session.md`
- Browser/MCP observations: snapshots `page-2026-05-22T01-45-49-729Z.yml` … `page-2026-05-22T01-46-...` (recorded in the session Action Timeline).
- Application: Swag Labs (saucedemo), https://www.saucedemo.com/
- Related notes: candidate page models and locator candidates documented per page in the source session report.

## Assumptions

- The `standard_user` account is enabled and uses the published shared password `secret_sauce`.
- The cart badge count is intended to reflect the number of items in the cart. (Inferred from observed badge incrementing to `1` after one add.)
- "Free Pony Express Delivery!" is the default and only shipping option for the happy path.
- The tax displayed on the overview page is computed from the item subtotal (~8% observed for this session). The exact formula is not documented; tests should compare relationally (`Total = Item total + Tax`) rather than asserting an exact tax value.
- The product `Sauce Labs Backpack` ($29.99) is representative of any inventory item that exercises the same checkout path.

## Open Questions

- What are the explicit validation rules for First Name, Last Name, and Zip/Postal Code on `/checkout-step-one.html`? (TC-08)
- Is the cart guaranteed to be empty after a successful order? Is that behavior covered by a requirement, or is the absence of the cart badge on `/checkout-complete.html` incidental? (TC-07)
- Is the ~8% tax rate a stable business rule, region-dependent, or fixed for the demo? Should tests assert the exact value or only the `Item total + Tax = Total` relationship? (TC-05)
- Is there an accessibility requirement that the cart link must be reachable by accessible name? If yes, the missing name on `a.shopping_cart_link` is a defect rather than an observation. (TC-09 — out of feature scope; tracked in source session.)
- Are the `events.backtrace.io` 401 responses expected, or do they indicate misconfigured telemetry credentials? (TC-10 — out of feature scope; tracked in source session.)
- Does the application support multi-quantity line items, or is quantity always 1?

## Potential Defects or Ambiguities

- **APP-1 (Accessibility, Potential Defect):** The header shopping cart link has no accessible name and does not surface in the accessibility tree until the cart badge is non-empty. Tracked in the source session; out of scope for this feature beyond noting that automation locators must rely on `data-test` for this element.
- **TOOL-1 (Tooling, not a product defect):** A standard MCP `browser_click` on inventory `Add to cart` and several checkout-advance buttons reported success but did not change application state in the exploration sessions. A DOM `.click()` via `browser_evaluate` worked. This is documented as a tooling caveat for exploration only; downstream Playwright automation should use the standard Playwright click API and verify reliability there.

## Scenarios

### Scenario: Standard user logs in successfully

**Scenario ID:** TC-01
**Tags:** `@ui` `@smoke` `@login` `@positive` `@automatable`
**Automation Priority:** High
**Priority Rationale:** Login is the precondition for every checkout scenario; smoke-critical.

#### Given

- The standard user is on the saucedemo login page.

#### When

- The user submits valid credentials.

#### Then

- The user lands on the inventory page (`/inventory.html`).
- The Products listing is visible.

#### Test Data

| Field | Value | Source | Notes |
|---|---|---|---|
| Username | `standard_user` | Demo app landing page | Public demo credential. |
| Password | `secret_sauce` | Demo app landing page | Public demo credential. |

#### Observed Evidence

- After clicking Login the URL advanced to `https://www.saucedemo.com/inventory.html`; six product cards were rendered with the Products header.

#### Automation Notes

These notes are optional implementation hints from exploration. They are not final automation decisions.

| Element or Action | Locator Candidate | Confidence | Source | Notes |
|---|---|---|---|---|
| Username input | `page.get_by_placeholder("Username")` | High | `sessions/mcp-exploration/saucedemo/standard-user-checkout-workflow_session.md` — Login Page | Or `[data-test='username']` |
| Password input | `page.get_by_placeholder("Password")` | High | Source session — Login Page | Or `[data-test='password']` |
| Login button | `page.get_by_role("button", name="Login")` | High | Source session — Login Page | Or `[data-test='login-button']` |
| Products listing | `page.get_by_text("Products", exact=True)` | Medium | Source session — Inventory Page | Header rendered as generic, not heading role (APP-5) |

#### Locator Risks

- "Products" header is rendered as a `generic`, not a `heading`. A role-based heading assertion will not match; prefer text-based or `data-test`.

#### Notes

- Foundation scenario; every other checkout scenario depends on a successful login as `standard_user`.

---

### Scenario: Adding a product places it in the cart

**Scenario ID:** TC-02
**Tags:** `@ui` `@smoke` `@cart` `@positive` `@automatable`
**Automation Priority:** High
**Priority Rationale:** Core add-to-cart behavior with deterministic observables. Both Then assertions (badge count and button toggle) are direct, immediate consequences of the same single user action.

#### Given

- The standard user is logged in and viewing the inventory page.

#### When

- The user adds Sauce Labs Backpack to the cart from the inventory listing.

#### Then

- The cart badge in the header shows `1`.
- The Sauce Labs Backpack action button label changes from `Add to cart` to `Remove`.

#### Test Data

| Field | Value | Source | Notes |
|---|---|---|---|
| Product | `Sauce Labs Backpack` ($29.99) | Inventory listing | Any product on the listing exercises the same flow. |

#### Observed Evidence

- Snapshot after add: header badge generic with text `"1"` present; `Add to cart` button replaced by `Remove`.

#### Automation Notes

| Element or Action | Locator Candidate | Confidence | Source | Notes |
|---|---|---|---|---|
| Backpack Add to cart | `page.locator("[data-test='add-to-cart-sauce-labs-backpack']")` | High | Source session — Inventory Page | Per-product `data-test` disambiguates the repeated `Add to cart` text |
| Backpack Remove | `page.locator("[data-test='remove-sauce-labs-backpack']")` | High | Source session — Inventory Page | Conditional; only present after Add |
| Cart badge | `page.locator("[data-test='shopping-cart-badge']")` | High | Source session — Inventory Page | Conditional — visible only after cart has items |

#### Locator Risks

- Six product cards share the same `Add to cart` visible text. A naïve role/name locator will match the first product, not Sauce Labs Backpack. Use the per-product `data-test`.
- Cart badge is conditional; assertions must tolerate the badge being absent before the first add.

#### Notes

- See **TOOL-1** in Potential Defects regarding MCP click reliability. This does not affect a Playwright-Python implementation; standard `locator.click()` should be used.

---

### Scenario: Cart page lists the added item with the correct name, quantity, and price

**Scenario ID:** TC-03
**Tags:** `@ui` `@smoke` `@cart` `@positive` `@automatable`
**Automation Priority:** High
**Priority Rationale:** Confirms cart persistence between inventory and cart routes; a cart that loses items between pages breaks every downstream scenario.

#### Given

- The standard user is logged in and has added Sauce Labs Backpack to the cart.

#### When

- The user opens the cart.

#### Then

- The cart lists exactly one line item for Sauce Labs Backpack.
- The line item shows quantity `1` and price `$29.99`.
- A Checkout action is available.

#### Test Data

| Field | Value | Source | Notes |
|---|---|---|---|
| Product | `Sauce Labs Backpack` ($29.99) | Inventory listing | Same item used in TC-02. |

#### Observed Evidence

- Cart page rendered one row with `QTY 1`, link text `Sauce Labs Backpack`, price `$29.99`, plus `Remove`, `Continue Shopping`, `Checkout` buttons.

#### Automation Notes

| Element or Action | Locator Candidate | Confidence | Source | Notes |
|---|---|---|---|---|
| Backpack cart line item | `page.locator(".cart_item").filter(has_text="Sauce Labs Backpack")` | Medium | Source session — Cart Page | Scope by product name; cart row container has no per-item `data-test` |
| Checkout button | `page.get_by_role("button", name="Checkout")` | High | Source session — Cart Page | Or `[data-test='checkout']` |

#### Locator Risks

- Cart line items repeat once per product; locators must scope by product name or use a per-product attribute. The line-item container itself does not expose a per-item `data-test`; only the Remove button does.

#### Notes

- None.

---

### Scenario: Checkout information form advances to the overview with valid input

**Scenario ID:** TC-04
**Tags:** `@ui` `@smoke` `@checkout` `@positive` `@automatable`
**Automation Priority:** High
**Priority Rationale:** First branch of the checkout funnel; gates everything downstream.

#### Given

- The standard user is on the checkout information page with one item in the cart.

#### When

- The user submits a valid first name, last name, and postal code.

#### Then

- The user lands on the checkout overview page (`/checkout-step-two.html`).

#### Test Data

| Field | Value | Source | Notes |
|---|---|---|---|
| First Name | `Test` | Tester-generated | Non-empty string. |
| Last Name | `User` | Tester-generated | Non-empty string. |
| Zip/Postal Code | `12345` | Tester-generated | Non-empty; format rules not verified (Open Question). |

#### Observed Evidence

- After Continue, URL advanced to `/checkout-step-two.html` and the overview view rendered with the cart item, payment, shipping, and totals.

#### Automation Notes

| Element or Action | Locator Candidate | Confidence | Source | Notes |
|---|---|---|---|---|
| First Name input | `page.get_by_placeholder("First Name")` | High | Source session — Checkout: Your Information | Or `[data-test='firstName']` |
| Last Name input | `page.get_by_placeholder("Last Name")` | High | Source session | Or `[data-test='lastName']` |
| Postal Code input | `page.get_by_placeholder("Zip/Postal Code")` | High | Source session | Or `[data-test='postalCode']` |
| Continue button | `page.get_by_role("button", name="Continue")` | High | Source session | Or `[data-test='continue']` |

#### Locator Risks

- Field-level error message locators were not exercised in the source session.

#### Notes

- Postal code format rules are not documented; this scenario asserts only that a non-empty value is accepted.

---

### Scenario: Overview page totals satisfy Item total + Tax = Total

**Scenario ID:** TC-05
**Tags:** `@ui` `@smoke` `@checkout` `@positive` `@automatable`
**Automation Priority:** High
**Priority Rationale:** Catches pricing-display regressions on the order summary; observable arithmetic check independent of the exact tax rate.

#### Given

- The standard user is on the checkout overview page with Sauce Labs Backpack in the cart.

#### When

- The user reads the Item total, Tax, and Total values.

#### Then

- `Total = Item total + Tax` when each value is parsed as a decimal currency amount.
- All three values are present and non-empty.

#### Test Data

| Field | Value | Source | Notes |
|---|---|---|---|
| Product | `Sauce Labs Backpack` ($29.99) | Inventory listing | Drives Item total. |

#### Observed Evidence

- Item total: `$29.99`. Tax: `$2.40`. Total: `$32.39`. (29.99 + 2.40 = 32.39.) Tax appears to be ~8% for this session, but the formula is not documented.

#### Automation Notes

| Element or Action | Locator Candidate | Confidence | Source | Notes |
|---|---|---|---|---|
| Item total label | `page.locator("[data-test='subtotal-label']")` | High | Source session — Checkout: Overview | Stable `data-test` for a computed value |
| Tax label | `page.locator("[data-test='tax-label']")` | High | Source session | |
| Total label | `page.locator("[data-test='total-label']")` | High | Source session | |

#### Locator Risks

- Numeric content is dynamic; tests must parse the numeric portion rather than exact-match a full label string.

#### Notes

- The exact tax value (`$2.40`) is intentionally not asserted because the tax rate is not a documented business rule. Asserting the relational identity is more durable.

---

### Scenario: Finishing the order shows the order confirmation page

**Scenario ID:** TC-06
**Tags:** `@ui` `@smoke` `@checkout` `@positive` `@automatable`
**Automation Priority:** High
**Priority Rationale:** Confirms the end-to-end happy path completes; this is the primary success oracle for the entire checkout flow.

#### Given

- The standard user is on the checkout overview page with Sauce Labs Backpack in the cart.

#### When

- The user submits the order.

#### Then

- The user lands on the order confirmation page (`/checkout-complete.html`).
- A heading "Thank you for your order!" is visible.

#### Test Data

| Field | Value | Source | Notes |
|---|---|---|---|
| (No additional input) | Not applicable | n/a | Submission only. |

#### Observed Evidence

- After Finish, URL advanced to `/checkout-complete.html`; the page rendered the "Checkout: Complete!" header, a "Thank you for your order!" heading, and the Back Home button.

#### Automation Notes

| Element or Action | Locator Candidate | Confidence | Source | Notes |
|---|---|---|---|---|
| Finish button | `page.get_by_role("button", name="Finish")` | High | Source session — Checkout: Overview | Or `[data-test='finish']` |
| Thank-you heading | `page.get_by_role("heading", name="Thank you for your order!")` | High | Source session — Checkout: Complete | Primary success oracle |
| Back Home button | `page.get_by_role("button", name="Back Home")` | High | Source session | Or `[data-test='back-to-products']` |

#### Locator Risks

- (none observed)

#### Notes

- None.

---

### Scenario: Cart is empty after order completion

**Scenario ID:** TC-07
**Tags:** `@ui` `@cart` `@positive` `@needs-clarification`
**Automation Priority:** Medium
**Priority Rationale:** Behavior is inferred — the cart badge is absent on `/checkout-complete.html`, but no explicit requirement specifies that the cart must be cleared on order submission. Resolve the Open Question before promoting to High.

#### Given

- The standard user is on the order confirmation page after completing a checkout.

#### When

- The user returns to the inventory page.

#### Then

- The cart badge is not displayed.

#### Test Data

| Field | Value | Source | Notes |
|---|---|---|---|
| (No additional input) | Not applicable | n/a | Observation only. |

#### Observed Evidence

- No cart badge was rendered in the header on `/checkout-complete.html` after Finish. Inventory page after Back Home was not re-snapshotted in this session; the inferred outcome is that the badge remains absent on the inventory page until a new add.

#### Automation Notes

| Element or Action | Locator Candidate | Confidence | Source | Notes |
|---|---|---|---|---|
| Cart badge | `page.locator("[data-test='shopping-cart-badge']")` | High | Source session — Inventory Page | Conditional; assertion is that the element is not visible / not present |

#### Locator Risks

- Cart badge is conditional; assertion should be "hidden" or "count = 0" rather than reading text.

#### Notes

- Needs clarification: confirm with product owner whether cart-clear on order completion is a contract or an implementation detail. If incidental, this scenario should remain a Medium follow-up; if contracted, promote to High.

---

### Scenario: Checkout information form rejects missing required fields

**Scenario ID:** TC-08
**Tags:** `@ui` `@checkout` `@negative` `@needs-clarification`
**Automation Priority:** Medium
**Priority Rationale:** Negative path was not exercised in the source session; validation rules are an Open Question. Worth automating once the requirement is confirmed.

#### Given

- The standard user is on the checkout information page with one item in the cart.

#### When

- The user submits the form with at least one required field blank.

#### Then

- The user remains on the checkout information page.
- A field-specific error message is displayed.

#### Test Data

| Field | Value | Source | Notes |
|---|---|---|---|
| First Name | (empty) | n/a | At least one required field left blank for this scenario. |
| Last Name | `User` | Tester-generated | |
| Zip/Postal Code | `12345` | Tester-generated | |

#### Observed Evidence

- Not exercised in this session. Source session lists this as a follow-up exploration (TC-08).

#### Automation Notes

| Element or Action | Locator Candidate | Confidence | Source | Notes |
|---|---|---|---|---|
| Error banner / per-field error | `page.locator("[data-test='error']")` | Medium | Source session — Checkout: Your Information | Conditional; locator inferred from the login error pattern, not observed on this page in source session |

#### Locator Risks

- Error message structure on the checkout information page has not been observed; the locator above is a hypothesis based on the demo's login error pattern and may need adjustment after a focused re-exploration.

#### Notes

- A focused `/explore-workflow` run is recommended to confirm validation behavior, field-specific error text, and locator before this scenario is automated.
