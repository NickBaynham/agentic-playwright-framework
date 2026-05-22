---
description: Review an existing MCP exploration artifact (a single session report or a folder of reports) for completeness and quality, and write or update an exploration review report.
argument-hint: <exploration-file-or-folder>
---

# /review-exploration

Use the `mcp-exploratory-testing` skill.

Arguments: `$ARGUMENTS`

## Behavior

1. Use the `mcp-exploratory-testing` skill and its templates and checklists.
2. Read the provided exploration artifact at the path supplied as the argument. The path may be a single session report file or a folder of session and report files.
3. Apply `templates/exploration_review_template.md` from the skill.
4. Apply the following checklists from the skill:
   - `checklists/exploration_scope_checklist.md`
   - `checklists/observation_quality_checklist.md`
   - `checklists/anomaly_classification_checklist.md`
   - `checklists/test_idea_quality_checklist.md`
   - `checklists/locator_candidate_checklist.md`
5. Identify gaps, ambiguity, missing data, missing outcomes, missing anomalies, weak evidence, conflated application and tooling anomalies, and candidate test cases without observable expected results.
5a. Review whether locator candidates were captured for meaningful workflow elements.
5b. Review whether locator confidence, rationale, repeated-element notes, and dynamic-element risks were documented.
5c. Confirm that locator candidates are clearly marked as non-final (not as final automation locators).
6. Write or update the review file at `reports/exploration/<app-name>/<workflow-name>_review.md`. Create directories as needed.
7. Do not generate BDD specs unless the user explicitly asks.
8. Do not generate Playwright or PyTest automation code.

## Output Summary

Finish by listing: the review file path, each check with its status, identified gaps with impact and recommendation, and a recommended next step (re-explore, hand off to `exploratory-to-bdd`, treat anomaly as a Potential Defect, or close).
