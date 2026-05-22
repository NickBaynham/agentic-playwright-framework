---
description: Review existing Playwright/PyTest automation for quality, maintainability, and framework compliance. Produces an automation review report with an Approval Recommendation. Does not modify code unless explicitly asked.
argument-hint: <test-file-or-folder>
---

# /review-playwright-test

Use the `agentic-playwright-automation` skill.

Arguments: `$ARGUMENTS`

## Behavior

1. Use the `agentic-playwright-automation` skill and its templates and checklists.
2. Read the selected tests plus related page objects, components, fixtures, data, and config.
3. Apply the following checklists:
   - `checklists/test_quality_checklist.md`
   - `checklists/page_object_quality_checklist.md`
   - `checklists/fixture_quality_checklist.md`
   - `checklists/test_data_quality_checklist.md`
   - `checklists/locator_quality_checklist.md`
   - `checklists/agent_safety_checklist.md`
4. Identify: hidden assertions, hard-coded data, brittle locators, duplicated code, over-engineered abstractions, fixture confusion, missing traceability, missing markers.
5. Write an automation review report at `automation/reports/automation/reviews/<target>_automation_review.md` using `templates/automation_review_template.md`.
6. End with an Approval Recommendation: Approved, Approved with Changes, or Needs Rework.
7. Do not modify code unless the user explicitly asks for fixes in this command invocation.

## Output Summary

Finish by listing: the review report path, every check with its status, issues found with severity and recommendation, and the final Approval Recommendation.
