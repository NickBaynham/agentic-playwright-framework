---
description: Bridge an MCP exploration session report into BDD artifacts by handing off to the exploratory-to-bdd skill. Does not generate Playwright or PyTest automation code.
argument-hint: <exploration-session-file>
---

# /exploration-to-bdd

This command bridges two skills:

- The `mcp-exploratory-testing` skill is responsible for observation and exploration artifacts.
- The `exploratory-to-bdd` skill is responsible for generating BDD specs and supporting artifacts.

This command reads an MCP exploration session report and hands off to the `exploratory-to-bdd` skill.

Arguments: `$ARGUMENTS`

## Behavior

1. Read the exploration session file at the path supplied as the argument.
2. Confirm the report contains enough information for BDD conversion: scope, at least one Page Observation, an Action Timeline, Observed Outcomes, Test Data Used, and at least one Candidate Test Case with an observable expected result.
3. If sufficient, use the `exploratory-to-bdd` skill to generate, under `specs/bdd/`:
   - Markdown BDD spec at `specs/bdd/markdown/<feature_name>.md`
   - Gherkin feature file at `specs/bdd/features/<feature_name>.feature`
   - Traceability matrix at `specs/bdd/traceability/<feature_name>_traceability_matrix.md`
   - Automation candidate review at `specs/bdd/automation/<feature_name>_automation_candidates.md`
   - BDD quality review at `specs/bdd/reviews/<feature_name>_bdd_quality_review.md`
4. If not sufficient, do not generate BDD artifacts. Instead, use the `mcp-exploratory-testing` skill to write an exploration review at `reports/exploration/<app-name>/<workflow-name>_review.md` describing the missing information and recommending a focused re-exploration.
5. Do not generate Playwright or PyTest automation code under any circumstances.

## Output Summary

If BDD artifacts were generated, list each file created, the scenarios discovered, any open questions, any potential defects, and the recommended automation priority for each scenario.

If BDD artifacts were not generated, list the review file path, the missing information, and a recommended re-exploration scope.
