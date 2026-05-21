# Role
You are a senior QA automation architect, BDD test designer, and Claude Code configuration specialist.
# Goal
Create a reusable Claude Code skill named `exploratory-to-bdd` plus supporting Claude Code slash commands. This skill will help convert exploratory testing notes, Playwright MCP browser exploration sessions, user stories, acceptance criteria, and manual test observations into structured BDD specifications.
The skill must support both:
1. Human-readable Markdown BDD specs
2. Gherkin `.feature` files
The skill must also generate:
- traceability matrices
- open questions
- automation priority recommendations
- potential defect notes
- BDD quality review reports
This is version `v0.1` of the skill. Keep it focused on BDD generation and review. Do not implement Playwright automation code generation yet.
---
# Project Context
This repository is part of an agentic testing workflow.
The intended workflow is:
```text
Playwright MCP browser exploration
    ↓
Exploratory session notes
    ↓
exploratory-to-bdd skill
    ↓
Markdown BDD specs
    ↓
Gherkin .feature files
    ↓
Traceability matrix
    ↓
BDD quality review
    ↓
Future conversion to Playwright/PyTest automation

The skill should support this project thesis:

Claude Code should not simply generate tests directly from vague requirements. It should first help explore the application, capture observed behavior, convert that behavior into reviewable BDD specifications, identify ambiguity, preserve traceability, and recommend which scenarios are good candidates for automation.

⸻

Required Folder Structure

Create the following Claude Code skill and command structure:

.claude/
  skills/
    exploratory-to-bdd/
      SKILL.md
      templates/
        markdown_bdd_spec_template.md
        gherkin_feature_template.feature
        traceability_matrix_template.md
        bdd_quality_review_template.md
        automation_candidate_template.md
      examples/
        saucedemo_login.md
        saucedemo_login.feature
        saucedemo_traceability_matrix.md
        saucedemo_bdd_quality_review.md
      checklists/
        bdd_quality_checklist.md
        automation_candidate_checklist.md
        ambiguity_and_defect_checklist.md
  commands/
    explore-to-bdd.md
    generate-bdd.md
    review-bdd.md
    execute-bdd-mcp.md

If any directories do not exist, create them.

⸻

Skill Purpose

Create .claude/skills/exploratory-to-bdd/SKILL.md.

The skill must explain that it should be used when converting any of the following into BDD specs:

* Playwright MCP exploration notes
* browser snapshots
* exploratory testing transcripts
* user stories
* acceptance criteria
* manual testing notes
* bug reproduction notes
* product behavior observations
* existing informal test cases

The skill should produce structured, reviewable BDD artifacts that can later be converted into automated tests.

⸻

Core Skill Principles

The SKILL.md must enforce these principles:

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

⸻

BDD Output Structure

The skill must standardize the output structure.

When generating BDD specs, write outputs under:

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

The skill must support generating all of these files when requested.

⸻

Markdown BDD Spec Requirements

Create template file:

.claude/skills/exploratory-to-bdd/templates/markdown_bdd_spec_template.md

The Markdown BDD spec must include:

# Feature: <Feature Name>
## Business Goal
<Plain-language goal of the feature.>
## Source Material
- User story:
- Acceptance criteria:
- Exploration session:
- Browser/MCP observations:
- Related notes:
## Assumptions
- <Assumption 1>
- <Assumption 2>
## Open Questions
- <Question 1>
- <Question 2>
## Potential Defects or Ambiguities
- <Issue 1>
- <Issue 2>
## Scenarios
### Scenario: <Scenario Name>
**Scenario ID:** <ID>  
**Tags:** `@ui` `@smoke` `@regression` `@automatable`  
**Automation Priority:** High | Medium | Low | Do Not Automate  
**Priority Rationale:** <Reason>
#### Given
- <Precondition or starting state>
#### When
- <User action or trigger>
#### Then
- <Expected outcome>
#### Test Data
| Field | Value | Source | Notes |
|---|---|---|---|
#### Observed Evidence
- <Observation from MCP/browser/session notes>
#### Notes
- <Additional context>

⸻

Gherkin Feature Requirements

Create template file:

.claude/skills/exploratory-to-bdd/templates/gherkin_feature_template.feature

The .feature files must follow this general format:

@feature_tag
Feature: <Feature Name>
  <Business goal or feature description.>
  Background:
    Given <shared precondition>
  @ui @smoke @automatable
  Scenario: <Scenario name>
    Given <starting condition>
    When <user action>
    Then <expected result>
    And <additional expected result>
  @ui @regression @automatable
  Scenario Outline: <Scenario outline name>
    Given <starting condition>
    When <user performs action with "<data_field>">
    Then <expected result>
    Examples:
      | data_field |
      | value      |

Gherkin rules:

* Use Feature, Background, Scenario, Scenario Outline, and Examples.
* Do not include low-level selectors in Gherkin steps.
* Do not include implementation details unless needed to clarify behavior.
* Do not write overly long click-by-click scenarios when a business-level step is clearer.
* Avoid vague outcomes like “it works” or “the app behaves correctly.”
* Prefer clear expected results.
* Keep scenario names concise and behavior-focused.
* Use tags consistently.

Recommended tags:

@ui
@api
@smoke
@regression
@negative
@positive
@checkout
@login
@cart
@search
@exploratory
@automatable
@manual-review
@needs-clarification
@potential-defect

⸻

Traceability Matrix Requirements

Create template file:

.claude/skills/exploratory-to-bdd/templates/traceability_matrix_template.md

The traceability matrix must use this structure:

# Traceability Matrix: <Feature Name>
| Case ID | Feature | Scenario | Source Type | Source Reference | Observed Evidence | Expected Outcome | Automation Priority | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|
| TC-001 | Login | Standard user logs in | MCP Session | sessions/saucedemo-exploration.md | Login redirected to /inventory.html | Inventory page is displayed | High | Ready | Core smoke case |

Status values:

Draft
Ready
Needs Review
Needs Clarification
Potential Defect
Automated
Do Not Automate

⸻

Automation Candidate Requirements

Create template file:

.claude/skills/exploratory-to-bdd/templates/automation_candidate_template.md

The automation candidate output must classify scenarios as:

High
Medium
Low
Do Not Automate

Classification rules:

High

Use for:

* core smoke paths
* business-critical transactions
* stable workflows
* high regression risk
* security or money-related flows
* scenarios that should run in CI

Medium

Use for:

* useful regression coverage
* moderate business value
* flows that are mostly stable
* scenarios useful for scheduled or nightly tests

Low

Use for:

* informational checks
* exploratory observations
* low-risk areas
* UI areas likely to change
* cases better suited for occasional review

Do Not Automate

Use for:

* subjective visual inspection
* unstable behavior
* one-time exploratory observations
* behavior without a clear expected result
* unclear or disputed requirements

The automation candidate file must include:

# Automation Candidate Review: <Feature Name>
| Scenario ID | Scenario | Priority | Recommended Automation Type | Rationale | Risks | Notes |
|---|---|---|---|---|---|---|

Recommended automation types:

Playwright UI
API
Unit
Integration
Manual
Do Not Automate
Needs Clarification

⸻

BDD Quality Review Requirements

Create template file:

.claude/skills/exploratory-to-bdd/templates/bdd_quality_review_template.md

The quality review must check:

* Are scenarios focused on one behavior?
* Are Given/When/Then steps logically ordered?
* Are expected outcomes clear and testable?
* Are assumptions listed?
* Are open questions listed?
* Are observed behavior and intended behavior separated?
* Are potential defects identified?
* Is test data identified?
* Is automation priority justified?
* Is traceability preserved?
* Are scenarios free from unnecessary implementation detail?
* Are there duplicate or overlapping scenarios?
* Are any scenarios too broad?
* Are any scenarios too vague?

The output structure must be:

# BDD Quality Review: <Feature Name>
## Summary
<Overall assessment.>
## Review Results
| Check | Status | Notes |
|---|---|---|
| Scenarios are focused | Pass/Fail/Needs Review |  |
| Expected outcomes are clear | Pass/Fail/Needs Review |  |
| Observed vs intended behavior is separated | Pass/Fail/Needs Review |  |
| Traceability is preserved | Pass/Fail/Needs Review |  |
| Automation priority is justified | Pass/Fail/Needs Review |  |
## Issues Found
| Issue | Severity | Recommendation |
|---|---|---|
## Recommended Revisions
- <Revision 1>
- <Revision 2>
## Approval Recommendation
Approved | Approved with Changes | Needs Rework

⸻

Checklists

Create the following checklist files.

.claude/skills/exploratory-to-bdd/checklists/bdd_quality_checklist.md

Include checks for:

* clear feature name
* business goal
* scenario focus
* clear Given/When/Then
* no vague assertions
* no invented requirements
* no hidden assumptions
* test data identified
* traceability preserved
* open questions captured
* defects separated from specs
* automation priority included

.claude/skills/exploratory-to-bdd/checklists/automation_candidate_checklist.md

Include checks for:

* business criticality
* stability
* repeatability
* regression value
* deterministic expected result
* data availability
* CI suitability
* maintenance risk
* whether API-level testing would be better than UI
* whether manual testing is more appropriate

.claude/skills/exploratory-to-bdd/checklists/ambiguity_and_defect_checklist.md

Include checks for:

* observed behavior differs from expected behavior
* expected behavior is not provided
* UI behavior appears inconsistent
* state changes are delayed or unclear
* data requirements are unknown
* user roles are unclear
* error handling is undefined
* behavior depends on environment
* product terminology is ambiguous
* suspected product defect should be documented separately

⸻

Example Artifacts

Create example files using the SauceDemo login flow.

.claude/skills/exploratory-to-bdd/examples/saucedemo_login.md

Include a Markdown BDD spec for successful login.

.claude/skills/exploratory-to-bdd/examples/saucedemo_login.feature

Include a Gherkin feature for successful login.

.claude/skills/exploratory-to-bdd/examples/saucedemo_traceability_matrix.md

Include at least one row mapping the login scenario to an MCP exploration source.

.claude/skills/exploratory-to-bdd/examples/saucedemo_bdd_quality_review.md

Include a short sample quality review.

Use these observed facts:

* Target app: SauceDemo
* URL: https://www.saucedemo.com/
* Standard username: standard_user
* Password: secret_sauce
* Successful login redirects to /inventory.html
* Inventory page displays Products
* Shopping cart link is visible

Do not include automation code.

⸻

Slash Commands

Create the following command files.

⸻

.claude/commands/explore-to-bdd.md

Purpose:

Use this command when the user wants to explore an application with Playwright MCP and then generate BDD specs.

Command behavior:

1. Use Playwright MCP if available.
2. Open the target URL supplied by the user.
3. Explore only the scope requested by the user.
4. Record observed pages, actions, outcomes, data needs, and anomalies.
5. Generate BDD Markdown and .feature specs.
6. Generate a traceability matrix.
7. Generate automation candidate review.
8. Generate BDD quality review.
9. Do not generate Playwright test automation code.

The command should accept arguments such as:

/explore-to-bdd <target-url> <scope-or-user-story>

The command file should include this instruction:

Use the exploratory-to-bdd skill. If the user has not provided enough scope, inspect only the smallest obvious workflow and clearly document assumptions and open questions.

⸻

.claude/commands/generate-bdd.md

Purpose:

Use this command when exploration notes, user stories, or acceptance criteria already exist and should be converted into BDD specs.

Command behavior:

1. Read the provided source file or text.
2. Identify features, scenarios, assumptions, data needs, and expected outcomes.
3. Generate Markdown BDD specs.
4. Generate Gherkin .feature files.
5. Generate traceability matrix.
6. Generate automation candidate review.
7. Generate BDD quality review.
8. Do not generate automation code.

The command should accept:

/generate-bdd <source-file-or-description>

⸻

.claude/commands/review-bdd.md

Purpose:

Use this command to review existing BDD specs for quality, ambiguity, traceability, and automation readiness.

Command behavior:

1. Read existing Markdown BDD specs and/or .feature files.
2. Apply the BDD quality checklist.
3. Identify ambiguity, duplication, broad scenarios, missing test data, vague expected outcomes, and invented requirements.
4. Recommend revisions.
5. Update or create a BDD quality review file under:

specs/bdd/reviews/

The command should accept:

/review-bdd <bdd-file-or-folder>

⸻

.claude/commands/execute-bdd-mcp.md

Purpose:

Use this command when the user wants Claude to execute BDD scenarios manually through Playwright MCP without writing automation code.

Command behavior:

1. Read the selected BDD spec or feature file.
2. Use Playwright MCP to execute scenarios through the browser.
3. Record pass/fail status.
4. Capture observed behavior.
5. Identify deviations from expected behavior.
6. Generate an execution report under:

reports/bdd-mcp-execution/

7. Do not generate Playwright/PyTest automation code.
8. Do not modify the BDD spec unless explicitly asked.

The command should accept:

/execute-bdd-mcp <bdd-file-or-folder> <target-url>

⸻

SKILL.md Content Requirements

The SKILL.md must include these sections:

# Exploratory to BDD
## Purpose
## When to Use This Skill
## Inputs
## Outputs
## Core Principles
## Required Output Structure
## Markdown BDD Spec Rules
## Gherkin Feature Rules
## Traceability Matrix Rules
## Automation Priority Rules
## Potential Defect and Ambiguity Rules
## BDD Quality Review Rules
## Workflow: Exploration Notes to BDD
## Workflow: User Story to BDD
## Workflow: BDD Review
## Workflow: BDD MCP Execution
## What This Skill Does Not Do in v0.1
## Final Review Checklist

⸻

Version Scope

This is exploratory-to-bdd version 0.1.

Include this explicitly in SKILL.md.

Included in v0.1

* Convert exploration notes to Markdown BDD specs
* Convert exploration notes to Gherkin .feature files
* Generate traceability matrix
* Classify automation priority
* Identify open questions
* Identify possible defects
* Review BDD scenario quality
* Support MCP-based manual scenario execution through command instructions

Not included in v0.1

* Playwright/PyTest code generation
* Cucumber/Behave runtime setup
* step definition generation
* Jira integration
* GitHub issue creation
* automatic defect filing
* BDD linter implementation

⸻

Acceptance Criteria

After implementation:

1. The .claude/skills/exploratory-to-bdd/ folder exists.
2. The skill has a complete SKILL.md.
3. Template files exist for:
    * Markdown BDD specs
    * Gherkin feature files
    * traceability matrix
    * BDD quality review
    * automation candidate review
4. Checklist files exist for:
    * BDD quality
    * automation candidate review
    * ambiguity and defect review
5. Example SauceDemo files exist.
6. Command files exist for:
    * explore-to-bdd
    * generate-bdd
    * review-bdd
    * execute-bdd-mcp
7. The commands instruct Claude to use the exploratory-to-bdd skill.
8. The skill clearly enforces separation of observed behavior and expected behavior.
9. The skill clearly states that it does not generate Playwright/PyTest automation code in v0.1.
10. The output is documentation-only: Markdown, .feature, and command instruction files.
11. The final response must summarize:
    * files created
    * purpose of the skill
    * available commands
    * how to use the skill in the exploratory testing workflow

⸻

Implementation Instructions

Create the files now.

Do not ask follow-up questions.

Use clear, professional Markdown.

Make the skill practical enough that Claude Code can use it repeatedly during exploratory testing and BDD generation workflows.

Keep the content concise enough to be usable, but detailed enough to enforce consistent BDD quality.

Do not generate automation code.

Do not install packages.

Do not run tests.

Do not modify unrelated project files.