# Exploration Anomaly Report: Standard User Checkout

| ID | Type | Observation | Evidence | Severity | Impact | Recommendation | Status |
|---|---|---|---|---|---|---|---|
| A-001 | Application Behavior | Reset App State (burger menu) cleared underlying cart state, but the "Remove" button on a previously added product remained labeled "Remove" until the page was reloaded. | snapshot-reset-before, snapshot-reset-after | Medium | Misleading visual state; a returning user could believe the item is still in the cart. | Confirm whether Reset App State is documented to require a reload before button text updates. If not, treat as Potential Defect. | Needs Review |
| A-002 | Tooling Behavior | A Playwright MCP `browser_click` on the Finish button on `/checkout-step-two.html` returned success, but the React handler did not fire and navigation to `/checkout-complete.html` did not occur. Re-taking a snapshot and issuing a DOM `.click()` through `browser_evaluate` triggered the expected navigation. | snapshot-finish-noop, snapshot-finish-after-evaluate | Medium | False sense of action completion in MCP-driven sessions for this specific control. | Treat as a Playwright MCP interaction limitation for this control. Document use of the `browser_evaluate` fallback in Tooling Notes. Downstream automation should not depend on this workaround. | Tooling Limitation |
| A-003 | Application Behavior | Tax line on the overview page was present but the calculation formula was not documented in any visible copy. | snapshot-overview | Low | Cannot author a precise assertion on tax value without a requirement. | Surface as Open Question. Either obtain the tax rule or assert presence of a Tax line only. | Open |

## Anomaly Type Values

- Application Behavior
- Tooling Behavior
- Environment
- Data
- Usability
- Accessibility
- Performance Observation
- Unknown

## Severity Values

- Low
- Medium
- High
- Critical
- Needs Clarification

## Status Values

- Open
- Needs Review
- Clarified
- Potential Defect
- Tooling Limitation
- Closed
