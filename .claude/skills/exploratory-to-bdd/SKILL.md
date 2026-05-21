---
name: exploratory-to-bdd
description: Convert exploratory testing notes, Playwright MCP exploration sessions, user stories, acceptance criteria, and manual test observations into structured BDD specifications. Produces Markdown BDD specs, Gherkin .feature files, traceability matrices, automation priority recommendations, and BDD quality reviews. Does not generate Playwright/PyTest automation code in v0.1.
---

# Exploratory to BDD

Version 0.1

## Purpose

Convert raw testing artifacts — exploratory session notes, Playwright MCP browser observations, user stories, acceptance criteria, manual test cases, and bug reproduction notes — into structured, reviewable BDD specifications. The skill prioritizes traceability, separation of observed versus intended behavior, and explicit identification of ambiguity, so the resulting specs are safe inputs for downstream automation.

## When to Use This Skill

Use this skill when the input is any of the following and the desired output is reviewable BDD documentation:

- Playwright MCP exploration notes
- browser snapshots
- exploratory testing transcripts
- user stories
- acceptance criteria
- manual testing notes
- bug reproduction notes
- product behavior observations
- existing informal test cases

Do not use this skill to generate Playwright or PyTest automation code; that is out of scope for v0.1.

## Inputs

- Free-form exploration notes (Markdown, text, or chat transcripts).
- Playwright MCP session artifacts (snapshots, console logs, navigation traces).
- User stories and acceptance criteria.
- Manual test cases (Markdown or other structured formats).
- Bug reports and reproduction steps.

## Outputs

- Markdown BDD specs.
- Gherkin `.feature` files.
- Traceability matrices.
- Automation candidate reviews.
- BDD quality review reports.

## Core Principles

1. Separate observed behavior from intended behavior.
2. Do not invent requirements.
3. Do not silently convert observed behavior into expected behavior if the requirement is unclear.
4. Preserve traceability to source observations, user stories, or acceptance criteria.
5. Prefer user-centered language over implementation details.
6. Keep scenarios focused on one behavior.
7. Use Gherkin for behavior, not technical implementation.
8. Use Scenario Outlines when the same behavior should be tested with multiple data sets.
9. Mark ambiguous behavior as an open question.
10. Mark suspected product issues as potential defects.
11. Include automation priority and rationale.
12. Do not generate Playwright/PyTest code in this skill version.
13. Do not generate step definitions in this skill version.
14. Do not introduce Cucumber/Behave runtime setup in this skill version.
15. Keep BDD specs useful for product, QA, engineering, and automation review.

## Required Output Structure

Write all generated artifacts under the project's `specs/` directory using this layout:

```
specs/
  bdd/
    features/
      <feature_name>.feature
    markdown/
      <feature_name>.md
    traceability/
      <feature_name>_traceability_matrix.md
    reviews/
      <feature_name>_bdd_quality_review.md
    automation/
      <feature_name>_automation_candidates.md
```

Create the directories if they do not already exist. Use `snake_case` for feature names.

## Markdown BDD Spec Rules

- Follow `templates/markdown_bdd_spec_template.md` exactly.
- Always populate Business Goal, Source Material, Assumptions, Open Questions, and Potential Defects sections — use "None identified" when nothing applies.
- Each scenario must have a unique Scenario ID, tags, Automation Priority, and Priority Rationale.
- Each scenario must include Test Data and Observed Evidence even when one of those is empty (use "Not applicable" rather than removing the section).
- Tie every scenario to a row in the traceability matrix using its Scenario ID.

## Gherkin Feature Rules

- Follow `templates/gherkin_feature_template.feature`.
- Use `Feature`, `Background`, `Scenario`, `Scenario Outline`, and `Examples` keywords.
- Do not include low-level selectors (CSS, XPath, `data-test`) in Gherkin steps.
- Do not include implementation details unless behavior cannot be expressed otherwise.
- Avoid long click-by-click scenarios when a business-level step is clearer.
- Avoid vague outcomes like "it works" or "the app behaves correctly."
- Keep scenario names concise and behavior-focused.
- Use tags consistently. Recommended tags:
  - `@ui`, `@api`
  - `@smoke`, `@regression`
  - `@negative`, `@positive`
  - `@checkout`, `@login`, `@cart`, `@search`
  - `@exploratory`, `@automatable`, `@manual-review`
  - `@needs-clarification`, `@potential-defect`

## Traceability Matrix Rules

- Follow `templates/traceability_matrix_template.md`.
- Every scenario in the Markdown spec must appear in the matrix.
- Use the following Status values: Draft, Ready, Needs Review, Needs Clarification, Potential Defect, Automated, Do Not Automate.
- Source References must point to a real file, URL, ticket, or session note.

## Automation Priority Rules

- Classify each scenario as High, Medium, Low, or Do Not Automate.
- High: core smoke paths, business-critical transactions, stable workflows, high regression risk, security or money-related flows, scenarios that should run in CI.
- Medium: useful regression coverage, moderate business value, mostly stable flows, scheduled or nightly test candidates.
- Low: informational checks, exploratory observations, low-risk areas, UI areas likely to change, cases better suited for occasional review.
- Do Not Automate: subjective visual inspection, unstable behavior, one-time exploratory observations, behavior without a clear expected result, unclear or disputed requirements.
- Always include a one-line Priority Rationale.

## Potential Defect and Ambiguity Rules

- If observed behavior conflicts with stated acceptance criteria, document it under Potential Defects in the Markdown spec.
- Tag any related scenario with `@potential-defect`.
- If a requirement is unclear, add an Open Question and tag the scenario with `@needs-clarification`.
- Never resolve ambiguity by guessing. Surface it instead.

## BDD Quality Review Rules

- Follow `templates/bdd_quality_review_template.md`.
- Apply every item in `checklists/bdd_quality_checklist.md`.
- Mark each check Pass, Fail, or Needs Review.
- File the review under `specs/bdd/reviews/<feature_name>_bdd_quality_review.md`.
- End with an Approval Recommendation: Approved, Approved with Changes, or Needs Rework.

## Workflow: Exploration Notes to BDD

1. Read the exploration source (Markdown notes, MCP transcript, manual session log).
2. Identify discrete user-facing behaviors and group them into features.
3. For each feature, draft the Markdown BDD spec using the template.
4. Convert each scenario into Gherkin and emit the `.feature` file.
5. Build the traceability matrix linking every scenario to its source.
6. Build the automation candidate review.
7. Run the BDD quality review and write the report.

## Workflow: User Story to BDD

1. Read the user story and any attached acceptance criteria.
2. Convert acceptance criteria into one or more scenarios.
3. Add Assumptions for anything implied but not stated.
4. Add Open Questions for anything missing.
5. Generate Markdown spec, `.feature` file, traceability matrix, automation candidates, and quality review.

## Workflow: BDD Review

1. Read the existing Markdown spec and/or `.feature` file.
2. Apply the BDD quality checklist.
3. Apply the ambiguity and defect checklist.
4. Identify duplicate, overlapping, broad, or vague scenarios.
5. Recommend revisions and update the review file under `specs/bdd/reviews/`.

## Workflow: BDD MCP Execution

1. Read the selected BDD spec or `.feature` file.
2. For each scenario, use Playwright MCP tools (`browser_navigate`, `browser_snapshot`, `browser_click`, `browser_fill_form`, `browser_evaluate`) to execute the steps against a live environment.
3. Record pass/fail per scenario and any observed deviations.
4. Write an execution report under `reports/bdd-mcp-execution/<feature_name>_<timestamp>.md`.
5. Do not modify the BDD spec unless explicitly asked.

## What This Skill Does Not Do in v0.1

Included:

- Convert exploration notes to Markdown BDD specs.
- Convert exploration notes to Gherkin `.feature` files.
- Generate traceability matrix.
- Classify automation priority.
- Identify open questions.
- Identify possible defects.
- Review BDD scenario quality.
- Support MCP-based manual scenario execution through command instructions.

Not included:

- Playwright or PyTest code generation.
- Cucumber/Behave runtime setup.
- Step definition generation.
- Jira integration.
- GitHub issue creation.
- Automatic defect filing.
- BDD linter implementation.

## Final Review Checklist

Before returning generated artifacts:

- Markdown BDD spec follows the template.
- Every scenario has a Scenario ID, tags, Automation Priority, and rationale.
- Gherkin file is syntactically valid and free of selectors or implementation detail.
- Traceability matrix includes every scenario and points to a real source.
- Automation candidate review classifies each scenario.
- BDD quality review is filed with an Approval Recommendation.
- Open questions and potential defects are surfaced, not silently resolved.
- No Playwright or PyTest automation code is included.
