# MCP Exploration Session: <Workflow Name>

## Session Metadata

| Field | Value |
|---|---|
| Application | <Application name> |
| Target URL | <URL> |
| Workflow | <Workflow name> |
| Tooling | Claude Code + Playwright MCP |
| Browser | <Browser> |
| Date | <Date> |
| Tester | Claude Code agent, human-directed |

## Exploration Scope

<Describe what is in scope.>

## Out of Scope

<Describe what is intentionally not explored.>

## Assumptions

- <Assumption 1>
- <Assumption 2>

## Test Data Used

| Data Item | Value | Source | Notes |
|---|---|---|---|

## Pages Observed

### <Page Name>

**URL:** `<URL or path>`
**Purpose:** <Observed purpose of page>

#### Observed Elements

- <Element 1>
- <Element 2>

#### Actions Available

- <Action 1>
- <Action 2>

#### Candidate Assertions

- <Assertion idea 1>
- <Assertion idea 2>

#### Locator Candidates

These are exploration evidence, not final implementation decisions.

| Element | Type | Role | Accessible Name / Text | Placeholder / Label | Test ID / Data Attribute | Candidate Locator | Confidence | Rationale | Notes |
|---|---|---|---|---|---|---|---|---|---|

#### Locator Risks

- <Risk 1>
- <Risk 2>

#### Repeated or Dynamic Elements

| Element Group | Locator Challenge | Suggested Strategy | Notes |
|---|---|---|---|

#### Notes

- <Notes>

## Action Timeline

| Step | Action | Observed Result | Evidence | Notes |
|---:|---|---|---|---|

## Observed Outcomes

- <Outcome 1>
- <Outcome 2>

## Anomalies and Risks

| ID | Type | Observation | Severity | Recommendation |
|---|---|---|---|---|

## Candidate Test Cases

| Candidate ID | Title | Priority | Notes |
|---|---|---|---|

## Candidate Page Models

### <Page Model Name>

#### Actions

- <Action 1>
- <Action 2>

#### Elements

- <Element 1>
- <Element 2>

#### Data Needs

- <Data need 1>
- <Data need 2>

## Candidate Data Needs

| Data Need | Example Value | Source | Required? | Notes |
|---|---|---|---|---|

## Open Questions

- <Question 1>
- <Question 2>

## Tooling Notes

- <Playwright MCP issue, fallback, or limitation>

## Automation Handoff Notes

These notes summarize the locator and page-model evidence carried forward into the BDD and automation phases. They are not final implementation decisions.

### Recommended Page Models

- <PageModelName>

### Locator Candidates to Review

| Page | Element | Candidate Locator | Confidence | Notes |
|---|---|---|---|---|

### Locator Risks

- <Risk 1>
- <Risk 2>

### Data Dependencies for Locators

| Element or Action | Data Dependency | Notes |
|---|---|---|

### Tooling Interaction Notes

- <Tooling note, such as MCP click fallback>

## Recommended Next Step

<Example: Convert high-priority candidate cases into BDD specs using the exploratory-to-bdd skill.>
