---
name: agentic-playwright-automation
description: Use when the user wants to convert approved BDD specs, Markdown behavior specs, automation candidate reports, user stories, or acceptance criteria into maintainable Python Playwright/PyTest automated tests — or when the user wants to scaffold a Python Playwright/PyTest framework, generate or update page objects, components, fixtures, data models, test data, or environment configuration, run a quality review of existing Playwright automation, or investigate a Playwright/PyTest test failure. Does not generate Cucumber/Behave step definitions or runtime in v0.1.
---

# Agentic Playwright Automation

## Version

0.1

## Purpose

Convert approved behavior specifications (BDD specs, Gherkin `.feature` files, automation candidate reviews, user stories, acceptance criteria, and exploration artifacts) into maintainable Python Playwright/PyTest automation inside a standardized framework. Also create or maintain the framework itself, review existing automation for quality, and investigate test failures without weakening behavior.

This is skill 3 in the agentic testing workflow:

```
Skill 1: mcp-exploratory-testing      -> exploration session reports
Skill 2: exploratory-to-bdd           -> Markdown BDD specs, .feature files,
                                         traceability, automation candidates
Skill 3: agentic-playwright-automation -> Python Playwright/PyTest automation
                                         inside automation/
```

## When to Use This Skill

Use this skill when the user wants to:

- Create or extend a Python Playwright/PyTest framework under `automation/`.
- Convert an approved BDD spec, `.feature` file, automation candidate, user story, or acceptance criteria into one or more Playwright/PyTest tests.
- Generate or update page objects, components, fixtures, data models, test data, or environment configuration.
- Review existing Playwright/PyTest automation for quality, maintainability, and framework compliance.
- Investigate a failing Playwright/PyTest test and classify the failure (Product Defect, Test Data, Locator, Environment, Timing/Flakiness, Framework, Tooling, Ambiguous Requirement).
- Produce an implementation report after writing automation.

Prefer using this skill after the `mcp-exploratory-testing` and `exploratory-to-bdd` skills have produced reviewable inputs.

Do not use this skill to introduce Cucumber or Behave, to generate step definitions, or to perform performance, security, accessibility, or visual regression testing in v0.1.

## Inputs

- Approved BDD Markdown specs under `specs/bdd/markdown/`.
- Gherkin `.feature` files under `specs/bdd/features/`.
- Automation candidate reviews under `specs/bdd/automation/`.
- Traceability matrices under `specs/bdd/traceability/`.
- BDD quality reviews under `specs/bdd/reviews/`.
- Exploration session reports under `sessions/mcp-exploration/`.
- Free-form user stories, acceptance criteria, or bug reports provided by the user.

## Outputs

Generated automation:

- Test files under `automation/tests/ui/` or `automation/tests/api/`.
- Page objects under `automation/framework/pages/`.
- Component objects under `automation/framework/components/`.
- Data models under `automation/framework/models/`.
- Test data under `automation/test_data/<environment>/`.
- Environment configuration under `automation/config/`.
- Fixtures in `automation/tests/conftest.py` or scoped `conftest.py` files.

Reports:

- Implementation reports under `automation/reports/automation/`.
- Suite implementation reports under `automation/reports/automation/`.
- Failure investigation reports under `automation/reports/automation/failures/`.
- Automation review reports under `automation/reports/automation/reviews/`.
- Framework setup report under `automation/reports/automation/framework_setup_report.md`.

## Core Principles

1. Use Python, PyTest, and Playwright.
2. Prefer PyTest as the test runner.
3. Use Playwright's Python sync API unless the existing project already uses async.
4. Keep meaningful business assertions at the top level of test functions.
5. Page objects should expose actions and locator properties, but must not hide important business assertions.
6. Use fixtures for configuration, pages, test data, and reusable setup.
7. Do not hard-code URLs, credentials, product names, checkout data, or environment-specific values in tests.
8. Use environment configuration for base URLs, API URLs, browser settings, and data paths.
9. Use data models or simple dataclasses for structured test data.
10. Prefer accessible Playwright locators in this order: role/name, label, placeholder, text, test id, stable CSS, XPath only as a last resort.
11. Do not use `time.sleep`.
12. Do not add arbitrary waits to hide timing issues.
13. Use Playwright auto-waiting and meaningful `expect` assertions.
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

## Required Automation Framework Structure

```
automation/
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
│   ├── components/
│   ├── models/
│   ├── data/
│   │   ├── test_data_loader.py
│   │   └── factories.py
│   ├── assertions/
│   │   └── README.md
│   ├── clients/
│   ├── reporting/
│   │   ├── execution_summary.py
│   │   └── defect_summary.py
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
```

Use PDM for Python package management unless the project already uses another tool. Provide a `Makefile` with `install`, `lint`, `format`, `test`, `test-ui`, `test-api`, `test-smoke`, `test-report`, and `test-debug` targets.

## Test Design Rules

- One behavior per test function. If a `.feature` scenario covers multiple distinct behaviors, split it.
- Follow Arrange / Act / Assert; use blank lines or comments to make the phases obvious.
- Test function names start with `test_` and describe the behavior, not the steps.
- Use PyTest markers (`@pytest.mark.ui`, `@pytest.mark.api`, `@pytest.mark.smoke`, `@pytest.mark.regression`, `@pytest.mark.negative`, plus feature-area markers).
- Use `playwright.sync_api.expect` for assertions on Locators and Pages so auto-waiting applies.
- Use `assert` only for non-UI data assertions (model equality, API response shape).
- Include a docstring with traceability to the source BDD scenario, user story ID, or exploration artifact.
- Parametrize with `@pytest.mark.parametrize` when the same behavior is exercised across multiple data sets; data should come from fixtures or test data files, not literals.
- Do not call `time.sleep`. Do not use `page.wait_for_timeout`. Use Playwright auto-waiting via `expect`, `wait_for`, or `locator.wait_for`.

## Page Object Rules

- One class per page or significant view.
- Constructor accepts a Playwright `Page` (or a parent locator for components).
- Inherit from `BasePage` when a base exists in the framework.
- Expose important locators as `@property` so the test can assert on them when needed.
- Expose user actions as methods named for the user intent (`login_as(user)`, `add_to_cart(product)`).
- Do not put business assertions inside page object methods. A page object method may verify a precondition (page loaded, URL matches) but must not own a behavior assertion that the test should make visible.
- Do not embed environment-specific values (URLs, credentials, test data). Accept them as method arguments or via injected fixtures.
- Do not duplicate locator definitions across page objects; extract a component if the same region appears on multiple pages.

## Component Object Rules

- Use components for reusable UI regions: navigation bars, menus, modals, product cards, cart drawers.
- Constructor accepts the parent `Page` and a root locator scoping the component.
- Expose component-level locators and actions only; do not perform full-page navigation.
- Components must not perform business assertions on behalf of tests.

## Fixture Rules

- Fixtures live in `automation/tests/conftest.py` or scoped `conftest.py` files near the tests that use them.
- Fixture names describe the resource (`standard_user`, `login_page`, `settings`, `api_client`).
- Default fixture scope is `function`. Use `session` or `module` only for expensive resources that are safe to share.
- Configuration fixtures must read from `automation/config/` and environment variables, not hard-coded literals.
- Page object fixtures construct the page from the Playwright `page` fixture.
- Test data fixtures load from `automation/test_data/<environment>/` via `framework/data/test_data_loader.py`.
- Do not store secrets in fixtures. Read from environment variables or a `.env` file, never check secrets into the repo.
- Avoid deep fixture chains. A test should be readable without reading three layers of fixtures.

## Test Data Rules

- Test data lives under `automation/test_data/<environment>/` in YAML.
- Environment-specific values (URLs, IDs, accounts) are partitioned by environment folder.
- A data loader under `automation/framework/data/test_data_loader.py` selects the active environment.
- Use data models in `automation/framework/models/` to give structured access to test data.
- Do not commit private credentials, tokens, or PII. Use environment variables and a documented `.env.example`.
- Mark generated data clearly when factories produce it (`framework/data/factories.py`).
- Document any cleanup or reset requirements next to the data file.

## Environment Configuration Rules

- `automation/config/environments.yaml` lists `local`, `dev`, `qa` (and others as needed).
- Each environment defines `base_url`, `api_url`, `browser`, `headless`, and `test_data_path`.
- `automation/config/settings.py` resolves the active environment from `APP_ENV` (default `local`), reads `environments.yaml`, and overlays values from `.env`.
- Tests and page objects receive configuration through fixtures, never by reading YAML directly.

## Locator Strategy Rules

Locator priority, highest first:

1. `page.get_by_role(role, name=...)`
2. `page.get_by_label(...)`
3. `page.get_by_placeholder(...)`
4. `page.get_by_text(...)`
5. `page.get_by_test_id(...)`
6. Stable CSS selectors
7. XPath only as a last resort, with a comment explaining why

Locators should reflect user behavior. If only XPath works, that often indicates a missing accessible name or test id; record it as an Open Question in the implementation report.

## Reporting Rules

- Configure PyTest HTML report output to `automation/reports/html/`.
- Configure JUnit XML output to `automation/reports/junit/`.
- Store Playwright traces under `automation/reports/traces/` and screenshots under `automation/reports/screenshots/` when failures occur.
- Implementation reports go to `automation/reports/automation/<feature>_<scenario>_implementation_report.md`.
- Suite implementation reports go to `automation/reports/automation/<feature>_suite_implementation_report.md`.
- Failure investigation reports go to `automation/reports/automation/failures/<failure_name>_investigation.md`.
- Automation review reports go to `automation/reports/automation/reviews/<target>_automation_review.md`.

## Failure Investigation Rules

- Reproduce the failure in isolation before changing code.
- Review PyTest output, screenshots, traces, videos, logs, environment config, test data, and the source BDD/spec.
- Classify the failure as exactly one of: Product Defect, Test Data Issue, Locator Issue, Environment Issue, Timing/Flakiness, Framework Issue, Tooling Issue, Ambiguous Requirement.
- Fix only the layer responsible for the failure.
- Never weaken or remove a business assertion to make a test pass.
- Never insert `time.sleep` or arbitrary waits to mask a timing issue.
- If the application appears defective, write a Potential Defect note in the investigation report rather than changing the test to match the buggy behavior.
- File the investigation under `automation/reports/automation/failures/`.

## Traceability Rules

- Every generated test docstring must reference its source: BDD Markdown spec path, scenario name (and Scenario ID where available), or user story/issue ID.
- Every implementation report must list each automated test and its source scenario.
- When extending a BDD spec or `.feature` file, update the spec first (via the `exploratory-to-bdd` skill) rather than embedding new behavior only in the test.

## Agent Safety Rules

- Do not perform broad unrelated refactors.
- Do not invent new framework patterns when an existing one fits.
- Do not delete unrelated files.
- Do not expose credentials in code, fixtures, reports, or commit messages.
- Do not run destructive data operations against shared environments unless the user explicitly authorizes them for the session.
- Do not mask failures by weakening assertions, swallowing exceptions, or adding waits.
- Do not pull in dependencies that are not required. Pin versions in `pyproject.toml`.
- Do not commit, push, or open pull requests unless the user explicitly asks.

## Workflow: Setup Playwright Framework

1. Inspect the current repository. If `automation/` exists, read what is already there.
2. Use the `/setup-playwright-framework` command behavior: create only missing pieces of the structure shown above.
3. Configure PDM with `playwright`, `pytest`, `pytest-playwright`, `pytest-html`, `pytest-xdist`, `pyyaml`, `python-dotenv`, `pydantic` (or stdlib `dataclasses`), `ruff`, and `mypy` (optional).
4. Create `Makefile` targets: `install`, `lint`, `format`, `test`, `test-ui`, `test-api`, `test-smoke`, `test-report`, `test-debug`.
5. Create framework docs under `automation/docs/`.
6. Write a setup report at `automation/reports/automation/framework_setup_report.md`.
7. Do not install packages and do not run tests unless the user explicitly asks.

## Workflow: Generate One Playwright Test

1. Read the source behavior spec (BDD Markdown, `.feature`, user story, or acceptance criteria).
2. Read `automation/docs/framework_rules.md` and related standards.
3. Inspect existing tests, page objects, components, fixtures, models, and test data for reuse.
4. Plan the smallest change that implements the behavior.
5. Reuse existing patterns; create new abstractions only when none fit.
6. Generate or update: test file, page object(s), component(s) if needed, fixtures, data models, test data.
7. Keep business assertions at the top level of the test, expressed with Playwright `expect`.
8. Include traceability in the test docstring.
9. Run the new test if the user authorizes execution; run the related folder if practical.
10. Write `automation/reports/automation/<feature>_<scenario>_implementation_report.md`.

## Workflow: Generate Playwright Suite from BDD

1. Read approved BDD specs and the automation candidate review.
2. Select only scenarios marked `High` priority, `@automatable`, and not `@needs-clarification` or `Do Not Automate`.
3. Inspect the existing framework. Plan a minimal incremental rollout.
4. Generate tests one at a time, running each before moving on if execution is authorized.
5. Reuse page objects, components, fixtures, models, and data; avoid duplication.
6. Produce one suite implementation report at `automation/reports/automation/<feature>_suite_implementation_report.md`, plus per-scenario implementation reports if scenarios are nontrivial.
7. Do not automate scenarios marked `Needs Clarification` unless the user explicitly authorizes it for the session.
8. Do not introduce Cucumber/Behave.

## Workflow: Review Playwright Automation

1. Read the target test files and the related page objects, components, fixtures, data, and config.
2. Apply: `checklists/test_quality_checklist.md`, `checklists/page_object_quality_checklist.md`, `checklists/fixture_quality_checklist.md`, `checklists/test_data_quality_checklist.md`, `checklists/locator_quality_checklist.md`, `checklists/agent_safety_checklist.md`.
3. Identify hidden assertions, hard-coded data, brittle locators, duplicated code, over-engineered abstractions, fixture confusion, missing traceability, and missing markers.
4. Write `automation/reports/automation/reviews/<target>_automation_review.md` using `templates/automation_review_template.md`.
5. End with an Approval Recommendation: Approved, Approved with Changes, Needs Rework.
6. Do not modify code unless the user explicitly asks.

## Workflow: Investigate Playwright Failure

1. Re-run the failing test in isolation if execution is authorized.
2. Review failure output, screenshots, traces, videos, logs, config, test data, and the source spec.
3. Classify the failure (one of the eight categories).
4. Fix only the correct layer. Do not weaken assertions, do not add sleeps.
5. If the application appears wrong, write a Potential Defect note instead of changing the test.
6. Write `automation/reports/automation/failures/<failure_name>_investigation.md` using `templates/failure_investigation_template.md`.

## What This Skill Does Not Do in v0.1

Included:

- Python Playwright/PyTest framework setup guidance.
- Page object and component generation.
- PyTest test, fixture, data model, and test data generation.
- Environment configuration guidance.
- Implementation reporting.
- Automation review.
- Failure investigation.
- Traceability to BDD, user stories, and exploration artifacts.

Not included:

- Cucumber/Behave runtime setup.
- Step definition generation.
- Jira integration.
- GitHub issue creation.
- Visual regression tooling.
- Performance testing.
- Security testing.
- Accessibility audit automation.
- Full CI/CD deployment automation beyond basic GitHub Actions guidance.
- Autonomous production testing.
- Automatic commits or pull requests.

## Final Review Checklist

Before returning generated automation:

- Source spec is referenced in every new test docstring.
- Tests follow Arrange / Act / Assert with top-level `expect` assertions.
- No `time.sleep` and no arbitrary `wait_for_timeout` were introduced.
- Page objects expose locators and actions; no business assertions are hidden inside them.
- Components are used for reusable UI regions; full-page responsibilities stay in page objects.
- Fixtures are named for the resource and live in `conftest.py` or a scoped fixture module.
- No hard-coded URLs, credentials, product names, or checkout data appear in tests or page objects.
- Test data lives under `automation/test_data/<environment>/` and is loaded through the data loader.
- Locators follow the priority order; XPath usage is justified in the implementation report.
- Existing patterns were reused before new ones were introduced.
- An implementation report was written under `automation/reports/automation/`.
- No Cucumber/Behave artifacts were introduced.
- No secrets were committed.
- No automatic commits, pushes, or pull requests were performed unless explicitly authorized.
