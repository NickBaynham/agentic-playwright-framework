# Failure Investigation Checklist

Apply per failing test. Mark each item Pass, Fail, or Needs Review.

| Check | Status | Notes |
|---|---|---|
| Failure is reproduced in isolation | | |
| PyTest output is reviewed | | |
| Screenshot, trace, and video are reviewed if available | | |
| Environment configuration is checked | | |
| Test data is checked | | |
| Locator is checked against current page | | |
| Source BDD spec or requirement is checked | | |
| Failure is classified (Product Defect, Test Data, Locator, Environment, Timing/Flakiness, Framework, Tooling, Ambiguous Requirement) | | |
| Assertion was not weakened to make the test pass | | |
| Sleep or arbitrary wait was not added to mask timing | | |
| Correct layer was identified before any fix was made | | |
| Potential Defect or clarification request was raised when application behavior is suspect | | |
