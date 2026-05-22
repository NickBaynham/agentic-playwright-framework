# Agent Safety Checklist

Apply to every automation change. Mark each item Pass, Fail, or Needs Review.

| Check | Status | Notes |
|---|---|---|
| No broad unrelated refactors were performed | | |
| No new framework pattern was invented when an existing one fits | | |
| No unrelated files were deleted | | |
| No credentials, tokens, or PII were exposed in code, fixtures, reports, or commit messages | | |
| No destructive data actions were performed against shared environments without explicit authorization | | |
| No failures were masked by weakening assertions, swallowing exceptions, or adding waits | | |
| No unnecessary dependencies were added; versions are pinned in `pyproject.toml` | | |
| No automatic git commit, push, or pull request was performed unless explicitly requested | | |
