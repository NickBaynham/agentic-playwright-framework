"""Framework smoke check.

This file ships with the framework scaffold. It does not exercise the
application under test. Its purpose is to confirm that pytest, the
environment loader, and the test-data loader wire together correctly.

Replace this with real scenario tests as they are implemented from the
BDD specs under ``specs/bdd/markdown/``.

Source:
    Framework scaffold — see ``automation/reports/automation/framework_setup_report.md``.
"""

from __future__ import annotations

import pytest

from config.settings import Settings
from framework.models.user import User


@pytest.mark.smoke
def test_settings_loads_local_environment(settings: Settings) -> None:
    """Settings load resolves a non-empty base URL for the active environment.

    Source:
        Framework scaffold — see reports/automation/framework_setup_report.md.
    """
    assert settings.environment in {"local", "dev", "qa"}
    assert settings.base_url.startswith("http")


@pytest.mark.smoke
def test_standard_user_loaded_from_test_data(standard_user: User) -> None:
    """The standard_user fixture is loaded from YAML and surfaces as a User model.

    Source:
        Framework scaffold — see reports/automation/framework_setup_report.md.
    """
    assert standard_user.username == "standard_user"
    assert standard_user.password  # value present; do not log
    assert standard_user.role == "standard"
