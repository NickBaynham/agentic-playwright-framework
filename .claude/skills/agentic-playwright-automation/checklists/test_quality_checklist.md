# Test Quality Checklist

Apply per test function. Mark each item Pass, Fail, or Needs Review.

| Check | Status | Notes |
|---|---|---|
| Test name reads as a behavior, not a series of steps | | |
| Arrange / Act / Assert flow is obvious | | |
| Assertions live at the top level of the test | | |
| No business assertions are hidden inside page object methods | | |
| No hard-coded URLs, credentials, product names, or checkout data | | |
| PyTest markers are present and appropriate (`ui`, `api`, `smoke`, `regression`, area markers) | | |
| No `time.sleep` and no `page.wait_for_timeout` | | |
| Expected result is deterministic and observable | | |
| Source traceability appears in the docstring (BDD path, scenario ID, story ID) | | |
| Related tests have been considered for impact | | |
