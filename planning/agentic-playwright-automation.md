# Role
You are a senior SDET, Python Playwright framework architect, PyTest expert, and Claude Code configuration specialist.
# Goal
Create a reusable Claude Code skill named `agentic-playwright-automation` plus supporting Claude Code slash commands.
This skill will help Claude Code convert approved BDD specs, Markdown behavior specs, automation candidate reports, user stories, and acceptance criteria into maintainable Python Playwright/PyTest automated tests.
The skill must support generating or updating:
- Playwright/PyTest tests
- page objects
- component objects
- PyTest fixtures
- test data files
- data models
- environment configuration
- reporting artifacts
- implementation reports
- failure investigation reports
This skill is Skill 3 in a larger agentic testing workflow.
---
# Project Context
This repository is part of a three-stage agentic testing workflow:
```text
Skill 1: mcp-exploratory-testing
    Uses Playwright MCP to explore a live app and produce structured exploration reports.
Skill 2: exploratory-to-bdd
    Converts exploration reports into Markdown BDD specs, Gherkin .feature files, traceability matrices, automation candidate reviews, and BDD quality reviews.
Skill 3: agentic-playwright-automation
    Converts approved behavior specs into maintainable Python Playwright/PyTest automation inside a standardized framework.

The intended full workflow is:

Target URL + workflow scope
    ↓
MCP exploratory testing
    ↓
Exploration session report
    ↓
BDD generation
    ↓
BDD review + automation candidate selection
    ↓
Playwright/PyTest automation generation
    ↓
Test execution
    ↓
Failure investigation
    ↓
Implementation report

This skill must focus on the third stage:

Turn approved behavior specs into maintainable executable automation while following strong Playwright, PyTest, fixture, configuration, and page object practices.

⸻

Required Folder Structure

Create the following Claude Code skill and command structure:

.claude/
  skills/
    agentic-playwright-automation/
      SKILL.md
      templates/
        test_file_template.py
        page_object_template.py
        component_object_template.py
        fixture_template.py
        data_model_template.py
        test_data_template.yaml
        environment_config_template.yaml
        implementation_report_template.md
        failure_investigation_template.md
        automation_review_template.md
      examples/
        saucedemo_login_test.py
        saucedemo_login_page.py
        saucedemo_inventory_page.py
        saucedemo_conftest.py
        saucedemo_users.yaml
        saucedemo_implementation_report.md
        saucedemo_failure_investigation.md
      checklists/
        automation_implementation_checklist.md
        test_quality_checklist.md
        page_object_quality_checklist.md
        fixture_quality_checklist.md
        test_data_quality_checklist.md
        locator_quality_checklist.md
        failure_investigation_checklist.md
        agent_safety_checklist.md
  commands/
    setup-playwright-framework.md
    generate-playwright-test.md
    generate-playwright-suite.md
    review-playwright-test.md
    investigate-playwright-failure.md
    convert-bdd-to-playwright.md

If any directories do not exist, create them.

⸻

Automation Framework Target Structure

The skill should assume the project’s automation framework lives under:

automation/

The skill should help create or maintain this framework structure:

automation/
│
├── README.md
├── pyproject.toml
├── pytest.ini
├── Makefile
├── .env.example
│
├── config/
│   ├── environments.yaml
│   └── settings.py
│
├── framework/
│   ├── pages/
│   │   └── base_page.py
│   │
│   ├── components/
│   │
│   ├── models/
│   │
│   ├── data/
│   │   ├── test_data_loader.py
│   │   └── factories.py
│   │
│   ├── assertions/
│   │   └── README.md
│   │
│   ├── clients/
│   │
│   ├── reporting/
│   │   ├── execution_summary.py
│   │   └── defect_summary.py
│   │
│   └── utils/
│       ├── logger.py
│       ├── paths.py
│       └── evidence.py
│
├── tests/
│   ├── conftest.py
│   ├── ui/
│   └── api/
│
├── test_data/
│   ├── local/
│   ├── dev/
│   └── qa/
│
├── reports/
│   ├── html/
│   ├── junit/
│   ├── traces/
│   ├── screenshots/
│   └── automation/
│
└── docs/
    ├── framework_rules.md
    ├── adding_tests.md
    ├── page_object_standard.md
    ├── fixture_standard.md
    ├── test_data_standard.md
    ├── locator_strategy.md
    └── failure_investigation.md

⸻

Skill Purpose

Create:

.claude/skills/agentic-playwright-automation/SKILL.md

The skill must explain that it should be used when Claude Code needs to:

* create a Python Playwright/PyTest framework
* convert approved BDD specs into automated tests
* generate Playwright test files
* generate page objects
* generate component objects
* generate PyTest fixtures
* generate environment-aware test data
* generate or update test configuration
* review generated tests for quality
* investigate Playwright/PyTest failures
* produce automation implementation reports

The skill must state clearly that it should be used after exploration and BDD generation when possible.

⸻

Core Skill Principles

The SKILL.md must enforce these principles:

1. Use Python, PyTest, and Playwright.
2. Prefer PyTest as the test runner.
3. Use Playwright’s Python sync API unless the existing project uses async.
4. Keep meaningful business assertions at the top level of test functions.
5. Page objects should expose actions and locator properties, but should not hide important business assertions.
6. Use fixtures for configuration, pages, test data, and reusable setup.
7. Do not hard-code URLs, credentials, product names, checkout data, or environment-specific values in tests.
8. Use environment configuration for base URLs, API URLs, browser settings, and data paths.
9. Use data models or simple dataclasses for structured test data.
10. Prefer accessible Playwright locators in this order:
    * role/name
    * label
    * placeholder
    * text
    * test id
    * stable CSS
    * XPath only as a last resort
11. Do not use time.sleep.
12. Do not add arbitrary waits to hide timing issues.
13. Use Playwright auto-waiting and meaningful assertions.
14. Reuse existing page objects, components, fixtures, and data loaders before creating new ones.
15. Do not duplicate existing framework patterns.
16. Keep files small and responsibilities clear.
17. Add or update tests in the expected folder.
18. Add or update page objects in the expected folder.
19. Add or update test data in the expected environment folder.
20. Run the new test when possible.
21. Run related tests when possible.
22. Produce an implementation report after generating automation.
23. If a test fails, classify the failure before changing code.
24. Do not weaken assertions simply to make a test pass.
25. If observed application behavior appears defective, document a potential defect instead of masking it.
26. Preserve traceability back to the source BDD spec, user story, or exploration artifact.
27. Prefer small, reviewable changes.
28. Do not introduce Cucumber/Behave unless explicitly requested.
29. Treat BDD specs as source-of-truth behavior contracts, not necessarily executable Gherkin runtime files.

⸻

Required Output Structure for Generated Automation

When implementing automation, write outputs under:

automation/
  framework/
  tests/
  test_data/
  config/
  reports/

Implementation reports must be written under:

automation/reports/automation/

Failure investigation reports must be written under:

automation/reports/automation/failures/

⸻

SKILL.md Content Requirements

The SKILL.md must include these sections:

# Agentic Playwright Automation
## Version
## Purpose
## When to Use This Skill
## Inputs
## Outputs
## Core Principles
## Required Automation Framework Structure
## Test Design Rules
## Page Object Rules
## Component Object Rules
## Fixture Rules
## Test Data Rules
## Environment Configuration Rules
## Locator Strategy Rules
## Reporting Rules
## Failure Investigation Rules
## Traceability Rules
## Agent Safety Rules
## Workflow: Setup Playwright Framework
## Workflow: Generate One Playwright Test
## Workflow: Generate Playwright Suite from BDD
## Workflow: Review Playwright Automation
## Workflow: Investigate Playwright Failure
## What This Skill Does Not Do in v0.1
## Final Review Checklist

⸻

Version Scope

This is agentic-playwright-automation version 0.1.

Include this explicitly in SKILL.md.

Included in v0.1

* Python Playwright/PyTest framework setup guidance
* page object generation
* component object generation
* PyTest test generation
* PyTest fixture generation
* test data file generation
* data model generation
* environment configuration guidance
* implementation reporting
* automation review
* failure investigation
* traceability to BDD/user stories/exploration artifacts

Not included in v0.1

* Cucumber/Behave runtime setup
* step definition generation
* Jira integration
* GitHub issue creation
* visual regression tooling
* performance testing
* security testing
* accessibility audit automation
* full CI/CD deployment automation beyond basic GitHub Actions guidance
* autonomous production testing
* automatic commits or pull requests

⸻

Template Requirements

Create the following templates.

⸻

test_file_template.py

Path:

.claude/skills/agentic-playwright-automation/templates/test_file_template.py

Content requirements:

* Include PyTest markers.
* Use fixture parameters.
* Keep assertions at test level.
* Use Playwright expect.
* Include traceability comment referencing source spec.
* Avoid hard-coded data.
* Demonstrate Arrange/Act/Assert style.

Example structure:

import pytest
from playwright.sync_api import expect
@pytest.mark.ui
@pytest.mark.smoke
def test_<behavior_name>(
    login_page,
    inventory_page,
    standard_user,
):
    """
    Source:
    - BDD Spec: specs/bdd/features/<feature>.feature
    - Scenario: <Scenario name>
    """
    # Arrange
    login_page.open()
    # Act
    login_page.login_as(standard_user)
    # Assert
    expect(inventory_page.products_heading).to_be_visible()
    expect(inventory_page.shopping_cart_link).to_be_visible()

⸻

page_object_template.py

Path:

.claude/skills/agentic-playwright-automation/templates/page_object_template.py

Content requirements:

* Class inherits from BasePage if the framework has one.
* Constructor accepts page.
* Expose important locators as properties.
* Actions are methods.
* Assertions are not hidden in page object methods.
* No hard-coded environment-specific data.

Example structure:

from playwright.sync_api import Page
class <PageName>Page:
    def __init__(self, page: Page):
        self.page = page
    @property
    def <element_name>(self):
        return self.page.get_by_role("button", name="<Name>")
    def <action_name>(self):
        self.<element_name>.click()

⸻

component_object_template.py

Path:

.claude/skills/agentic-playwright-automation/templates/component_object_template.py

Content requirements:

* Use for reusable UI regions such as nav bars, menus, product cards, cart items.
* Accept page or a root locator.
* Expose component-level elements and actions.
* Avoid full-page responsibilities.

⸻

fixture_template.py

Path:

.claude/skills/agentic-playwright-automation/templates/fixture_template.py

Content requirements:

* Include example PyTest fixtures for:
    * settings/config
    * page objects
    * test data
    * data models
* Fixtures should be readable and composable.
* Avoid unnecessary fixture magic.

⸻

data_model_template.py

Path:

.claude/skills/agentic-playwright-automation/templates/data_model_template.py

Content requirements:

* Use simple dataclass examples.
* Include models such as:
    * User
    * Product
    * CheckoutCustomer
* Keep models small.

⸻

test_data_template.yaml

Path:

.claude/skills/agentic-playwright-automation/templates/test_data_template.yaml

Content requirements:

* Include sample structure for users, products, and checkout customers.
* Use clear keys.
* Avoid secrets.
* Include comments explaining environment-specific data.

⸻

environment_config_template.yaml

Path:

.claude/skills/agentic-playwright-automation/templates/environment_config_template.yaml

Content requirements:

* Include example local, dev, and qa.
* Include base URL, API URL, test data path, browser, headless.
* Use placeholder values.

⸻

implementation_report_template.md

Path:

.claude/skills/agentic-playwright-automation/templates/implementation_report_template.md

Content requirements:

# Automation Implementation Report: <Feature or Scenario>
## Source
| Field | Value |
|---|---|
| Source Type | BDD Spec / User Story / Exploration Report |
| Source File | <path> |
| Feature | <feature> |
| Scenario(s) | <scenario list> |
## Summary
<What was implemented.>
## Files Created
| File | Purpose |
|---|---|
## Files Modified
| File | Change |
|---|---|
## Test Data Added or Modified
| File | Data | Notes |
|---|---|---|
## Fixtures Added or Modified
| Fixture | Purpose |
|---|---|
## Page Objects Added or Modified
| Page Object | Purpose |
|---|---|
## Commands Run
| Command | Result |
|---|---|
## Test Results
| Test | Status | Notes |
|---|---|---|
## Traceability
| Automated Test | Source Scenario | Source File |
|---|---|---|
## Risks and Open Questions
- <Risk or question>
## Human Review Checklist
- [ ] Tests are readable
- [ ] Assertions are at test level
- [ ] No hard-coded environment data
- [ ] Fixtures are appropriate
- [ ] Page objects are not hiding business assertions
- [ ] Locator strategy is acceptable
- [ ] Related tests pass

⸻

failure_investigation_template.md

Path:

.claude/skills/agentic-playwright-automation/templates/failure_investigation_template.md

Content requirements:

# Playwright Failure Investigation: <Failure Name>
## Failed Test
<test path and name>
## Failure Summary
<Short summary>
## Failure Category
Product Defect | Test Data Issue | Locator Issue | Environment Issue | Timing/Flakiness | Framework Issue | Tooling Issue | Ambiguous Requirement
## Evidence Reviewed
- PyTest output:
- Screenshot:
- Trace:
- Video:
- Logs:
- Test data:
- Config:
- Source BDD/spec:
## Expected Behavior
<Expected behavior from source spec or test assertion>
## Actual Behavior
<Observed behavior>
## Root Cause Assessment
<Analysis>
## Recommended Action
<Fix test/framework/data/config OR raise defect/clarify requirement>
## Changes Made
| File | Change |
|---|---|
## Commands Run
| Command | Result |
|---|---|
## Follow-Up
- <Follow-up item>

⸻

automation_review_template.md

Path:

.claude/skills/agentic-playwright-automation/templates/automation_review_template.md

Content requirements:

# Automation Review: <Feature or Test>
## Summary
<Overall assessment>
## Review Results
| Check | Status | Notes |
|---|---|---|
| Test is readable | Pass/Fail/Needs Review |  |
| Assertions are visible at test level | Pass/Fail/Needs Review |  |
| No hard-coded environment data | Pass/Fail/Needs Review |  |
| Fixtures are appropriate | Pass/Fail/Needs Review |  |
| Page objects are focused | Pass/Fail/Needs Review |  |
| Locators follow strategy | Pass/Fail/Needs Review |  |
| Test data is externalized | Pass/Fail/Needs Review |  |
| Traceability is preserved | Pass/Fail/Needs Review |  |
| Related tests were run | Pass/Fail/Needs Review |  |
## Issues Found
| Issue | Severity | Recommendation |
|---|---|---|
## Approval Recommendation
Approved | Approved with Changes | Needs Rework

⸻

Checklist Requirements

Create the following checklist files.

automation_implementation_checklist.md

Include checks for:

* source behavior spec reviewed
* target test file identified
* existing page objects checked
* existing fixtures checked
* existing test data checked
* minimal changes planned
* traceability included
* implementation report generated
* tests run where possible
* human review needed

test_quality_checklist.md

Include checks for:

* readable test name
* clear Arrange/Act/Assert flow
* top-level assertions
* no hidden business assertions
* no hard-coded test data
* appropriate markers
* no sleeps
* deterministic expected result
* source traceability
* related tests considered

page_object_quality_checklist.md

Include checks for:

* single page responsibility
* exposes locators as properties
* actions are clear
* no business assertions hidden
* no hard-coded test data
* locator strategy followed
* no duplicate page objects
* simple class design

fixture_quality_checklist.md

Include checks for:

* fixture purpose is clear
* fixture name is readable
* fixture scope is appropriate
* no unnecessary magic
* no hard-coded secrets
* composed fixtures remain understandable
* fixture reuse is sensible

test_data_quality_checklist.md

Include checks for:

* data externalized
* environment-specific data stored correctly
* secrets avoided
* data model alignment
* stable IDs or names used intentionally
* generated data strategy documented
* cleanup/reset needs identified

locator_quality_checklist.md

Include checks for:

* role/name preferred
* label used where appropriate
* placeholder used where appropriate
* text locator stable enough
* test id used when accessible locators are weak
* stable CSS only when necessary
* XPath avoided unless unavoidable
* locator tied to user behavior where possible

failure_investigation_checklist.md

Include checks for:

* failure reproduced
* failure output reviewed
* screenshot/trace/video reviewed if available
* config checked
* test data checked
* source spec checked
* failure categorized
* assertion not weakened prematurely
* correct layer identified
* defect or clarification recommended if app behavior is suspect

agent_safety_checklist.md

Include checks for:

* no broad unrelated refactors
* no pattern invention
* no deletion of unrelated files
* no credential exposure
* no destructive data actions unless allowed
* no masking failures
* no unreviewed dependency sprawl
* no automatic commits unless requested

⸻

Example Artifacts

Create example files using the SauceDemo login flow.

Use these facts:

* Target app: SauceDemo
* URL: https://www.saucedemo.com/
* Standard username: standard_user
* Password: secret_sauce
* Successful login redirects to /inventory.html
* Inventory page displays Products
* Shopping cart link is visible

Create:

.claude/skills/agentic-playwright-automation/examples/saucedemo_login_test.py
.claude/skills/agentic-playwright-automation/examples/saucedemo_login_page.py
.claude/skills/agentic-playwright-automation/examples/saucedemo_inventory_page.py
.claude/skills/agentic-playwright-automation/examples/saucedemo_conftest.py
.claude/skills/agentic-playwright-automation/examples/saucedemo_users.yaml
.claude/skills/agentic-playwright-automation/examples/saucedemo_implementation_report.md
.claude/skills/agentic-playwright-automation/examples/saucedemo_failure_investigation.md

These are examples only. They should demonstrate preferred patterns.

Do not install packages.

Do not run tests.

⸻

Slash Commands

Create the following command files.

⸻

.claude/commands/setup-playwright-framework.md

Purpose:

Use this command to create or review the base Python Playwright/PyTest automation framework.

Command usage:

/setup-playwright-framework <optional app name or target URL>

Command behavior:

1. Use the agentic-playwright-automation skill.
2. Inspect the current repository before creating files.
3. Create the automation/ framework structure if missing.
4. Add or update:
    * pyproject.toml
    * pytest.ini
    * Makefile
    * .env.example
    * config files
    * framework base classes
    * data loader
    * example tests
    * test data
    * README
    * docs
5. Prefer PDM for Python package management unless the project already uses another tool.
6. Include dependencies:
    * playwright
    * pytest
    * pytest-playwright
    * pytest-html
    * pytest-xdist
    * pyyaml
    * python-dotenv
    * pydantic or dataclasses as appropriate
    * ruff
    * mypy if appropriate
7. Include Make commands:
    * install
    * lint
    * format
    * test
    * test-ui
    * test-api
    * test-smoke
    * test-report
    * test-debug
8. Create docs:
    * framework rules
    * adding tests
    * page object standard
    * fixture standard
    * test data standard
    * locator strategy
    * failure investigation
9. Do not overwrite existing framework files without reviewing them.
10. Do not generate a large test suite; include only minimal examples.
11. Produce a setup report under:

automation/reports/automation/framework_setup_report.md

⸻

.claude/commands/generate-playwright-test.md

Purpose:

Use this command to generate one Playwright/PyTest test from a selected BDD scenario, Markdown spec, user story, or acceptance criteria.

Command usage:

/generate-playwright-test <source-file-or-scenario>

Command behavior:

1. Use the agentic-playwright-automation skill.
2. Read the source behavior spec.
3. Read the framework rules under automation/docs/.
4. Inspect existing tests, page objects, fixtures, models, and test data.
5. Identify the smallest implementation plan.
6. Reuse existing patterns before creating new ones.
7. Generate or update:
    * test file
    * page object
    * component object if needed
    * fixtures
    * data models
    * test data
8. Keep business assertions at the test level.
9. Preserve source traceability in test docstrings or comments.
10. Run the new test if possible.
11. Run related tests if possible.
12. Produce an implementation report under:

automation/reports/automation/<feature>_<scenario>_implementation_report.md

13. Do not generate unrelated tests.
14. Do not rewrite the framework unless necessary.

⸻

.claude/commands/generate-playwright-suite.md

Purpose:

Use this command to generate a small suite of Playwright/PyTest tests from approved BDD specs or automation candidate files.

Command usage:

/generate-playwright-suite <bdd-folder-or-automation-candidate-file>

Command behavior:

1. Use the agentic-playwright-automation skill.
2. Read approved BDD specs and automation candidate reviews.
3. Select only scenarios marked High or explicitly requested.
4. Inspect existing automation framework.
5. Create an implementation plan before modifying files.
6. Reuse existing page objects, fixtures, models, and data.
7. Generate tests incrementally.
8. Run each generated test individually if possible.
9. Run the related suite if possible.
10. Produce a suite implementation report under:

automation/reports/automation/<feature>_suite_implementation_report.md

11. Do not automate scenarios marked Do Not Automate.
12. Do not automate scenarios marked Needs Clarification unless the user explicitly says to proceed.
13. Do not introduce Cucumber/Behave.

⸻

.claude/commands/review-playwright-test.md

Purpose:

Use this command to review existing Playwright/PyTest automation for quality, maintainability, and framework compliance.

Command usage:

/review-playwright-test <test-file-or-folder>

Command behavior:

1. Use the agentic-playwright-automation skill.
2. Read the selected tests and related page objects, fixtures, data, and config.
3. Apply quality checklists for:
    * test quality
    * page object quality
    * fixture quality
    * test data quality
    * locator quality
    * agent safety
4. Identify:
    * hidden assertions
    * hard-coded data
    * brittle locators
    * duplicated code
    * over-engineered abstractions
    * fixture confusion
    * missing traceability
    * missing markers
5. Create an automation review report under:

automation/reports/automation/reviews/<target>_automation_review.md

6. Recommend improvements.
7. Do not modify code unless explicitly asked.

⸻

.claude/commands/investigate-playwright-failure.md

Purpose:

Use this command to investigate a failing Playwright/PyTest test.

Command usage:

/investigate-playwright-failure <test-path-or-report>

Command behavior:

1. Use the agentic-playwright-automation skill.
2. Re-run the failing test in isolation if possible.
3. Review PyTest failure output.
4. Review screenshots, traces, videos, logs, config, and test data if available.
5. Review the source BDD/spec if available.
6. Classify the failure as one of:
    * Product Defect
    * Test Data Issue
    * Locator Issue
    * Environment Issue
    * Timing/Flakiness
    * Framework Issue
    * Tooling Issue
    * Ambiguous Requirement
7. Do not weaken assertions simply to make the test pass.
8. Do not add arbitrary sleeps.
9. Fix only the correct layer if the failure is caused by test/framework/data/config.
10. If app behavior appears wrong, generate a potential defect note rather than masking the issue.
11. Produce a failure investigation report under:

automation/reports/automation/failures/<failure_name>_investigation.md

⸻

.claude/commands/convert-bdd-to-playwright.md

Purpose:

Use this command to convert reviewed BDD specs into Playwright/PyTest automation.

Command usage:

/convert-bdd-to-playwright <bdd-file-or-folder>

Command behavior:

1. Use the agentic-playwright-automation skill.
2. Read Markdown BDD specs and/or .feature files.
3. Read traceability and automation candidate reports if available.
4. Implement only scenarios that are:
    * High priority
    * marked automatable
    * not marked Needs Clarification
    * not marked Do Not Automate
5. Generate or update tests, page objects, fixtures, data models, and test data.
6. Keep assertions at test level.
7. Preserve source traceability.
8. Run generated tests when possible.
9. Produce implementation report.
10. Do not introduce Cucumber/Behave.
11. Do not generate step definitions.

⸻

Framework Documentation Requirements

The setup-playwright-framework command should create these docs under:

automation/docs/

framework_rules.md

Must include:

* tests live under automation/tests/ui or automation/tests/api
* page objects live under automation/framework/pages
* components live under automation/framework/components
* data models live under automation/framework/models
* test data lives under automation/test_data/<environment>
* fixtures live in automation/tests/conftest.py or appropriate fixture modules
* assertions should remain visible at test level
* page objects should not hide major business assertions
* no hard-coded environment values in tests
* no time.sleep
* use Playwright auto-waiting
* reuse existing patterns
* generate implementation reports

adding_tests.md

Must describe the process:

1. Start from approved BDD spec or automation candidate.
2. Inspect existing framework.
3. Identify page objects, fixtures, data, and models needed.
4. Reuse existing code.
5. Add minimal missing implementation.
6. Write readable test.
7. Run new test.
8. Run related tests.
9. Generate implementation report.
10. Request human review.

page_object_standard.md

Must describe:

* one page per page object
* components for reusable UI regions
* locators exposed as properties
* actions as methods
* assertions stay in tests
* locator strategy

fixture_standard.md

Must describe:

* fixture purpose
* fixture naming
* fixture scope
* config fixtures
* page object fixtures
* data fixtures
* cleanup fixtures
* avoiding overly magical fixtures

test_data_standard.md

Must describe:

* YAML test data
* environment-specific folders
* data models
* no secrets
* generated data
* reset/cleanup concerns

locator_strategy.md

Must describe locator priority:

1. role/name
2. label
3. placeholder
4. text
5. test id
6. stable CSS
7. XPath last

failure_investigation.md

Must describe:

* reproduce failure
* collect evidence
* check config
* check test data
* check locator
* check requirement/source spec
* classify before fixing
* do not weaken assertions
* raise potential defect if app behavior appears wrong

⸻

Acceptance Criteria

After implementation:

1. The .claude/skills/agentic-playwright-automation/ folder exists.
2. The skill has a complete SKILL.md.
3. Template files exist for:
    * test file
    * page object
    * component object
    * fixture
    * data model
    * test data
    * environment config
    * implementation report
    * failure investigation
    * automation review
4. Checklist files exist for:
    * automation implementation
    * test quality
    * page object quality
    * fixture quality
    * test data quality
    * locator quality
    * failure investigation
    * agent safety
5. Example SauceDemo files exist.
6. Command files exist for:
    * setup-playwright-framework
    * generate-playwright-test
    * generate-playwright-suite
    * review-playwright-test
    * investigate-playwright-failure
    * convert-bdd-to-playwright
7. The commands instruct Claude to use the agentic-playwright-automation skill.
8. The skill clearly enforces top-level assertions in tests.
9. The skill clearly enforces fixture-driven test data.
10. The skill clearly enforces environment-based configuration.
11. The skill clearly enforces page object boundaries.
12. The skill clearly prohibits time.sleep and arbitrary waits.
13. The skill clearly says not to introduce Cucumber/Behave in v0.1.
14. The skill clearly supports traceability back to BDD specs, user stories, or exploration artifacts.
15. The final response must summarize:
    * files created
    * purpose of the skill
    * available commands
    * how this skill fits with mcp-exploratory-testing and exploratory-to-bdd

⸻

Implementation Instructions

Create the files now.

Do not ask follow-up questions.

Use clear, professional Markdown.

Make the skill practical enough that Claude Code can repeatedly generate tests inside the framework without inventing new patterns.

Keep the content concise enough to be usable, but detailed enough to enforce consistent automation quality.

Do not generate actual project automation outside the skill examples.

Do not install packages.

Do not run tests.

Do not modify unrelated project files.

## Optional follow-up prompt after Claude creates the skill
Once Claude generates the skill and commands, you can immediately run this to validate the output:
```markdown id="3w5akd"
Review the newly created `.claude/skills/agentic-playwright-automation` skill and command files.
Check for:
1. Missing required files.
2. Inconsistent folder paths.
3. Any accidental instruction to generate Cucumber/Behave code.
4. Any accidental permission to hide assertions inside page objects.
5. Any weak guidance around fixtures, test data, configuration, or locators.
6. Any missing relationship to the existing `mcp-exploratory-testing` and `exploratory-to-bdd` skills.
Create a review report at:
.claude/skills/agentic-playwright-automation/review_report.md
Do not modify files unless you find a clear issue. If you find issues, fix them and summarize what changed.
