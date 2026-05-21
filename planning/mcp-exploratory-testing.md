# Role
You are a senior QA architect, exploratory testing expert, Playwright MCP specialist, and Claude Code configuration specialist.
# Goal
Create a reusable Claude Code skill named `mcp-exploratory-testing` plus supporting Claude Code slash commands.
This skill will guide Claude Code in using Playwright MCP to perform bounded exploratory testing sessions against a live web application and produce structured exploration artifacts.
This skill is responsible for:
- opening and navigating web applications through Playwright MCP
- exploring a defined workflow or bounded application area
- recording observed pages, actions, outcomes, data needs, and anomalies
- identifying candidate test cases
- identifying candidate page models
- identifying open questions and risks
- producing structured exploration session reports
This skill is **not** responsible for generating BDD specs or automated test code. BDD generation is handled by a separate skill named `exploratory-to-bdd`.
---
# Project Context
This repository is part of an agentic testing workflow.
The intended workflow is:
```text
Target URL + workflow scope
    ↓
mcp-exploratory-testing skill
    ↓
Playwright MCP browser exploration
    ↓
Structured exploration session report
    ↓
exploratory-to-bdd skill
    ↓
Markdown BDD specs + Gherkin .feature files
    ↓
BDD quality review + traceability matrix
    ↓
Future conversion to Playwright/PyTest automation

The purpose of this skill is to standardize the first stage of the workflow:

Use Claude Code and Playwright MCP to explore a live application like a human exploratory tester, while preserving structured evidence that can later be converted into BDD specs or automated tests.

⸻

Required Folder Structure

Create the following Claude Code skill and command structure:

.claude/
  skills/
    mcp-exploratory-testing/
      SKILL.md
      templates/
        exploration_session_template.md
        page_observation_template.md
        action_timeline_template.md
        anomaly_report_template.md
        test_idea_template.md
        page_model_candidate_template.md
        exploration_review_template.md
      examples/
        saucedemo_checkout_exploration.md
        saucedemo_checkout_anomalies.md
        saucedemo_checkout_test_ideas.md
      checklists/
        exploration_scope_checklist.md
        observation_quality_checklist.md
        anomaly_classification_checklist.md
        test_idea_quality_checklist.md
  commands/
    explore-workflow.md
    explore-app.md
    review-exploration.md
    exploration-to-bdd.md

If any directories do not exist, create them.

⸻

Skill Purpose

Create:

.claude/skills/mcp-exploratory-testing/SKILL.md

The skill must explain that it should be used when Claude Code needs to use Playwright MCP to explore a live web application and produce structured exploratory testing artifacts.

The skill should apply when the user provides:

* a target URL
* a workflow scope
* a user story
* a business flow
* a feature area
* an exploratory testing goal
* a regression risk area
* a prompt such as: “Use Playwright MCP to explore the standard user checkout flow.”

⸻

Core Skill Principles

The SKILL.md must enforce these principles:

1. Explore only the requested workflow or bounded scope.
2. Prefer Playwright MCP accessibility snapshots for reasoning.
3. Use screenshots only when visual evidence is needed.
4. Record observations in structured Markdown.
5. Separate observed application behavior from expected/intended behavior.
6. Separate application anomalies from tooling anomalies.
7. Do not invent requirements.
8. Do not silently decide product correctness without a requirement.
9. Document assumptions, uncertainty, and open questions.
10. Capture data used during exploration.
11. Capture pages visited and their purpose.
12. Capture actions performed and observed outcomes.
13. Capture state changes such as URL changes, button text changes, cart badge changes, validation messages, and confirmation messages.
14. Identify candidate assertions from observed outcomes.
15. Identify candidate test cases, but do not generate formal BDD specs.
16. Identify candidate page models, but do not generate page object code.
17. Do not generate Playwright/PyTest automation code in this skill version.
18. Do not generate Cucumber/Behave feature files in this skill version.
19. Do not modify application data destructively unless the user explicitly allows it.
20. Do not store secrets, tokens, or private credentials in reports.
21. Treat public demo credentials as acceptable only when they are visibly provided by the demo app or user.
22. Clearly mark any tool workaround, such as using DOM .click() via browser_evaluate when an MCP click does not trigger expected behavior.

⸻

Required Output Structure

The skill must standardize exploration outputs under:

sessions/
  mcp-exploration/
    <app-name>/
      <workflow-name>_session.md
reports/
  exploration/
    <app-name>/
      <workflow-name>_observations.md
      <workflow-name>_anomalies.md
      <workflow-name>_test_ideas.md
      <workflow-name>_review.md

For small explorations, it is acceptable to produce only the main session report:

sessions/mcp-exploration/<app-name>/<workflow-name>_session.md

But the command should recommend splitting observations, anomalies, and test ideas into separate reports when the session becomes large.

⸻

Required Session Report Format

Create template:

.claude/skills/mcp-exploratory-testing/templates/exploration_session_template.md

The session report must include:

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
## Recommended Next Step
<Example: Convert high-priority candidate cases into BDD specs using the exploratory-to-bdd skill.>

⸻

Page Observation Template

Create template:

.claude/skills/mcp-exploratory-testing/templates/page_observation_template.md

The page observation template must include:

# Page Observation: <Page Name>
## URL
<URL or path>
## Page Purpose
<Observed purpose>
## Entry Conditions
- <How the user reached the page>
## Observed Elements
| Element | Type | User-Visible Text | Locator Hint | Notes |
|---|---|---|---|---|
## User Actions Available
| Action | Trigger Element | Observed Result | Notes |
|---|---|---|---|
## State Changes
| Trigger | Before | After | Notes |
|---|---|---|---|
## Candidate Assertions
- <Assertion 1>
- <Assertion 2>
## Candidate Test Ideas
- <Test idea 1>
- <Test idea 2>
## Open Questions
- <Question 1>

⸻

Action Timeline Template

Create template:

.claude/skills/mcp-exploratory-testing/templates/action_timeline_template.md

The action timeline template must include:

# Action Timeline: <Workflow Name>
| Step | Page | Action | Test Data | Observed Result | Evidence | Notes |
|---:|---|---|---|---|---|---|

⸻

Anomaly Report Template

Create template:

.claude/skills/mcp-exploratory-testing/templates/anomaly_report_template.md

The anomaly report template must include:

# Exploration Anomaly Report: <Workflow Name>
| ID | Type | Observation | Evidence | Severity | Impact | Recommendation | Status |
|---|---|---|---|---|---|---|---|

Anomaly types:

Application Behavior
Tooling Behavior
Environment
Data
Usability
Accessibility
Performance Observation
Unknown

Severity values:

Low
Medium
High
Critical
Needs Clarification

Status values:

Open
Needs Review
Clarified
Potential Defect
Tooling Limitation
Closed

⸻

Test Idea Template

Create template:

.claude/skills/mcp-exploratory-testing/templates/test_idea_template.md

The test idea template must include:

# Candidate Test Ideas: <Workflow Name>
| Candidate ID | Title | Behavior Area | Priority | Suggested Type | Rationale | Notes |
|---|---|---|---|---|---|---|

Priority values:

High
Medium
Low
Needs Clarification

Suggested type values:

BDD Spec
Exploratory Follow-Up
Playwright UI Automation Candidate
API Automation Candidate
Manual Review
Defect Investigation
Do Not Automate

⸻

Page Model Candidate Template

Create template:

.claude/skills/mcp-exploratory-testing/templates/page_model_candidate_template.md

The page model candidate template must include:

# Candidate Page Models: <Workflow Name>
## <Page Model Name>
### Observed Purpose
<Observed page purpose>
### Candidate Actions
| Action | Description | Data Needed | Resulting State |
|---|---|---|---|
### Candidate Elements
| Element | User-Visible Text | Locator Hint | Notes |
|---|---|---|---|
### Candidate Assertions
- <Assertion 1>
- <Assertion 2>
### Risks
- <Risk 1>

The skill must state clearly that candidate page models are design observations only and should not be treated as implementation until a separate automation phase.

⸻

Exploration Review Template

Create template:

.claude/skills/mcp-exploratory-testing/templates/exploration_review_template.md

The exploration review must include:

# Exploration Review: <Workflow Name>
## Summary
<Overall review of exploration completeness and evidence quality.>
## Review Results
| Check | Status | Notes |
|---|---|---|
| Scope was followed | Pass/Fail/Needs Review |  |
| Pages were documented | Pass/Fail/Needs Review |  |
| Actions were documented | Pass/Fail/Needs Review |  |
| Outcomes were documented | Pass/Fail/Needs Review |  |
| Test data was captured | Pass/Fail/Needs Review |  |
| Anomalies were separated from expected behavior | Pass/Fail/Needs Review |  |
| Tooling issues were separated from app issues | Pass/Fail/Needs Review |  |
| Candidate test ideas were identified | Pass/Fail/Needs Review |  |
| Open questions were captured | Pass/Fail/Needs Review |  |
## Gaps
| Gap | Impact | Recommendation |
|---|---|---|
## Recommended Next Step
<Recommendation>

⸻

Checklists

Create the following checklist files.

.claude/skills/mcp-exploratory-testing/checklists/exploration_scope_checklist.md

Include checks for:

* target URL provided
* workflow scope provided
* in-scope areas identified
* out-of-scope areas identified
* user role identified
* required test data identified
* destructive actions avoided unless permitted
* credentials handled safely
* stop condition defined
* next artifact identified

.claude/skills/mcp-exploratory-testing/checklists/observation_quality_checklist.md

Include checks for:

* pages visited are recorded
* URLs or paths are recorded
* page purposes are described
* visible elements are listed
* actions are listed
* state changes are documented
* candidate assertions are identified
* evidence references are included
* assumptions are listed
* open questions are listed

.claude/skills/mcp-exploratory-testing/checklists/anomaly_classification_checklist.md

Include checks for:

* anomaly type identified
* severity assigned
* evidence recorded
* app behavior separated from tooling behavior
* environment issues separated from application issues
* recommendation provided
* status assigned
* potential defects marked clearly
* uncertainty documented

.claude/skills/mcp-exploratory-testing/checklists/test_idea_quality_checklist.md

Include checks for:

* candidate test has clear behavior area
* candidate test has observable expected result
* priority assigned
* rationale provided
* suggested test type assigned
* not duplicative of another candidate
* suitable for BDD conversion if relevant
* automation candidacy noted but not implemented

⸻

Example Artifacts

Create example files using the SauceDemo standard user checkout flow.

Use these observed facts:

* Target app: SauceDemo
* URL: https://www.saucedemo.com/
* Workflow: standard user checkout
* Standard username: standard_user
* Password: secret_sauce
* Successful login redirects to /inventory.html
* Inventory page displays Products
* Inventory page has six products
* Adding Sauce Labs Backpack changes its button to Remove
* Cart badge increments to 1
* Cart page displays Sauce Labs Backpack with quantity 1
* Checkout accepts first name, last name, and postal code
* Checkout overview displays item total, tax, and total
* Completing checkout displays Thank you for your order!
* Back Home returns user to inventory page
* Reset App State may clear state while visible button text may require reload to fully reflect reset
* In one observed MCP session, a tool click returned success but the React handler did not fire; DOM .click() through evaluate worked as fallback

Create:

.claude/skills/mcp-exploratory-testing/examples/saucedemo_checkout_exploration.md
.claude/skills/mcp-exploratory-testing/examples/saucedemo_checkout_anomalies.md
.claude/skills/mcp-exploratory-testing/examples/saucedemo_checkout_test_ideas.md

Do not include automation code.

⸻

Slash Commands

Create the following command files.

⸻

.claude/commands/explore-workflow.md

Purpose:

Use this command when the user wants Claude Code to use Playwright MCP to explore a bounded workflow.

Command usage:

/explore-workflow <target-url> <workflow-scope>

Command behavior:

1. Use the mcp-exploratory-testing skill.
2. Verify Playwright MCP tools are available.
3. Open the target URL.
4. Explore only the requested workflow scope.
5. Prefer accessibility snapshots for reasoning.
6. Record pages, actions, outcomes, state changes, data used, anomalies, and tooling notes.
7. Identify candidate test cases and candidate page models.
8. Produce a session report at:

sessions/mcp-exploration/<app-name>/<workflow-name>_session.md

9. Do not generate BDD specs.
10. Do not generate automation code.
11. Recommend using the exploratory-to-bdd skill as the next step.

The command should include this instruction:

If scope is ambiguous, choose the smallest reasonable workflow and document assumptions instead of exploring the entire application.

⸻

.claude/commands/explore-app.md

Purpose:

Use this command for broader app reconnaissance, still bounded and structured.

Command usage:

/explore-app <target-url> <scope-or-goal>

Command behavior:

1. Use the mcp-exploratory-testing skill.
2. Explore the target app only within the stated scope.
3. Identify major pages, navigation paths, forms, flows, user roles if visible, and obvious risk areas.
4. Avoid destructive actions unless explicitly permitted.
5. Produce an app reconnaissance report under:

sessions/mcp-exploration/<app-name>/app_reconnaissance_session.md

6. Generate candidate workflows for follow-up exploration.
7. Do not generate BDD specs.
8. Do not generate automation code.

⸻

.claude/commands/review-exploration.md

Purpose:

Use this command to review existing exploration notes for completeness and quality.

Command usage:

/review-exploration <exploration-file-or-folder>

Command behavior:

1. Use the mcp-exploratory-testing skill.
2. Read the provided exploration artifact.
3. Apply the exploration review checklist.
4. Identify gaps, ambiguity, missing data, missing outcomes, missing anomalies, and weak evidence.
5. Create or update a review file under:

reports/exploration/<app-name>/<workflow-name>_review.md

6. Do not generate BDD specs unless explicitly asked.
7. Do not generate automation code.

⸻

.claude/commands/exploration-to-bdd.md

Purpose:

Bridge from the MCP exploration skill to the separate exploratory-to-bdd skill.

Command usage:

/exploration-to-bdd <exploration-session-file>

Command behavior:

1. Read the exploration session file.
2. Confirm it contains enough information for BDD conversion.
3. If sufficient, invoke/use the exploratory-to-bdd skill.
4. Generate:
    * Markdown BDD spec
    * Gherkin .feature file
    * traceability matrix
    * automation candidate review
    * BDD quality review
5. If not sufficient, create an exploration review describing missing information.
6. Do not generate Playwright/PyTest automation code.

This command should clearly state that mcp-exploratory-testing handles observation and exploratory-to-bdd handles BDD generation.

⸻

SKILL.md Content Requirements

The SKILL.md must include these sections:

# MCP Exploratory Testing
## Version
## Purpose
## When to Use This Skill
## Inputs
## Outputs
## Core Principles
## Required Output Structure
## Exploration Scope Rules
## Playwright MCP Usage Rules
## Observation Rules
## Action Timeline Rules
## Page Observation Rules
## Data Capture Rules
## Anomaly and Risk Rules
## Candidate Test Idea Rules
## Candidate Page Model Rules
## Safety and Credential Rules
## Tooling Limitation Rules
## Workflow: Bounded Workflow Exploration
## Workflow: App Reconnaissance
## Workflow: Exploration Review
## Workflow: Exploration to BDD Handoff
## What This Skill Does Not Do in v0.1
## Final Review Checklist

⸻

Version Scope

This is mcp-exploratory-testing version 0.1.

Include this explicitly in SKILL.md.

Included in v0.1

* bounded workflow exploration
* app reconnaissance
* page observations
* action timeline
* observed outcomes
* test data capture
* anomaly and risk capture
* candidate test ideas
* candidate page models
* open questions
* exploration quality review
* handoff guidance to the exploratory-to-bdd skill

Not included in v0.1

* BDD spec generation
* Gherkin .feature generation
* Playwright/PyTest code generation
* page object implementation
* test fixture implementation
* formal defect filing
* Jira/GitHub issue creation
* performance testing
* accessibility audit
* security testing
* visual regression testing

⸻

Acceptance Criteria

After implementation:

1. The .claude/skills/mcp-exploratory-testing/ folder exists.
2. The skill has a complete SKILL.md.
3. Template files exist for:
    * exploration session
    * page observation
    * action timeline
    * anomaly report
    * test ideas
    * candidate page models
    * exploration review
4. Checklist files exist for:
    * exploration scope
    * observation quality
    * anomaly classification
    * test idea quality
5. Example SauceDemo files exist.
6. Command files exist for:
    * explore-workflow
    * explore-app
    * review-exploration
    * exploration-to-bdd
7. The commands instruct Claude to use the mcp-exploratory-testing skill.
8. The skill clearly enforces separation of observed application behavior from intended behavior.
9. The skill clearly separates application anomalies from tooling anomalies.
10. The skill clearly states that it does not generate BDD specs or automation code in v0.1.
11. The exploration-to-bdd command clearly hands off to the separate exploratory-to-bdd skill.
12. The output is documentation-only: Markdown skill, template, checklist, example, and command files.
13. The final response must summarize:
    * files created
    * purpose of the skill
    * available commands
    * how this skill fits into the larger exploratory testing to BDD workflow

⸻

Implementation Instructions

Create the files now.

Do not ask follow-up questions.

Use clear, professional Markdown.

Make the skill practical enough that Claude Code can use it repeatedly during browser-based exploratory testing sessions.

Keep the content concise enough to be usable, but detailed enough to enforce consistent exploration quality.

Do not generate BDD specs as project output outside the example files.

Do not generate Playwright/PyTest automation code.

Do not install packages.

Do not run tests.

Do not modify unrelated project files.
