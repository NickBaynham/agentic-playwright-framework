# Custom assertions

Tests should use Playwright's `expect` from `playwright.sync_api` for UI assertions and Python's `assert` for data assertions on models or API responses.

Only introduce a custom assertion helper in this package when a behavior assertion is repeated across multiple tests in a way that obscures intent — for example, parsing the three currency strings (Item total, Tax, Total) on the checkout overview and asserting their arithmetic relationship.

Custom assertion helpers must remain thin. They must not hide the source values; tests should still be able to read those values back. They must not own business contracts; the test is still the authoritative caller of the assertion.

Avoid adding a helper for a one-off use. Avoid adding a helper that simply wraps a single `expect` call.
