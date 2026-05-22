# Framework Rules

These are the rules every test, page object, fixture, and data file in this framework must follow. They are summarized from the `agentic-playwright-automation` skill.

## Language and Runtime

- Python 3.11+, PyTest as the runner, Playwright sync API.
- PDM for package management; dependency versions pinned in `pyproject.toml`.

## Tests

- One behavior per test function.
- Arrange / Act / Assert structure with blank lines separating phases.
- Test names start with `test_` and describe behavior, not steps.
- Business assertions live at the top level of the test, expressed with `playwright.sync_api.expect` for UI and `assert` for data.
- Every test has a docstring that references its source spec (BDD Markdown path, Scenario ID, or exploration artifact path).
- No `time.sleep`. No `page.wait_for_timeout`. Use auto-waiting via `expect` and `locator.wait_for`.
- Use PyTest markers from `pytest.ini` (`ui`, `api`, `smoke`, `regression`, `negative`, `login`, `cart`, `checkout`, `inventory`, `needs_clarification`, `potential_defect`).

## Page Objects

- One class per page or significant view, inheriting from `BasePage`.
- Locators exposed as `@property`.
- Methods named for user intent (`login_as(user)`, `add_to_cart(product)`).
- No business assertions inside page object methods.
- No environment-specific values inside page objects.

## Components

- One class per reusable region (nav bar, modal, product card, cart drawer).
- Constructor accepts the parent `Page` and a root `Locator`.
- Components do not perform full-page navigation and do not own business assertions.

## Fixtures

- Fixtures live in `tests/conftest.py` or a scoped `conftest.py`.
- Default scope is `function`; broaden only for safe-to-share, expensive resources.
- Fixtures read configuration from `config.settings`, not from literals.
- Never store secrets in fixtures; read from environment variables or a local `.env`.

## Test Data

- All test data lives under `test_data/<environment>/` as YAML.
- Data is loaded through `framework/data/test_data_loader.py` and surfaced via dataclass models from `framework/models/`.
- No private credentials, tokens, or PII in committed YAML.

## Locator Strategy

See `locator_strategy.md`. In short: prefer `get_by_role(role, name=...)`, then `get_by_label`, `get_by_placeholder`, `get_by_text`, `get_by_test_id`, then stable CSS, then XPath only as a last resort.

## Traceability

Every test docstring references its source. Implementation reports under `reports/automation/` list each test and its source scenario.

## Agent Safety

- No broad unrelated refactors.
- No invented framework patterns when an existing one fits.
- No credentials in code, fixtures, reports, or commit messages.
- No destructive operations against shared environments without explicit authorization.
- No assertion weakening, exception swallowing, or sleeps to mask failures.
- No automatic git commits, pushes, or PRs unless explicitly requested.
