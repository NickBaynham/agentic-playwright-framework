---
description: Generate a small suite of Playwright/PyTest tests from approved BDD specs or an automation candidate file. Implements only High-priority, automatable scenarios; skips Do Not Automate and Needs Clarification. Does not introduce Cucumber/Behave.
argument-hint: <bdd-folder-or-automation-candidate-file>
---

# /generate-playwright-suite

Use the `agentic-playwright-automation` skill.

Arguments: `$ARGUMENTS`

## Behavior

1. Use the `agentic-playwright-automation` skill and its templates and checklists.
2. Read approved BDD specs in `specs/bdd/markdown/` and the corresponding automation candidate review in `specs/bdd/automation/`.
3. Select scenarios that satisfy all of: marked `High` priority, marked `@automatable`, not marked `@needs-clarification`, not marked `Do Not Automate`. The user may explicitly approve a non-default scenario for inclusion.
4. Inspect the existing automation framework.
5. Produce an implementation plan listing each selected scenario, the reusable assets to use, and any new assets to introduce.
6. Generate tests one at a time. After each generated test, run it in isolation if execution is authorized. Do not proceed to the next test if the prior test is failing without an investigation.
7. Reuse existing page objects, components, fixtures, models, and data. Avoid duplication.
8. Run the related suite when authorized after the last test is generated.
9. Do not perform any git commit, push, or pull request.
10. Write per-scenario implementation reports (when scenarios are non-trivial) and a single suite implementation report at `automation/reports/automation/<feature>_suite_implementation_report.md`.

## Output Summary

Finish by listing: scenarios implemented, scenarios skipped (with reason), files created or modified, fixtures touched, suite execution results (if run), and the suite implementation report path.
