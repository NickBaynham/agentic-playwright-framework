---
description: Explore an application with Playwright MCP and convert the session into BDD specs, traceability, automation candidates, and a quality review.
argument-hint: <target-url> <scope-or-user-story>
---

# /explore-to-bdd

Use the `exploratory-to-bdd` skill.

Arguments: `$ARGUMENTS`

## Behavior

1. Use the Playwright MCP if available (`browser_navigate`, `browser_snapshot`, `browser_click`, `browser_fill_form`, `browser_evaluate`). If the MCP is not available, abort and tell the user.
2. Open the target URL supplied by the user as the first argument.
3. Explore only the scope described by the user (second argument). Do not wander outside that scope.
4. As you go, record: pages visited, user actions performed, outcomes observed, data needed, and anomalies.
5. Generate BDD artifacts using the `exploratory-to-bdd` skill:
   - Markdown BDD spec → `specs/bdd/markdown/<feature_name>.md`
   - Gherkin feature → `specs/bdd/features/<feature_name>.feature`
   - Traceability matrix → `specs/bdd/traceability/<feature_name>_traceability_matrix.md`
   - Automation candidate review → `specs/bdd/automation/<feature_name>_automation_candidates.md`
   - BDD quality review → `specs/bdd/reviews/<feature_name>_bdd_quality_review.md`
6. Do not generate Playwright or PyTest automation code.

## Scope Guidance

If the user has not provided enough scope, inspect only the smallest obvious workflow and clearly document Assumptions and Open Questions in the Markdown spec. Do not invent missing requirements.

## Output Summary

Finish by listing the files created, the scenarios discovered, any open questions, any potential defects, and the recommended automation priority for each scenario.
