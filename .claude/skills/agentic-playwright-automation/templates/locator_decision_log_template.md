# Locator Decision Log: <Feature or Scenario>

## Purpose

This document records how locator candidates from exploration were reviewed and converted into final page object locators. It is the canonical place to explain accepted, modified, scoped, rejected, and needs-review decisions.

## Locator Strategy Reference

Preferred general order:

1. role/name
2. label
3. placeholder
4. text
5. test id / data-test
6. stable CSS
7. XPath only as a last resort

Practical exceptions:

- Use scoped locators or data-test locators for repeated elements.
- Use data-test locators for icon-only elements.
- Document dynamic or conditional element risks.

## Decisions

Decision values: Accepted, Accepted with Scope, Modified, Rejected, Needs Review.

| Page Object | Element | Candidate Locator | Final Locator | Decision | Rationale | Source |
|---|---|---|---|---|---|---|

## Rejected Candidates

| Element | Rejected Candidate | Reason | Replacement |
|---|---|---|---|

## Risks and Mitigations

| Page Object | Element | Risk | Mitigation |
|---|---|---|---|
