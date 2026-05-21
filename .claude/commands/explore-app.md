---
description: Use Playwright MCP to perform bounded app reconnaissance on a live web application and produce a structured app reconnaissance report with candidate workflows for follow-up exploration.
argument-hint: <target-url> <scope-or-goal>
---

# /explore-app

Use the `mcp-exploratory-testing` skill.

Arguments: `$ARGUMENTS`

## Behavior

1. Use the `mcp-exploratory-testing` skill and its templates and checklists.
2. Verify Playwright MCP tools are available. If they are not available, abort and tell the user.
3. Open the target URL supplied as the first argument with `browser_navigate`.
4. Explore the target application only within the scope or goal supplied as the second argument.
5. Identify major pages, navigation paths, forms, flows, visible user roles, and obvious risk areas. Do not deep-dive any single workflow in this command.
6. Prefer `browser_snapshot` for reasoning. Use `browser_take_screenshot` only when visual evidence is necessary.
7. Avoid destructive actions (delete, cancel, reset shared state, payment submission) unless the user explicitly authorizes them for this session.
8. Produce an app reconnaissance report at `sessions/mcp-exploration/<app-name>/app_reconnaissance_session.md`, using the exploration session template.
9. Under Recommended Next Step, list candidate workflows for follow-up `/explore-workflow` runs. Each candidate should be small enough to run on its own.
10. Do not generate BDD specs.
11. Do not generate Playwright or PyTest automation code.

## Scope Guidance

Reconnaissance is bounded by the scope or goal argument. Do not navigate outside the requested area. If a candidate workflow is observed but cannot be characterized without entering an out-of-scope area, list it as an Open Question rather than exploring it.

## Output Summary

Finish by listing: the reconnaissance report file path, the major pages and flows observed, the candidate workflows recommended for follow-up exploration, any anomalies, and any open questions.
