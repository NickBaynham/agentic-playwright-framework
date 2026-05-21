---
description: Review existing BDD specs and feature files for quality, ambiguity, traceability, and automation readiness.
argument-hint: <bdd-file-or-folder>
---

# /review-bdd

Use the `exploratory-to-bdd` skill.

Arguments: `$ARGUMENTS`

## Behavior

1. Read the BDD artifacts at the supplied path. Accept either a single file or a folder containing Markdown specs and/or `.feature` files.
2. Apply `.claude/skills/exploratory-to-bdd/checklists/bdd_quality_checklist.md`.
3. Apply `.claude/skills/exploratory-to-bdd/checklists/ambiguity_and_defect_checklist.md`.
4. Identify ambiguity, duplication, broad scenarios, missing test data, vague expected outcomes, and invented requirements.
5. Recommend concrete revisions.
6. Write or update a BDD quality review file at `specs/bdd/reviews/<feature_name>_bdd_quality_review.md` using `templates/bdd_quality_review_template.md`.
7. Do not modify the source BDD spec or feature file unless explicitly asked.
8. End with an Approval Recommendation: Approved, Approved with Changes, or Needs Rework.

## Output Summary

Finish by listing the reviewed files, the review file written, the count of issues found by severity, and the Approval Recommendation.
