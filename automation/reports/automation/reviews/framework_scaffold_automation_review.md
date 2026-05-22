# Automation Review: Framework Scaffold

## Summary

Reviewed the contents of `automation/` against all seven checklists from the `agentic-playwright-automation` skill. The scaffold is sound and matches the skill's mandated layout. No application page objects or feature tests exist yet — only configuration, framework base scaffolding, one framework-smoke test, test data, docs, and a setup report.

Three Medium-severity issues should be addressed before the first feature test lands:

- **M-1:** the local `headless: false` setting will be ignored by `pytest-playwright` because nothing bridges the resolved `Settings` to Playwright's launch fixtures.
- **M-2:** `framework/data/factories.py` defines a `CheckoutCustomer` dataclass that belongs under `framework/models/` per the test data standard.
- **M-3:** `framework/assertions/` is missing an `__init__.py`, so it will not be importable as a Python package when the first assertion helper is added.

Six Low-severity findings are polish.

The scoped checks for tests, page objects, locators, and locator decisions return "Not applicable" for most items because there are no application tests, page objects, or locators against the SUT yet.

Approval Recommendation: **Approved with Changes.**

## Scope of Review

- `automation/pyproject.toml`, `automation/pytest.ini`, `automation/Makefile`, `automation/.env.example`, `automation/.gitignore`, `automation/README.md`.
- `automation/config/{environments.yaml, settings.py}`.
- `automation/framework/pages/base_page.py`.
- `automation/framework/models/user.py`.
- `automation/framework/data/{test_data_loader.py, factories.py}`.
- `automation/framework/utils/{logger.py, paths.py, evidence.py}`.
- `automation/framework/reporting/{execution_summary.py, defect_summary.py}` (placeholders).
- `automation/framework/{assertions/README.md, clients/__init__.py, components/__init__.py}` (placeholders).
- `automation/tests/{conftest.py, ui/test_framework_smoke.py}`.
- `automation/test_data/local/users.yaml`.
- `automation/docs/*.md`.
- `automation/reports/automation/framework_setup_report.md`.

## Review Results

### Test Quality Checklist

Applied to `tests/ui/test_framework_smoke.py` (two functions) and the conftest fixtures it consumes. No feature tests exist, so SUT-level test-quality checks are not applicable.

| Check | Status | Notes |
|---|---|---|
| Test name reads as a behavior, not a series of steps | Pass | `test_settings_loads_local_environment`, `test_standard_user_loaded_from_test_data`. Both describe outcomes. |
| Arrange / Act / Assert flow is obvious | Pass | Each test has a single assertion phase consuming a single fixture. |
| Assertions live at the top level of the test | Pass | Both use `assert` on dataclass fields. Appropriate because these are data assertions, not UI assertions. |
| No business assertions hidden inside page object methods | Not applicable | No page objects involved. |
| No hard-coded URLs, credentials, product names, or checkout data | Pass | The username literal `"standard_user"` is a YAML key/identifier, not test data — it indexes the loader output. |
| PyTest markers present and appropriate | Pass with note | `@pytest.mark.smoke` only. `@pytest.mark.ui` is correctly omitted because no browser is driven. |
| No `time.sleep` and no `page.wait_for_timeout` | Pass | None present anywhere in the tree. |
| Expected result is deterministic and observable | Pass | `assert settings.environment in {"local","dev","qa"}`, `assert settings.base_url.startswith("http")`, dataclass field checks. |
| Source traceability appears in the docstring | Pass with note (L-3) | Module docstring references the setup report. Per-function docstrings have one-line summaries but no explicit Source block. |
| Related tests have been considered for impact | Not applicable | No related tests. |

### Page Object Quality Checklist

No concrete page objects exist; only `BasePage`. Items below evaluate `BasePage`.

| Check | Status | Notes |
|---|---|---|
| Class responsible for a single page or significant view | Not applicable | `BasePage` is the abstract base, not a page. |
| Important locators exposed as `@property` | Not applicable | No locators yet. |
| User actions are methods named for user intent | Not applicable | Only `open()`, which is the canonical navigation method on the base. |
| No business assertions hidden inside methods | Pass | `BasePage` defines no assertions. |
| No hard-coded URLs, credentials, or environment-specific data | Pass | `URL_PATH` defaults to `"/"`; base URL comes from the constructor. |
| Locator strategy follows the priority order | Not applicable | No locators yet. |
| No duplicate page objects | Pass | Only one class exists. |
| Class design is simple and readable | Pass | 18 lines, no surprising state. |
| Page object uses final locator decisions | Not applicable | No locators yet. |
| Repeated element locators scoped or disambiguated | Not applicable | No locators yet. |
| Dynamic or conditional element risks addressed | Not applicable | No locators yet. |

### Fixture Quality Checklist

Applied to `tests/conftest.py` — three fixtures: `settings`, `users`, `standard_user`.

| Check | Status | Notes |
|---|---|---|
| Fixture purpose clear from name and signature | Pass | Names describe resources; signatures show their dependencies. |
| Fixture name describes the resource (not the action) | Pass | All three are noun-form. |
| Fixture scope appropriate | Pass | `settings` is session-scoped (read-only config); `users` and `standard_user` are function-scoped. |
| Avoids unnecessary magic | Pass | No `autouse`, no metaclasses, no deep indirection. |
| No secrets baked into the fixture body | Pass | All values come from YAML / env. |
| Composed fixtures readable | Pass | At most two layers (`standard_user` ← `users` ← `settings`). |
| Reused across tests rather than duplicated | Pass | Both framework-smoke tests share the `settings`/`standard_user` fixtures. |

### Test Data Quality Checklist

Applied to `test_data/local/users.yaml` and `framework/data/{test_data_loader.py, factories.py}`.

| Check | Status | Notes |
|---|---|---|
| Data externalized to `automation/test_data/<environment>/` | Pass | `users.yaml` is under `test_data/local/`. |
| Environment-specific data in matching environment folder | Pass | Only `local/` has files; `dev/` and `qa/` are placeholders. |
| No private credentials, tokens, or PII committed | Pass | All six accounts are SauceDemo public demo credentials, published by the application itself. |
| Data shape aligns with a model in `framework/models/` | Pass with note (M-2) | `users` aligns with `framework/models/user.py`. **However**, `framework/data/factories.py` defines `CheckoutCustomer` inline rather than under `framework/models/`. See M-2. |
| Stable IDs/names used intentionally and documented | Pass | YAML keys match the demo's published usernames; documented in the file header. |
| Generated-data strategy documented next to the factory | Pass | The factory module docstring explains when to use it and that generated values are marked (UUID fragment in last name). |
| Cleanup/reset requirements identified next to the data | Pass | SauceDemo provides a `Reset App State` UI control; the data file does not need a cleanup contract. |

### Locator Quality Checklist

Not applicable yet — no locators against the SUT exist in any page object, component, fixture, or test. Re-apply this checklist when the first page object lands via `/convert-bdd-to-playwright`.

| Check | Status | Notes |
|---|---|---|
| `get_by_role(role, name=...)` preferred when available | Not applicable | No locators. |
| `get_by_label(...)` used for labelled form controls | Not applicable | No locators. |
| `get_by_placeholder(...)` used when label unavailable | Not applicable | No locators. |
| `get_by_text(...)` used only when stable and unambiguous | Not applicable | No locators. |
| `get_by_test_id(...)` used when accessible locators insufficient | Not applicable | No locators. |
| Stable CSS only when no accessible locator works | Not applicable | No locators. |
| XPath last resort, with explanatory comment | Not applicable | No locators. |
| Locator reflects user behavior rather than DOM structure | Not applicable | No locators. |
| Final locator selected after reviewing exploration candidates | Not applicable | No locators selected yet. |
| Locator decision recorded in implementation report | Not applicable | No implementation reports yet (other than the framework setup report). |

### Locator Decision Checklist

Not applicable at this stage. Will apply when page objects are first generated from the BDD spec. The Markdown spec at `specs/bdd/markdown/standard_user_checkout.md` already carries locator candidates as Automation Notes; the next implementation report must consume them and record decisions.

| Check | Status | Notes |
|---|---|---|
| Exploration locator candidates reviewed | Not applicable yet | Available in the source session report; will be consumed during the next implementation pass. |
| Markdown BDD Automation Notes reviewed | Not applicable yet | Available in `specs/bdd/markdown/standard_user_checkout.md`. |
| Final locator selected per element | Not applicable yet | No page objects yet. |
| Decision documented | Not applicable yet | No implementation report yet to record decisions. |
| Rationale included for each decision | Not applicable yet | — |
| Repeated elements scoped or disambiguated | Not applicable yet | — |
| Dynamic / conditional elements risks acknowledged | Not applicable yet | — |
| Accessible locators preferred when stable | Not applicable yet | — |
| `data-test` used to improve stability or disambiguation | Not applicable yet | — |
| Stable CSS only where accessible locators insufficient | Not applicable yet | — |
| XPath avoided unless unavoidable | Not applicable yet | — |
| Traceability from final locator to exploration candidate preserved | Not applicable yet | — |
| Page object uses final locator, not raw unreviewed candidate | Not applicable yet | — |

### Agent Safety Checklist

Applied to the scaffold run that produced this code.

| Check | Status | Notes |
|---|---|---|
| No broad unrelated refactors | Pass | Only `automation/` was created. |
| No new framework pattern invented when an existing one fits | Pass | All structural pieces match the skill's required structure. |
| No unrelated files deleted | Pass | Nothing was deleted; this was a greenfield scaffold. |
| No credentials, tokens, or PII exposed | Pass | Only saucedemo's publicly-published demo credentials appear in committed YAML; `.env` is in `.gitignore`. |
| No destructive data actions against shared environments | Pass | None performed. |
| No failures masked by weakening assertions / swallowing exceptions / adding waits | Pass | None present. |
| No unnecessary dependencies; versions pinned | Pass with note (L-5) | All declared dependencies are pinned. `pydantic` is declared but unused at this stage — see L-5. |
| No automatic git commit, push, or PR | Pass | None performed. |

## Issues Found

| ID | Severity | Issue | Recommendation |
|---|---|---|---|
| **M-1** | Medium | `pytest-playwright` reads its browser/headless settings from its own CLI flags and fixtures (`browser_type_launch_args`, `--headed`, `--browser`). The resolved `Settings.headless` and `Settings.browser` are not bridged to those fixtures. The `local` environment's `headless: false` will be silently ignored, and tests will run headless even when the developer expects a visible browser. | In `tests/conftest.py`, override `browser_type_launch_args` to consume `settings.headless`, and override `browser_name` to consume `settings.browser`. Add a brief note in `docs/fixture_standard.md`. Verify with `make test-debug` once feature tests exist. |
| **M-2** | Medium | `framework/data/factories.py` declares a `CheckoutCustomer` dataclass at module scope. Per `docs/test_data_standard.md` (and the skill's Test Data Rules), data models live under `framework/models/`. Two homes for the same kind of object will drift. | Move `CheckoutCustomer` into `framework/models/checkout_customer.py`. Re-export from `framework/data/factories.py` only if a single import path is desired; otherwise have callers import from `framework.models.checkout_customer` directly. |
| **M-3** | Medium | `framework/assertions/` contains only a `README.md`. There is no `__init__.py`, so `framework.assertions` is not importable as a Python package. The first time someone adds a helper, the missing marker file will cause an import error. | Add an empty `framework/assertions/__init__.py`. |
| **L-1** | Low | `pyproject.toml` includes `[tool.pytest.ini_options]` as an empty block with an explanatory comment, while `pytest.ini` is the canonical config. The empty TOML block is harmless but easy to misread as "no pytest config". | Either delete the empty `[tool.pytest.ini_options]` block, or replace it with a single key duplicating the `minversion` from `pytest.ini` so PDM users see something concrete. |
| **L-2** | Low | `pyproject.toml` defines a `[tool.pdm.scripts] install-browsers` entry, but the Makefile invokes the raw `pdm run playwright install --with-deps chromium`. Two paths to the same action drift. | Change the Makefile target to `pdm run install-browsers`, or delete the PDM script. Keep one. |
| **L-3** | Low | Per-function docstrings in `tests/ui/test_framework_smoke.py` lack the explicit `Source:` block recommended by the test template. The module-level docstring covers traceability, so the omission is minor. | Add a one-line Source block to each function docstring referencing the setup report (`reports/automation/framework_setup_report.md`). Keep the module docstring as well. |
| **L-4** | Low | The Makefile `clean` target removes `reports/*` and `__pycache__` / `.pytest_cache`, but not `.ruff_cache` and `.mypy_cache`. | Add the two extra `find ... -type d -name` lines to `clean`. |
| **L-5** | Low | `pydantic==2.10.4` is pinned in `pyproject.toml` but no code imports it. The skill lists it as optional (`pydantic` OR `dataclasses`). The scaffold uses `dataclasses`, so `pydantic` is dead weight. | Either remove `pydantic` from the dependency list (and update the setup report), or import it from the first data model that actually needs validation. Defer if `pydantic` is expected within the next one or two iterations. |
| **L-6** | Low | `framework/utils/evidence.py` provides `screenshot_path` / `save_screenshot` but no `pytest_runtest_makereport` hook wires them on failure. The setup report acknowledges this. | Wire the hook in `tests/conftest.py` when the first feature test lands. Defer for now. |

## Recommended Revisions

To move from Approved with Changes to Approved, apply the three Medium fixes (M-1, M-2, M-3) before the first feature test is generated by `/convert-bdd-to-playwright`. The Low fixes are polish and can land in the same revision.

Concrete sequence:

1. M-3 (add `framework/assertions/__init__.py`) — trivial.
2. M-2 (move `CheckoutCustomer` to `framework/models/checkout_customer.py`) — trivial.
3. M-1 (bridge `Settings` to `pytest-playwright` fixtures in `tests/conftest.py`) — small but requires verifying that `headed: false` actually launches headless on CI and that local `headless: false` launches a visible browser.
4. Pick up the Low items (L-1 through L-5) opportunistically; L-6 stays deferred until the first feature test lands.

## Approval Recommendation

**Approved with Changes.**

- The scaffold is structurally complete and matches the skill's mandate.
- Three Medium issues must be resolved before the first feature implementation; none of them block running the framework-smoke tests today, but all of them will bite the first feature test or the first locator decision.
- The six Low items are polish and may land in the same revision.
- The skill's Final Review Checklist passes for everything that applies at the scaffold stage: no `time.sleep`, no hard-coded URLs, no secrets committed, no Cucumber/Behave artifacts, no automatic git operations, no business assertions hidden in non-existent page objects.
