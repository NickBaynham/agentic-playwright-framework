# Candidate Test Ideas: Standard User Checkout

| Candidate ID | Title | Behavior Area | Priority | Suggested Type | Rationale | Locator References | Notes |
|---|---|---|---|---|---|---|---|
| TC-001 | Standard user logs in successfully | Authentication | High | BDD Spec | Smoke path; observable redirect to `/inventory.html`. | LoginPage: Username input, Password input, Login button | Source: snapshot-04 |
| TC-002 | Adding Sauce Labs Backpack updates button label and cart badge | Cart | High | BDD Spec | Smoke path; deterministic observables (button text "Remove", cart badge `1`). | InventoryPage: Backpack Add to cart, Backpack Remove, Cart badge | Source: snapshot-05. Locator risk: repeated Add to cart buttons |
| TC-003 | Cart page lists previously added item with quantity 1 | Cart | High | BDD Spec | Smoke path; verifies cart hand-off from inventory. | CartPage: Cart line item (Backpack), Your Cart heading | Source: snapshot-06 |
| TC-004 | Checkout step one accepts valid first name, last name, postal code | Checkout | High | BDD Spec | Positive path; gates progression to overview. | CheckoutInformationPage: First Name, Last Name, Postal Code, Continue button | Source: snapshot-08, snapshot-09 |
| TC-005 | Checkout overview displays item total, tax, and total | Checkout | Medium | BDD Spec | Observable but tax rule undocumented; assert presence rather than value pending requirement. | CheckoutOverviewPage: Item total label, Tax label, Total label | See anomaly A-003 |
| TC-006 | Finish completes checkout and displays "Thank you for your order!" | Checkout | High | BDD Spec | Primary success oracle for checkout. | CheckoutOverviewPage: Finish button; OrderConfirmationPage: Thank-you message | See anomaly A-002 for known tooling caveat |
| TC-007 | Back Home returns user to inventory page | Navigation | Medium | BDD Spec | Navigation regression check after order completion. | OrderConfirmationPage: Back Home button | Source: snapshot-11 |
| TC-008 | Reset App State updates visible button text without requiring reload | App State | Needs Clarification | Defect Investigation | Observed behavior conflicts with reasonable user expectation; no requirement available. | InventoryPage: Backpack Add/Remove (toggle) | See anomaly A-001 |
| TC-009 | Login with empty credentials surfaces an error banner | Authentication | Medium | Exploratory Follow-Up | Negative path not exercised in this session; candidate for a targeted follow-up exploration. | LoginPage: Error banner (conditional, not observed) | Not yet observed |

## Priority Values

- High
- Medium
- Low
- Needs Clarification

## Suggested Type Values

- BDD Spec
- Exploratory Follow-Up
- Playwright UI Automation Candidate
- API Automation Candidate
- Manual Review
- Defect Investigation
- Do Not Automate
