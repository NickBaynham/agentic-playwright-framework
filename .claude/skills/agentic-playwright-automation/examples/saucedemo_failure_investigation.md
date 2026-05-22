# Playwright Failure Investigation: SauceDemo Login Smoke Flaky on Finish Click

## Failed Test

`automation/tests/ui/test_saucedemo_checkout.py::test_standard_user_completes_checkout`

## Failure Summary

The Finish click on `/checkout-step-two.html` intermittently does not navigate to `/checkout-complete.html`. Playwright reports the click as successful, but the Order Confirmation page never renders. The next `expect` on the confirmation heading times out.

## Failure Category

Tooling Issue (Playwright click did not trigger the React handler in MCP-style exploration of the same control). Possible secondary Timing/Flakiness if a React state update is delayed.

## Evidence Reviewed

- PyTest output: `automation/reports/junit/test_saucedemo_checkout.xml`
- Screenshot: `automation/reports/screenshots/test_standard_user_completes_checkout.png`
- Trace: `automation/reports/traces/test_standard_user_completes_checkout.zip`
- Video: not enabled for this run
- Logs: PyTest live log
- Test data: `automation/test_data/local/users.yaml`, `automation/test_data/local/checkout_customers.yaml`
- Config: `automation/config/environments.yaml` (`local`)
- Source BDD/spec: `specs/bdd/markdown/saucedemo_checkout.md`

## Expected Behavior

After clicking Finish on the checkout overview, the user is navigated to `/checkout-complete.html` and "Thank you for your order!" is visible.

## Actual Behavior

Click is reported successful. Page does not navigate. The confirmation heading assertion times out.

## Root Cause Assessment

Reproduced once in three runs. Two clean runs use the same fixtures, same data, and the same locator. The exploratory session noted the same symptom when driving Finish through Playwright MCP. Suspected interaction-layer issue with this specific control rather than the application logic, but the application repaint may also be a factor.

## Recommended Action

1. Keep the existing assertion. Do not weaken or remove it.
2. Replace the click with `expect(self.finish_button).to_be_enabled()` followed by `self.finish_button.click()` to leverage Playwright auto-waiting against the actual control state.
3. If the failure persists, add a single `expect(self.page).to_have_url(re.compile(r"/checkout-complete\\.html$"))` immediately after the click, which surfaces a clearer failure boundary and forces Playwright auto-waiting on the URL.
4. Do not add `time.sleep` or `wait_for_timeout`.
5. Open a Potential Defect note if the application Finish handler genuinely drops the click on real users.

## Changes Made

| File | Change |
|---|---|
| `automation/framework/pages/checkout_overview_page.py` | Added explicit enabled-state guard before the Finish click. |
| `automation/tests/ui/test_saucedemo_checkout.py` | No assertion weakening. Added a focused URL expectation after Finish. |

## Commands Run

| Command | Result |
|---|---|
| `pytest tests/ui/test_saucedemo_checkout.py::test_standard_user_completes_checkout -x` | Passed 5/5 after the fix on local. |
| `pytest tests/ui -k checkout` | Passed. |

## Follow-Up

- Re-run nightly for one week and re-evaluate.
- If the symptom recurs without the URL guard catching it, raise as Potential Defect to product engineering with the trace artifact attached.
