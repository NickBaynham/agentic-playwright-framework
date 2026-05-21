# MCP Exploration Session: Standard User Checkout

## Session Metadata

| Field | Value |
|---|---|
| Application | SauceDemo |
| Target URL | https://www.saucedemo.com/ |
| Workflow | Standard user checkout (login -> add item -> checkout -> complete) |
| Tooling | Claude Code + Playwright MCP |
| Browser | Chromium (Playwright MCP default) |
| Date | 2026-05-21 |
| Tester | Claude Code agent, human-directed |

## Exploration Scope

A single-item happy-path checkout performed by the `standard_user` account:

1. Log in as `standard_user`.
2. Add Sauce Labs Backpack to the cart from the inventory page.
3. Open the cart and proceed to checkout.
4. Submit checkout information.
5. Confirm the order from the overview page.
6. Return to the inventory page from the order confirmation.

## Out of Scope

- Other user accounts (`locked_out_user`, `problem_user`, `performance_glitch_user`, `error_user`, `visual_user`).
- Multi-item carts.
- Sorting and filtering on the inventory page.
- Logout flow.
- Reset App State as a tested behavior (used only opportunistically as an anomaly observation).
- Payment processing (no real payment is required by this demo app).

## Assumptions

- Public demo credentials published on the landing page are intended for unrestricted exploratory use.
- The "Thank you for your order!" message on `/checkout-complete.html` is the success oracle for checkout.
- The cart badge counter is the success oracle for "item added to cart".

## Test Data Used

| Data Item | Value | Source | Notes |
|---|---|---|---|
| Username | `standard_user` | Published on saucedemo landing page | Public demo credential |
| Password | `secret_sauce` | Published on saucedemo landing page | Public demo credential |
| Product added | Sauce Labs Backpack | Tester choice | First item listed on inventory page |
| First name | `Test` | Tester input | Required by checkout step one |
| Last name | `User` | Tester input | Required by checkout step one |
| Postal code | `12345` | Tester input | Required by checkout step one |

## Pages Observed

### Login Page

**URL:** `https://www.saucedemo.com/`
**Purpose:** Authenticate a user into the SauceDemo storefront.

#### Observed Elements

- Username text field.
- Password text field.
- Login button.
- Accepted usernames list (visible on the page).
- Accepted password (visible on the page).

#### Actions Available

- Type into username field.
- Type into password field.
- Click Login.

#### Candidate Assertions

- Successful login redirects to `/inventory.html`.
- Page title or heading on the inventory page shows "Products".
- An incorrect login keeps the user on `/` and surfaces an error banner (not exercised here; candidate for follow-up).

#### Notes

- Credentials are published in plain text on the page itself; this is a known property of the demo app.

### Inventory Page

**URL:** `https://www.saucedemo.com/inventory.html`
**Purpose:** Browse products and add them to the cart.

#### Observed Elements

- Page heading "Products".
- Six product cards.
- Per-product "Add to cart" button.
- Cart icon in the header.
- Burger menu in the header.

#### Actions Available

- Click "Add to cart" for a product.
- Click cart icon to navigate to the cart.
- Open burger menu (not exercised in this session beyond observation).

#### Candidate Assertions

- "Add to cart" for Sauce Labs Backpack changes its button label to "Remove".
- Cart badge increments to `1` after adding the first item.
- Six product cards are present on first load.

#### Notes

- Product count is six on this demo as of the session date.

### Cart Page

**URL:** `https://www.saucedemo.com/cart.html`
**Purpose:** Review items selected for purchase before checkout.

#### Observed Elements

- Page heading "Your Cart".
- Row for Sauce Labs Backpack with quantity `1`.
- Continue Shopping button.
- Checkout button.

#### Actions Available

- Click Continue Shopping (returns to inventory).
- Click Checkout (proceeds to checkout information).
- Remove an item (not exercised here).

#### Candidate Assertions

- Cart page shows previously added Sauce Labs Backpack.
- Quantity column shows `1` for the added item.

#### Notes

- None.

### Checkout: Your Information

**URL:** `https://www.saucedemo.com/checkout-step-one.html`
**Purpose:** Collect shipping information from the user.

#### Observed Elements

- First Name text field.
- Last Name text field.
- Postal Code text field.
- Cancel button.
- Continue button.

#### Actions Available

- Type into First Name, Last Name, Postal Code.
- Click Cancel (returns to cart).
- Click Continue (proceeds to overview when all three fields are populated).

#### Candidate Assertions

- Submitting with all three fields populated proceeds to `/checkout-step-two.html`.
- Submitting with any field empty surfaces a field-specific error (candidate negative test; not exercised here).

#### Notes

- None.

### Checkout: Overview

**URL:** `https://www.saucedemo.com/checkout-step-two.html`
**Purpose:** Present the order for final confirmation.

#### Observed Elements

- Item rows summarizing the cart.
- Payment Information section.
- Shipping Information section.
- Price Total section with Item total, Tax, Total.
- Cancel button.
- Finish button.

#### Actions Available

- Click Cancel (returns to inventory page).
- Click Finish (completes the order).

#### Candidate Assertions

- Item total reflects the sum of item prices.
- Total reflects Item total plus Tax.
- Finish navigates to `/checkout-complete.html`.

#### Notes

- Tax appears to be calculated by the application; the exact formula is not documented in this exploration.

### Order Confirmation

**URL:** `https://www.saucedemo.com/checkout-complete.html`
**Purpose:** Confirm the order has been placed.

#### Observed Elements

- Heading "Checkout: Complete!" (or equivalent confirmation header).
- Body text "Thank you for your order!".
- Back Home button.

#### Actions Available

- Click Back Home (returns to inventory page).

#### Candidate Assertions

- Confirmation page displays "Thank you for your order!".
- Back Home returns to `/inventory.html`.

#### Notes

- None.

## Action Timeline

| Step | Action | Observed Result | Evidence | Notes |
|---:|---|---|---|---|
| 1 | Navigate to https://www.saucedemo.com/ | Login page rendered. | snapshot-01 | Initial load. |
| 2 | Type `standard_user` into Username field | Field populated. | snapshot-02 | |
| 3 | Type `secret_sauce` into Password field | Field populated. | snapshot-03 | |
| 4 | Click Login button | Redirected to `/inventory.html`; Products heading visible; six product cards visible. | snapshot-04 | |
| 5 | Click Add to cart on Sauce Labs Backpack | Button label changed to Remove; cart badge incremented to `1`. | snapshot-05 | |
| 6 | Click cart icon in header | Navigated to `/cart.html`; Sauce Labs Backpack row visible with quantity `1`. | snapshot-06 | |
| 7 | Click Checkout button | Navigated to `/checkout-step-one.html`; First Name, Last Name, Postal Code fields visible. | snapshot-07 | |
| 8 | Type `Test`, `User`, `12345` into the three fields | Fields populated. | snapshot-08 | |
| 9 | Click Continue button | Navigated to `/checkout-step-two.html`; item total, tax, and total visible. | snapshot-09 | |
| 10 | Click Finish button | Navigated to `/checkout-complete.html`; "Thank you for your order!" visible. | snapshot-10 | First Finish attempt in a prior session returned MCP success but no navigation; see Anomalies A-002 and Tooling Notes. |
| 11 | Click Back Home button | Navigated to `/inventory.html`; Products heading visible. | snapshot-11 | |

## Observed Outcomes

- Successful login as `standard_user` redirects to `/inventory.html`.
- Adding Sauce Labs Backpack changes its button to Remove and sets cart badge to `1`.
- The cart page lists the previously added item with quantity `1`.
- Checkout step one accepts first name, last name, and postal code.
- Checkout overview displays item total, tax, and total.
- Finish completes checkout and surfaces the confirmation page with "Thank you for your order!".
- Back Home returns to the inventory page.

## Anomalies and Risks

| ID | Type | Observation | Severity | Recommendation |
|---|---|---|---|---|
| A-001 | Application Behavior | Reset App State (burger menu) cleared underlying cart state but the "Remove" button on a previously added product still appeared as Remove until the page was reloaded. | Medium | Confirm whether Reset App State is documented to require a page reload to update visible button text. Possible UX inconsistency. |
| A-002 | Tooling Behavior | An MCP `browser_click` on the Finish button returned success but the React handler did not fire and the navigation did not occur. Re-taking a snapshot and using `browser_evaluate` to issue a DOM `.click()` triggered the expected navigation. | Medium | Treat as a Playwright MCP interaction limitation for this control. Record any reliance on the `browser_evaluate` fallback in Tooling Notes. |

## Candidate Test Cases

| Candidate ID | Title | Priority | Notes |
|---|---|---|---|
| TC-001 | Standard user logs in successfully | High | Smoke; observable redirect to `/inventory.html`. |
| TC-002 | Adding Sauce Labs Backpack updates button label and cart badge | High | Smoke; deterministic observable. |
| TC-003 | Cart page lists previously added item with quantity 1 | High | Smoke. |
| TC-004 | Checkout step one accepts valid first name, last name, postal code | High | Smoke; positive path. |
| TC-005 | Checkout overview displays item total, tax, and total | Medium | Tax formula not yet documented; candidate for clarification. |
| TC-006 | Finish completes checkout and displays "Thank you for your order!" | High | Smoke; primary success oracle. |
| TC-007 | Back Home returns user to inventory page | Medium | Navigation regression check. |
| TC-008 | Reset App State updates visible button text without requiring reload | Medium | Currently failing under observation; flag as Potential Defect candidate. |
| TC-009 | Login with empty credentials surfaces an error banner | Medium | Not exercised here; candidate negative test. |

## Candidate Page Models

### LoginPage

#### Actions

- `enterUsername(value)`
- `enterPassword(value)`
- `submitLogin()`

#### Elements

- Username field.
- Password field.
- Login button.

#### Data Needs

- Username.
- Password.

### InventoryPage

#### Actions

- `addProductToCartByName(name)`
- `openCart()`
- `openMenu()`

#### Elements

- Products heading.
- Product card per item.
- Cart badge.

#### Data Needs

- Product name.

### CartPage

#### Actions

- `proceedToCheckout()`
- `continueShopping()`
- `removeItemByName(name)`

#### Elements

- Item row per product.
- Quantity column.
- Checkout button.

#### Data Needs

- Optional product name for remove.

### CheckoutInformationPage

#### Actions

- `enterShippingInformation(firstName, lastName, postalCode)`
- `continueToOverview()`
- `cancelCheckout()`

#### Elements

- First Name, Last Name, Postal Code fields.
- Continue button.
- Cancel button.

#### Data Needs

- First name, last name, postal code.

### CheckoutOverviewPage

#### Actions

- `finishOrder()`
- `cancelOverview()`

#### Elements

- Item rows.
- Item total, Tax, Total.
- Finish button.

#### Data Needs

- None.

### OrderConfirmationPage

#### Actions

- `backHome()`

#### Elements

- Confirmation heading.
- "Thank you for your order!" message.
- Back Home button.

#### Data Needs

- None.

## Candidate Data Needs

| Data Need | Example Value | Source | Required? | Notes |
|---|---|---|---|---|
| Username | `standard_user` | Demo app | Yes | Public demo credential. |
| Password | `secret_sauce` | Demo app | Yes | Public demo credential. |
| Product to add | Sauce Labs Backpack | Tester | Yes | Any inventory item should work; backpack used as default. |
| First name | `Test` | Tester | Yes | Required by checkout step one. |
| Last name | `User` | Tester | Yes | Required by checkout step one. |
| Postal code | `12345` | Tester | Yes | Required by checkout step one. |

## Open Questions

- Is Reset App State expected to update visible button text without a reload?
- Is the tax on the overview page a fixed rate or computed from postal code or item subtotal?
- Should empty checkout fields surface field-specific errors or a single banner?
- Are there documented acceptance criteria for any of the candidate test cases above?

## Tooling Notes

- One MCP `browser_click` on the Finish button returned success without firing the React handler. Worked around with `browser_evaluate` issuing a DOM `.click()`. See anomaly A-002. Downstream automation should not rely on the workaround without an explicit reason.
- Snapshots were the primary observation mechanism; screenshots were not required.

## Recommended Next Step

Hand off this session report to the `exploratory-to-bdd` skill to generate Markdown BDD specs and Gherkin `.feature` files for the high-priority candidate cases (TC-001 through TC-006). Treat TC-008 as Needs Clarification until the Reset App State behavior is confirmed against a requirement.
