# Locator Candidates: <Workflow Name>

## Purpose

This document records locator candidates observed during MCP exploration. These candidates are evidence for later automation design and are **not final implementation decisions**. Final locator decisions are made by the `agentic-playwright-automation` skill during page object creation.

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

- Use scoped locators or stable test IDs for repeated elements.
- Use data-test locators for icon-only elements or ambiguous controls.
- Document dynamic and conditional elements as locator risks.

## Candidates

| Page | Element | Type | Role | Accessible Name / Text | Placeholder / Label | Test ID / Data Attribute | Candidate Locator | Confidence | Rationale | Notes |
|---|---|---|---|---|---|---|---|---|---|---|

## Repeated or Dynamic Elements

| Page | Element Group | Locator Challenge | Suggested Strategy | Notes |
|---|---|---|---|---|

## Locator Risks

| Page | Element | Risk | Impact | Recommendation |
|---|---|---|---|---|

## Automation Handoff Summary

| Page | Element | Recommended Candidate | Confidence | Review Needed? |
|---|---|---|---|---|
