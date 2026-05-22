"""Path helpers anchored at the automation root."""

from __future__ import annotations

from pathlib import Path

AUTOMATION_ROOT: Path = Path(__file__).resolve().parents[2]
CONFIG_DIR: Path = AUTOMATION_ROOT / "config"
TEST_DATA_DIR: Path = AUTOMATION_ROOT / "test_data"
REPORTS_DIR: Path = AUTOMATION_ROOT / "reports"
