# Automation Candidate Checklist

Use to evaluate whether a scenario should be automated and at what priority.

## Value

- [ ] Is the scenario business-critical?
- [ ] Does failure of this scenario impact revenue, security, or compliance?
- [ ] Does this scenario provide meaningful regression coverage?
- [ ] Is the scenario suitable for CI gating?

## Stability

- [ ] Is the underlying feature stable enough that the test will not be repeatedly rewritten?
- [ ] Is the UI area for this scenario unlikely to churn?
- [ ] Is the expected result deterministic across runs?
- [ ] Are the required test data and environment reliably available?

## Repeatability

- [ ] Can the scenario be reset to a known state before each run?
- [ ] Can the test data be provisioned reliably (fixtures, seeded users, mocks)?
- [ ] Are external dependencies controllable or mockable?

## Level of Testing

- [ ] Would this scenario be cheaper and more reliable as an API test instead of a UI test?
- [ ] Would a unit or integration test cover the underlying behavior more directly?
- [ ] Is manual exploration more appropriate for this scenario (subjective, visual, or unstable)?

## Maintenance Risk

- [ ] How often is the surface being tested expected to change?
- [ ] Are there enough stable hooks (`data-test`, accessible labels) to write a durable test?
- [ ] Is the scenario likely to become flaky?

## Final Classification

- [ ] Priority assigned: High / Medium / Low / Do Not Automate.
- [ ] Recommended automation type assigned: Playwright UI / API / Unit / Integration / Manual / Do Not Automate / Needs Clarification.
- [ ] Rationale recorded.
