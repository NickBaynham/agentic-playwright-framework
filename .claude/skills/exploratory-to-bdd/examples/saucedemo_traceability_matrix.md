# Traceability Matrix: SauceDemo Standard User Login

| Case ID | Feature | Scenario | Source Type | Source Reference | Observed Evidence | Expected Outcome | Locator Candidate Reference | Locator Risk | Automation Priority | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TC-001 | SauceDemo Login | Standard user logs in successfully | MCP Session | `cases/saucelabs.md` TC-01, `.playwright-mcp/page-2026-05-21T18-33-55-546Z.yml` | URL advanced to `/inventory.html`, Products heading and cart link visible | User reaches the products page after login | saucedemo_checkout_exploration.md → LoginPage (Username, Password, Login button); InventoryPage (Products heading, Shopping cart link) | Cart link has no accessible name; use `data-test` | High | Ready | Core smoke case used as the entry point for all checkout scenarios |

## Status Legend

- **Draft** — Spec is in progress and not ready for review.
- **Ready** — Spec is reviewed and ready for execution or automation work.
- **Needs Review** — Spec needs another reviewer pass.
- **Needs Clarification** — Open questions block readiness.
- **Potential Defect** — Observed behavior may not match intended behavior.
- **Automated** — Scenario is covered by an automated test.
- **Do Not Automate** — Scenario should remain manual or exploratory.
