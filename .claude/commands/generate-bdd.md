---
description: Convert existing exploration notes, user stories, or acceptance criteria into BDD specs, traceability, automation candidates, and a quality review.
argument-hint: <source-file-or-description>
---

# /generate-bdd

Use the `exploratory-to-bdd` skill.

Arguments: `$ARGUMENTS`

## Behavior

1. Read the source provided by the user. The argument may be a file path, a folder path, or an inline description.
2. Identify features, scenarios, assumptions, data needs, and expected outcomes from the source.
3. Generate BDD artifacts using the `exploratory-to-bdd` skill:
   - Markdown BDD spec → `specs/bdd/markdown/<feature_name>.md`
   - Gherkin feature → `specs/bdd/features/<feature_name>.feature`
   - Traceability matrix → `specs/bdd/traceability/<feature_name>_traceability_matrix.md`
   - Automation candidate review → `specs/bdd/automation/<feature_name>_automation_candidates.md`
   - BDD quality review → `specs/bdd/reviews/<feature_name>_bdd_quality_review.md`
4. Preserve traceability back to the source in the matrix.
5. Surface Open Questions and Potential Defects rather than guessing.
6. Do not generate Playwright or PyTest automation code.

## Output Summary

Finish by listing the files created, the scenarios discovered, and any items flagged for clarification or as potential defects.
