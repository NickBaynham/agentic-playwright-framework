# BDD Quality Checklist

Use during authoring or review of any BDD spec produced by the `exploratory-to-bdd` skill.

## Feature-level

- [ ] Feature has a clear, concise name.
- [ ] Business Goal is written in plain language and ties to user value.
- [ ] Source Material section references real artifacts (story, criteria, session log).
- [ ] Assumptions section is present and lists implicit dependencies.
- [ ] Open Questions section is present and lists unresolved ambiguity.
- [ ] Potential Defects section is present and separates suspected product issues from accepted behavior.

## Scenario-level

- [ ] Each scenario is focused on one behavior.
- [ ] Scenario name describes the behavior, not the steps.
- [ ] Given/When/Then steps are clear and ordered logically.
- [ ] Expected outcome is concrete and testable.
- [ ] No vague assertions ("it works", "looks correct").
- [ ] No invented requirements not present in the source.
- [ ] No hidden assumptions inside the steps.
- [ ] Test Data section identifies fields, values, and their source.
- [ ] Observed Evidence ties the scenario back to source artifacts.
- [ ] Scenario ID is unique and matches the traceability matrix.

## Traceability and Automation

- [ ] Every scenario appears in the traceability matrix.
- [ ] Status values in the matrix are from the allowed set.
- [ ] Automation Priority is set and justified.
- [ ] Automation Priority Rationale is one line and specific.

## Gherkin Hygiene

- [ ] No selectors (CSS, XPath, `data-test`) in Gherkin steps.
- [ ] No implementation detail unless required for clarity.
- [ ] Tags are consistent across scenarios.
- [ ] Scenario Outlines are used when the same behavior is tested with multiple data sets.
