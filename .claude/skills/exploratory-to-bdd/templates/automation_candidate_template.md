# Automation Candidate Review: <Feature Name>

| Scenario ID | Scenario | Priority | Recommended Automation Type | Rationale | Risks | Notes |
|---|---|---|---|---|---|---|
| TC-001 | <Scenario name> | High / Medium / Low / Do Not Automate | Playwright UI / API / Unit / Integration / Manual / Do Not Automate / Needs Clarification | <Why this priority and type fit> | <Stability, data, or environment risks> | <Notes> |

## Priority Definitions

- **High** — Core smoke paths, business-critical transactions, stable workflows, high regression risk, security or money-related flows, scenarios that should run in CI.
- **Medium** — Useful regression coverage, moderate business value, flows that are mostly stable, scheduled or nightly test candidates.
- **Low** — Informational checks, exploratory observations, low-risk areas, UI areas likely to change, cases better suited for occasional review.
- **Do Not Automate** — Subjective visual inspection, unstable behavior, one-time exploratory observations, behavior without a clear expected result, unclear or disputed requirements.

## Recommended Automation Types

- Playwright UI
- API
- Unit
- Integration
- Manual
- Do Not Automate
- Needs Clarification
