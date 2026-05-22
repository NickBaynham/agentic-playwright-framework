---
description: Investigate a failing Playwright/PyTest test. Classifies the failure, identifies the responsible layer, and produces a failure investigation report. Never weakens assertions and never adds sleeps to mask flakiness.
argument-hint: <test-path-or-report>
---

# /investigate-playwright-failure

Use the `agentic-playwright-automation` skill.

Arguments: `$ARGUMENTS`

## Behavior

1. Use the `agentic-playwright-automation` skill and its templates and checklists.
2. Re-run the failing test in isolation if execution is authorized.
3. Review PyTest failure output, screenshots under `automation/reports/screenshots/`, traces under `automation/reports/traces/`, videos if available, logs, environment configuration, test data, and the source BDD spec.
4. Classify the failure as exactly one of: `Product Defect`, `Test Data Issue`, `Locator Issue`, `Environment Issue`, `Timing/Flakiness`, `Framework Issue`, `Tooling Issue`, `Ambiguous Requirement`.
5. Do not weaken or remove any business assertion to make the test pass.
6. Do not add `time.sleep` or `page.wait_for_timeout` to mask timing.
7. Fix only the layer responsible for the failure. If the application appears defective, write a Potential Defect note instead of changing the test.
8. Apply `checklists/failure_investigation_checklist.md` before concluding.
9. Do not perform any git commit, push, or pull request.
10. Write a failure investigation report at `automation/reports/automation/failures/<failure_name>_investigation.md` using `templates/failure_investigation_template.md`.

## Output Summary

Finish by listing: the investigation report path, the failure category, the responsible layer, changes made (if any), commands run, and follow-up items (including any Potential Defect notes).
