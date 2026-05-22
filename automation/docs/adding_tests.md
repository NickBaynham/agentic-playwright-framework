# Adding a Test

Follow this flow whenever you add a new test to the suite.

## 1. Start from an approved BDD scenario

Find the source spec under `specs/bdd/markdown/<feature>.md`. The scenario you implement must be tagged `@automatable` and not `@needs-clarification` or `@do-not-automate`. If the spec is missing or incomplete, update it via the `exploratory-to-bdd` skill before writing code.

## 2. Inspect existing assets

Before creating a new page object, component, fixture, model, or data file, check whether one already exists. Reuse beats new code. Look in:

- `framework/pages/` for page objects.
- `framework/components/` for reusable UI regions.
- `framework/models/` for data models.
- `framework/data/` for loaders and factories.
- `tests/conftest.py` for shared fixtures.
- `test_data/<env>/` for canonical seed data.

## 3. Plan the smallest change

Write the smallest plan that implements the behavior. If you find yourself adding a second page object, component, or fixture, ask whether one of them can be deferred until a second test motivates it.

## 4. Implement

Create or update:

- Test file under `tests/ui/` (or `tests/api/`).
- Page object(s) under `framework/pages/`.
- Component(s) under `framework/components/`, if a region is shared.
- Fixtures in `tests/conftest.py` or a scoped `conftest.py` near the test.
- Data models under `framework/models/`.
- Test data under `test_data/<env>/`.

## 5. Locator decisions

Read locator candidates from the source exploration report and the Markdown spec's Automation Notes. Compare each candidate against the locator strategy. Record every final locator decision in the implementation report's Locator Decision Log with one of: Accepted, Accepted with Scope, Modified, Rejected, Needs Review.

## 6. Test docstring

Include traceability in the test docstring:

```
Source:
    BDD Spec: specs/bdd/markdown/<feature>.md
    Feature:  specs/bdd/features/<feature>.feature
    Scenario: <Scenario name or Scenario ID>
```

## 7. Run

When authorized to execute:

```
make test-ui                                          # all UI tests
pdm run pytest tests/ui/test_<feature>.py -k <name>   # one test
```

If the new test fails, do not weaken assertions. Investigate using `/investigate-playwright-failure` and write the failure investigation report.

## 8. Write the implementation report

Generate `reports/automation/<feature>_<scenario>_implementation_report.md` using `templates/implementation_report_template.md` from the skill. Include the Locator Decision Log, Locator Risks Carried Forward, files created or modified, test results, and any open questions.
