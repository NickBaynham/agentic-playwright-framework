---
description: Convert reviewed BDD specs and Gherkin .feature files into Playwright/PyTest automation under automation/. Implements only High-priority, automatable scenarios with traceability. Does not introduce Cucumber/Behave or generate step definitions.
argument-hint: <bdd-file-or-folder>
---

# /convert-bdd-to-playwright

Use the `agentic-playwright-automation` skill.

Arguments: `$ARGUMENTS`

## Behavior

1. Use the `agentic-playwright-automation` skill and its templates and checklists.
2. Read the Markdown BDD specs under `specs/bdd/markdown/` and the corresponding `.feature` files under `specs/bdd/features/` for the supplied path.
3. Read the traceability matrix in `specs/bdd/traceability/` and the automation candidate review in `specs/bdd/automation/` if available.
4. Implement only scenarios that are all of: `High` priority, marked `@automatable`, not marked `@needs-clarification`, not marked `Do Not Automate`.
5. Generate or update: tests under `automation/tests/`, page objects under `automation/framework/pages/`, components under `automation/framework/components/` if needed, data models under `automation/framework/models/`, test data under `automation/test_data/<environment>/`, fixtures in the appropriate `conftest.py`.
6. Keep business assertions at the top level of the test using Playwright `expect`.
7. Preserve source traceability in every test docstring: BDD spec path, scenario name, Scenario ID.
8. Run generated tests when execution is authorized.
9. Do not introduce Cucumber/Behave runtime or generate step definitions.
10. Do not perform any git commit, push, or pull request.
11. Write an implementation report at `automation/reports/automation/<feature>_<scenario>_implementation_report.md` per scenario, plus a suite report when more than one scenario is implemented in the same run.

## Output Summary

Finish by listing: scenarios implemented, scenarios skipped (with reason), files created or modified, test results (if run), the implementation reports written, and any Open Questions or Potential Defects.
