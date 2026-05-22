# Automation Candidate Review: Standard User Checkout

## Summary

This review classifies each scenario in `specs/bdd/markdown/standard_user_checkout.md` for automation suitability. Six scenarios (TC-01–TC-06) are recommended for High-priority automation as a smoke suite. Two scenarios (TC-07, TC-08) are Medium-priority and blocked by Open Questions; they should be reviewed by product before automation.

## Candidate Table

| Scenario ID | Title | Priority | Suggested Type | Tags | Rationale | Locator Candidate References | Locator Risks | Notes |
|---|---|---|---|---|---|---|---|---|
| TC-01 | Standard user logs in successfully | High | Playwright UI Automation Candidate | `@ui` `@smoke` `@login` `@positive` `@automatable` | Precondition for every other scenario; deterministic URL transition. | LoginPage: Username, Password, Login button; InventoryPage: Products listing | "Products" header is rendered as `generic`, not `heading` role. | Foundation; should be the first test implemented. |
| TC-02 | Adding one product updates the cart badge and toggles the Add button to Remove | High | Playwright UI Automation Candidate | `@ui` `@smoke` `@cart` `@positive` `@automatable` | Core add-to-cart behavior with deterministic badge text and button label observables. | InventoryPage: Backpack Add to cart, Backpack Remove, Cart badge | Repeated `Add to cart` text across six product cards; cart badge is conditional. | Use per-product `data-test` (`add-to-cart-<slug>` / `remove-<slug>`). TOOL-1 is an MCP-exploration anomaly only. |
| TC-03 | Cart page lists the added item with the correct name, quantity, and price | High | Playwright UI Automation Candidate | `@ui` `@smoke` `@cart` `@positive` `@automatable` | Confirms cart persistence between routes. | CartPage: Backpack cart line item, Checkout button | Cart row container has no per-item `data-test`; scoping required (filter `.cart_item` by product name). | |
| TC-04 | Checkout information form advances to the overview with valid input | High | Playwright UI Automation Candidate | `@ui` `@smoke` `@checkout` `@positive` `@automatable` | First branch of the checkout funnel; observable URL transition. | CheckoutInformationPage: First Name, Last Name, Postal Code, Continue | Postal code format rules not documented; non-empty values only. | |
| TC-05 | Overview page totals satisfy Item total + Tax = Total | High | Playwright UI Automation Candidate | `@ui` `@smoke` `@checkout` `@positive` `@automatable` | Catches pricing-display regressions independently of the exact tax rate. | CheckoutOverviewPage: Item total label, Tax label, Total label | Numeric content is dynamic; parse rather than exact-match. | Assert relational identity, not exact tax value. |
| TC-06 | Finishing the order shows the order confirmation page | High | Playwright UI Automation Candidate | `@ui` `@smoke` `@checkout` `@positive` `@automatable` | End-to-end success oracle for the checkout flow. | CheckoutOverviewPage: Finish button; CheckoutCompletePage: Thank-you heading | None observed. | |
| TC-07 | Cart is empty after order completion | Medium | Exploratory Follow-Up | `@ui` `@cart` `@positive` `@needs-clarification` | Behavior is inferred; no documented requirement that cart must be cleared on order completion. | InventoryPage: Cart badge (assert hidden) | Cart badge is conditional. | Confirm with product owner whether cart-clear is contracted. Promote to High once clarified. |
| TC-08 | Checkout information form rejects missing required fields | Medium | Exploratory Follow-Up, Playwright UI Automation Candidate | `@ui` `@checkout` `@negative` `@needs-clarification` | Negative path not exercised in source session; validation rules unknown. | CheckoutInformationPage form fields; Error banner (hypothesized) | Error element structure not observed on this page. | Run a focused `/explore-workflow` against `/checkout-step-one.html` before automating. |

## Out-of-Feature Candidates

These items were captured in the source session report but belong to other features and are not included in this BDD spec:

| Source ID | Title | Recommended Home | Notes |
|---|---|---|---|
| TC-09 | Shopping cart link has an accessible name | Accessibility audit (separate feature) | Tied to Anomaly APP-1. Needs an accessibility requirement to evaluate. |
| TC-10 | Telemetry endpoint placeholders are replaced before deployment | Environment / deployment review (separate feature) | Tied to Anomaly APP-2. Configuration concern, not a functional flow. |

## Recommended Smoke Suite

The smallest reviewable smoke suite that covers the end-to-end happy path:

1. TC-01 (login)
2. TC-02 (add to cart)
3. TC-03 (cart contents)
4. TC-04 (checkout information)
5. TC-05 (overview totals)
6. TC-06 (order confirmation)

These six scenarios, run in order, cover every page in the source session and exercise every High-priority observable outcome.

## Risks and Open Questions Carried Forward

- TC-05 / TC-07 depend on Open Questions about tax-rate stability and the post-order cart-clear contract. Defaults proposed: relational identity assertion for TC-05; hidden-badge assertion for TC-07 (Medium until confirmed).
- TC-08 depends on a focused re-exploration to characterize validation behavior and error locators.
- Accessibility (APP-1, TC-09) and telemetry configuration (APP-2, TC-10) are tracked separately.
- TOOL-1 (MCP click reliability) is not expected to affect Playwright-Python automation, but downstream reviewers should monitor for similar reliability issues on the same controls when tests are first run.
