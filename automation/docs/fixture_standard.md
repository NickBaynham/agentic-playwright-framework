# Fixture Standard

## Location

- Shared fixtures live in `tests/conftest.py`.
- Feature-scoped fixtures live in a `conftest.py` next to the tests that use them (e.g., `tests/ui/checkout/conftest.py`).

## Naming

- Fixture names describe the resource, not the action: `standard_user`, `login_page`, `settings`, `api_client`, `cart_with_backpack`.
- Avoid verb-style fixture names. A fixture provides; a function acts.

## Scopes

- Default scope is `function`.
- Use `session` only for read-only, expensive resources (the resolved `settings`, a long-lived HTTP client).
- Use `module` or `class` only when sharing is genuinely safe across the scope.

## Configuration

- Configuration fixtures read from `config.settings` and environment variables. Never embed literals.
- Page-object fixtures receive `page` (from `pytest-playwright`) and `settings`, and construct the page object using the resolved `base_url`.
- Test-data fixtures load from `test_data/<env>/` through `framework.data.test_data_loader`.

## Secrets

- Never store secrets in fixtures.
- Read sensitive values from `os.environ`; populate via a local `.env` (not committed) or a secret manager.
- Public demo credentials (saucedemo's `standard_user / secret_sauce`) are acceptable in committed YAML because the application publishes them.

## Depth

- A test should be readable without reading three layers of fixtures.
- If a fixture depends on three or more other fixtures, ask whether one of them is unnecessary indirection.
