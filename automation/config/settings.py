"""Environment configuration loader.

Resolves the active environment from APP_ENV (default ``local``), reads
``environments.yaml``, and overlays values from a local ``.env`` file. Tests
and page objects receive a ``Settings`` instance through the ``settings``
fixture; they must not read YAML or environment variables directly.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

import yaml
from dotenv import load_dotenv

CONFIG_DIR = Path(__file__).resolve().parent
AUTOMATION_ROOT = CONFIG_DIR.parent
ENV_FILE = CONFIG_DIR / "environments.yaml"


@dataclass(frozen=True)
class Settings:
    environment: str
    base_url: str
    api_url: str
    browser: str
    headless: bool
    test_data_path: Path


def _as_bool(value: object) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "on"}


def load_settings(environment: str | None = None) -> Settings:
    load_dotenv(AUTOMATION_ROOT / ".env", override=False)

    active = environment or os.environ.get("APP_ENV", "local")

    with ENV_FILE.open("r", encoding="utf-8") as handle:
        all_envs = yaml.safe_load(handle) or {}

    if active not in all_envs:
        known = ", ".join(sorted(all_envs.keys())) or "(none)"
        raise ValueError(f"Unknown APP_ENV='{active}'. Known environments: {known}.")

    raw = all_envs[active]
    base_url = os.environ.get("BASE_URL", raw["base_url"])
    api_url = os.environ.get("API_URL", raw.get("api_url", ""))
    browser = os.environ.get("BROWSER", raw["browser"])
    headless = _as_bool(os.environ.get("HEADLESS", raw["headless"]))
    test_data_rel = raw["test_data_path"]

    return Settings(
        environment=active,
        base_url=base_url.rstrip("/"),
        api_url=api_url,
        browser=browser,
        headless=headless,
        test_data_path=(AUTOMATION_ROOT / test_data_rel).resolve(),
    )
