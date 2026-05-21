# Ambiguity and Defect Checklist

Use to surface unresolved questions and suspected product issues during BDD authoring or review.

## Behavior Clarity

- [ ] Does observed behavior differ from expected behavior?
- [ ] Is expected behavior actually documented anywhere?
- [ ] Is the expected outcome deterministic and unambiguous?
- [ ] Is UI behavior consistent across runs and environments?
- [ ] Are state changes immediate, or are they delayed in a way that needs documentation?

## Data and Roles

- [ ] Are the required data inputs known?
- [ ] Are user roles, permissions, or feature flags clearly defined for the scenario?
- [ ] Are there edge cases (empty, invalid, boundary) that are unspecified?

## Error Handling

- [ ] Is error handling defined for invalid input?
- [ ] Is error messaging defined and reviewable?
- [ ] Are recovery paths defined?

## Environment

- [ ] Does the behavior depend on environment (browser, OS, locale, timezone)?
- [ ] Are network conditions or backend availability assumptions documented?

## Terminology and Sources

- [ ] Is product terminology consistent with the source material?
- [ ] Are conflicting acceptance criteria flagged for clarification?

## Defect Capture

- [ ] If observed behavior contradicts intended behavior, has it been listed under Potential Defects?
- [ ] Has the related scenario been tagged `@potential-defect`?
- [ ] Has a separate defect record been recommended (without auto-filing in v0.1)?
