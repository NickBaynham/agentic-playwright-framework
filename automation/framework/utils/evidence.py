"""Failure-evidence helpers.

Save Playwright traces and screenshots into the standard
``reports/{traces,screenshots}/`` directories. Tests should not call these
directly during the happy path; they are invoked by a Pytest hook or by an
investigation workflow when a test fails.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import Page

from framework.utils.paths import REPORTS_DIR


def screenshot_path(test_name: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    target = REPORTS_DIR / "screenshots" / f"{test_name}-{stamp}.png"
    target.parent.mkdir(parents=True, exist_ok=True)
    return target


def save_screenshot(page: Page, test_name: str) -> Path:
    target = screenshot_path(test_name)
    page.screenshot(path=str(target), full_page=True)
    return target
