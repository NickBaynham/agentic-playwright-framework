---
description: Create or review the Python Playwright/PyTest automation framework under automation/. Adds missing structure, PDM configuration, Makefile, docs, base classes, and example tests. Does not install packages or run tests unless explicitly authorized.
argument-hint: <optional-app-name-or-target-url>
---

# /setup-playwright-framework

Use the `agentic-playwright-automation` skill.

Arguments: `$ARGUMENTS`

## Behavior

1. Use the `agentic-playwright-automation` skill and its templates and checklists.
2. Inspect the current repository before creating any files. If `automation/` already exists, read what is present and do not overwrite a user file without showing the change first.
3. Create only the missing pieces of the framework structure documented in the skill (`automation/{README.md, pyproject.toml, pytest.ini, Makefile, .env.example, config/, framework/, tests/, test_data/, reports/, docs/}`).
4. Configure PDM as the package manager unless the project already uses another tool. Pin versions in `pyproject.toml`. Dependencies: `playwright`, `pytest`, `pytest-playwright`, `pytest-html`, `pytest-xdist`, `pyyaml`, `python-dotenv`, `pydantic` (or stdlib `dataclasses`), `ruff`, and `mypy` (optional).
5. Add `Makefile` targets: `install`, `lint`, `format`, `test`, `test-ui`, `test-api`, `test-smoke`, `test-report`, `test-debug`.
6. Create docs under `automation/docs/`: `framework_rules.md`, `adding_tests.md`, `page_object_standard.md`, `fixture_standard.md`, `test_data_standard.md`, `locator_strategy.md`, `failure_investigation.md`.
7. Seed minimal examples only: a base page, a sample fixture, a single example test. Do not generate a large test suite from this command.
8. Do not install packages and do not run tests unless the user explicitly authorizes execution.
9. Do not perform any git commit, push, or pull request.
10. Write a setup report at `automation/reports/automation/framework_setup_report.md`.

## Output Summary

Finish by listing: the framework files created, the docs created, the Makefile targets, the dependency set, anything intentionally left untouched, and the setup report path.
