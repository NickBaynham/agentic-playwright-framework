# Feature: SauceDemo Standard User Login

## Business Goal

A standard user can sign in to the SauceDemo storefront and reach the product catalog so they can browse and purchase items.

## Source Material

- User story: "As a returning shopper, I want to log in so that I can see and order products."
- Acceptance criteria: Successful login lands the user on the products listing page.
- Exploration session: `cases/saucelabs.md` (TC-01)
- Browser/MCP observations: `.playwright-mcp/page-2026-05-21T18-33-55-546Z.yml`
- Related notes: `blogs/exploratory.md`

## Assumptions

- The `standard_user` account is enabled in the target environment.
- The site is reachable at `https://www.saucedemo.com/`.
- The same shared password (`secret_sauce`) is in use for demo accounts.

## Open Questions

- Should login redirect always be `/inventory.html`, or are there marketing or onboarding redirects in other environments?
- Is there a session timeout the test should respect?

## Potential Defects or Ambiguities

- None identified for the standard user login path.

## Scenarios

### Scenario: Standard user logs in successfully

**Scenario ID:** TC-001
**Tags:** `@ui` `@smoke` `@login` `@positive` `@automatable`
**Automation Priority:** High
**Priority Rationale:** Login is a prerequisite for every other purchase flow and is a core smoke check.

#### Given

- The user is on the SauceDemo login page.

#### When

- The user enters valid credentials and submits the login form.

#### Then

- The user is redirected to the inventory page.
- The Products header is visible.
- The shopping cart link is visible in the header.

#### Test Data

| Field | Value | Source | Notes |
|---|---|---|---|
| Username | standard_user | Login page hints | Public demo account |
| Password | secret_sauce | Login page hints | Shared across demo users |

#### Observed Evidence

- After clicking Login, the URL advanced to `https://www.saucedemo.com/inventory.html`.
- The page snapshot showed the Products heading and a shopping cart link with no badge.

#### Automation Notes

These notes are optional implementation hints carried forward from exploration. They are not final automation decisions.

| Element or Action | Locator Candidate | Confidence | Source | Notes |
|---|---|---|---|---|
| Username input | `page.get_by_placeholder("Username")` | High | saucedemo_checkout_exploration.md | Or `[data-test='username']` |
| Password input | `page.get_by_placeholder("Password")` | High | saucedemo_checkout_exploration.md | Or `[data-test='password']` |
| Login button | `page.get_by_role("button", name="Login")` | High | saucedemo_checkout_exploration.md | Or `[data-test='login-button']` |
| Products heading | `page.get_by_role("heading", name="Products")` | High | saucedemo_checkout_exploration.md | Inventory landing |
| Shopping cart link | `page.locator("[data-test='shopping-cart-link']")` | High | saucedemo_checkout_exploration.md | Icon-only; data-test is stable |

#### Locator Risks

- Shopping cart link has no accessible name on the anchor itself; rely on `data-test` rather than role/name.

#### Notes

- This scenario is the foundation for all checkout-related scenarios.
