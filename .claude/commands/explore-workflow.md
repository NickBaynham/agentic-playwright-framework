---
description: Use Playwright MCP to explore a single bounded workflow on a live web application and produce a structured exploration session report. Does not generate BDD specs or automation code.
argument-hint: <target-url> <workflow-scope>
---

# /explore-workflow

Use the `mcp-exploratory-testing` skill.

Arguments: `$ARGUMENTS`

## Behavior

1. Use the `mcp-exploratory-testing` skill and its templates and checklists.
2. Verify Playwright MCP tools are available (`browser_navigate`, `browser_snapshot`, `browser_click`, `browser_type`, `browser_fill_form`, `browser_select_option`, `browser_press_key`, `browser_evaluate`, `browser_wait_for`, `browser_take_screenshot`, `browser_console_messages`, `browser_network_requests`). If they are not available, abort and tell the user.
3. Open the target URL supplied as the first argument with `browser_navigate`.
4. Explore only the workflow scope supplied as the second argument. Do not wander outside that scope.
5. Prefer `browser_snapshot` accessibility snapshots for reasoning. Use `browser_take_screenshot` only when a visual fact cannot be expressed in the snapshot.
6. Record pages visited, actions performed, observed outcomes, state changes (URL, cart badge, button text, validation messages, confirmation messages), data used, anomalies, and tooling notes.
7. Classify each anomaly using the anomaly report template. Keep application anomalies and tooling anomalies in distinct rows.
8. Identify candidate test cases and candidate page models, using the corresponding templates. Do not generate BDD specs, Gherkin files, page object code, or Playwright/PyTest code.
9. Produce the session report at `sessions/mcp-exploration/<app-name>/<workflow-name>_session.md`, using `kebab-case` for `<app-name>` and `<workflow-name>`.
10. If the session report grows beyond roughly 400 lines, split observations, anomalies, and test ideas into separate reports under `reports/exploration/<app-name>/`.
11. Apply the Final Review Checklist from the skill before returning.
12. Recommend using the `exploratory-to-bdd` skill (via the `/exploration-to-bdd` command) as the next step for the high-priority candidate test cases.

## Scope Guidance

If the scope is ambiguous, choose the smallest reasonable workflow, document the assumption under Assumptions in the session report, and proceed. Do not expand scope silently; list additional candidate workflows under Recommended Next Step instead.

## Output Summary

Finish by listing: the session report file path, pages observed, candidate test cases with priority, any anomalies (split by Application vs Tooling), any open questions, and the recommended next step.
