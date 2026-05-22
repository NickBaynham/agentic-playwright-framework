---
description: Generate one Playwright/PyTest test from a selected BDD scenario, Markdown spec, user story, or acceptance criteria. Reuses existing framework patterns and writes an implementation report. Does not introduce Cucumber/Behave.
argument-hint: <source-file-or-scenario>
---

# /generate-playwright-test

Use the `agentic-playwright-automation` skill.

Arguments: `$ARGUMENTS`

## Behavior

1. Use the `agentic-playwright-automation` skill and its templates and checklists.
2. Read the source behavior spec at the supplied path. If a `.feature` file and a Markdown BDD spec both exist for the same feature, prefer the Markdown spec as the contract and the `.feature` file for scenario phrasing.
3. Read `automation/docs/framework_rules.md` and related standards (`page_object_standard.md`, `fixture_standard.md`, `test_data_standard.md`, `locator_strategy.md`).
4. Inspect existing tests, page objects, components, fixtures, models, and test data for reuse.
5. Produce the smallest implementation plan that covers the selected scenario.
6. Reuse existing patterns before creating new ones. If a new page object, component, or fixture is required, justify it in the implementation report.
7. Generate or update: test file under `automation/tests/ui/` or `automation/tests/api/`, page object(s) under `automation/framework/pages/`, component(s) under `automation/framework/components/` if needed, fixtures in the appropriate `conftest.py`, data models under `automation/framework/models/`, test data under `automation/test_data/<environment>/`.
8. Keep business assertions at the top level of the test using Playwright `expect`. Do not hide assertions inside page objects.
9. Include traceability in the test docstring (source BDD path, scenario name, Scenario ID, or user story ID).
10. Run the new test only if the user authorizes execution. Run related tests in the same folder if practical and authorized.
11. Do not perform any git commit, push, or pull request.
12. Write an implementation report at `automation/reports/automation/<feature>_<scenario>_implementation_report.md`.

## Output Summary

Finish by listing: the test file path, page objects and components touched, fixtures added or modified, test data added or modified, commands run (if any), test results, the implementation report path, and any Open Questions or Potential Defects.
