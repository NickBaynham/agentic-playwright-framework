# Failure Investigation

A failing test is data, not a problem to make disappear. Investigate before changing anything.

## Reproduce

Run the failing test in isolation before touching code:

```
pdm run pytest tests/ui/test_<feature>.py::test_<name> -s
PWDEBUG=1 pdm run pytest tests/ui/test_<feature>.py::test_<name> -s
```

Check that the failure is consistent across two or three runs. Intermittent failures change the classification.

## Gather evidence

- PyTest output and the failure traceback.
- The Playwright trace under `reports/traces/`.
- Screenshots under `reports/screenshots/`.
- Browser console messages and network requests if captured.
- The source BDD spec, exploration report, and any related anomalies.
- The current environment configuration (`APP_ENV`, `config/environments.yaml`, `.env` overrides).

## Classify

Pick exactly one of the eight categories:

- **Product Defect** — the application's observable behavior does not match the BDD scenario or stated requirement.
- **Test Data Issue** — the test consumed data that did not satisfy the precondition (wrong user, stale fixture, missing seed).
- **Locator Issue** — the locator no longer matches the intended element (renamed control, missing `data-test`, structural change).
- **Environment Issue** — the environment differed from the assumption (wrong base URL, dependent service down, browser binary mismatch).
- **Timing/Flakiness** — race or auto-waiting boundary; the test passes when state is given a moment to settle. Note: the fix is to wait on the right state, not to add a sleep.
- **Framework Issue** — a defect in the framework code (broken fixture, faulty data loader).
- **Tooling Issue** — a defect in Playwright, pytest, or another dependency.
- **Ambiguous Requirement** — the spec itself does not define a deterministic expected outcome.

## Fix the right layer

- Product Defect: file or note a Potential Defect. Do not change the test to match the buggy behavior.
- Test Data: update `test_data/<env>/`.
- Locator: update the page object or component.
- Environment: update `config/` or `.env` (per-developer overrides, not committed secrets).
- Timing/Flakiness: change the test to wait on the right observable, not an arbitrary duration.
- Framework / Tooling: fix the layer; do not work around it in the test.
- Ambiguous Requirement: open a question on the BDD spec; do not invent a requirement.

## Forbidden moves

- Adding `time.sleep` or `page.wait_for_timeout` to mask a flake.
- Weakening or removing a business assertion to make a test pass.
- Catching and ignoring an exception in the test to hide a failure.
- Modifying the source BDD spec to match buggy behavior.

## Document

Write `reports/automation/failures/<failure_name>_investigation.md` using `templates/failure_investigation_template.md` from the skill. Include reproduction commands, evidence references, classification, the layer changed, and a one-line summary of the fix.
