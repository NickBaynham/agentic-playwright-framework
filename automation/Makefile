SHELL := /bin/bash
APP_ENV ?= local

.PHONY: help install install-browsers lint format test test-ui test-api test-smoke test-report test-debug clean

help:
	@echo "Targets:"
	@echo "  install           Install Python dependencies via PDM."
	@echo "  install-browsers  Install Playwright browser binaries."
	@echo "  lint              Run ruff lint checks."
	@echo "  format            Run ruff format."
	@echo "  test              Run the full test suite."
	@echo "  test-ui           Run UI tests only."
	@echo "  test-api          Run API tests only."
	@echo "  test-smoke        Run smoke-marked tests."
	@echo "  test-report       Run tests and open the HTML report."
	@echo "  test-debug        Run tests in Playwright debug mode (PWDEBUG=1)."
	@echo "  clean             Remove generated report artifacts."

install:
	pdm install -d

install-browsers:
	pdm run install-browsers

lint:
	pdm run ruff check .

format:
	pdm run ruff format .

test:
	APP_ENV=$(APP_ENV) pdm run pytest

test-ui:
	APP_ENV=$(APP_ENV) pdm run pytest -m ui

test-api:
	APP_ENV=$(APP_ENV) pdm run pytest -m api

test-smoke:
	APP_ENV=$(APP_ENV) pdm run pytest -m smoke

test-report:
	APP_ENV=$(APP_ENV) pdm run pytest
	@echo "Open reports/html/report.html in your browser."

test-debug:
	APP_ENV=$(APP_ENV) PWDEBUG=1 pdm run pytest -s

clean:
	rm -rf reports/html/* reports/junit/* reports/traces/* reports/screenshots/*
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name .ruff_cache -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +
