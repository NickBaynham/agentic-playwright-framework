---
description: Execute BDD scenarios manually through Playwright MCP and record an execution report. Does not generate automation code.
argument-hint: <bdd-file-or-folder> <target-url>
---

# /execute-bdd-mcp

Use the `exploratory-to-bdd` skill.

Arguments: `$ARGUMENTS`

## Behavior

1. Read the BDD spec or feature file(s) at the supplied path (first argument).
2. Use Playwright MCP (`browser_navigate`, `browser_snapshot`, `browser_click`, `browser_fill_form`, `browser_evaluate`) to execute each scenario against the supplied target URL (second argument).
3. For each scenario:
   - Record pass or fail.
   - Capture the observed behavior, including any deviations from the expected outcome.
   - Note any flakiness, retries, or unexpected modal/timing issues.
4. Generate an execution report at `reports/bdd-mcp-execution/<feature_name>_<YYYYMMDD-HHMMSS>.md`. The report must include:
   - Target URL and environment notes.
   - Summary table of Scenario ID, status, and notes.
   - Per-scenario detail with Observed Evidence.
   - Any newly discovered Open Questions or Potential Defects.
5. Do not generate Playwright or PyTest automation code.
6. Do not modify the BDD spec unless explicitly asked. If issues are found, recommend they be addressed via `/review-bdd`.

## Output Summary

Finish by listing the execution report path, totals (pass/fail), and any scenarios that surfaced new defects or open questions.
