# Agentic Playwright Framework

A workspace for exploratory and automated browser testing driven by an LLM agent (Claude Code) and the Playwright MCP server. The agent navigates the application under test, captures observed behavior as acceptance criteria, and executes those criteria against the live site.

## Project Layout

```
.
├── cases/        Markdown test cases written in user-story / acceptance-criteria form
├── blogs/        Long-form write-ups of testing sessions and methodology
├── .claude/      Claude Code project configuration
└── .playwright-mcp/  Runtime artifacts from the Playwright MCP (snapshots, console logs)
```

## Prerequisites

- Node.js 18 or newer
- Claude Code CLI (`npm install -g @anthropic-ai/claude-code`)
- A Playwright-compatible browser (installed via `npx playwright install`)

## Setting up the Playwright MCP

The agent drives the browser through the official Playwright MCP server. Register it with Claude Code:

```bash
claude mcp add playwright -- npx -y @playwright/mcp@latest
npx playwright install
```

For a project-scoped configuration, add an `.mcp.json` at the repo root:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  }
}
```

Verify with `claude mcp list` — `playwright` should appear in the output.

## Working in This Repo

1. Start Claude Code from the project root: `claude`.
2. Ask the agent to drive a site (for example, `Open https://www.saucedemo.com/`).
3. Walk the application step by step in natural language. The agent uses `browser_navigate`, `browser_snapshot`, `browser_click`, `browser_fill_form`, and `browser_evaluate` under the hood.
4. Once a flow is understood, ask the agent to write the test cases to `cases/<feature>.md`.
5. Ask the agent to execute the cases and report status.

See `blogs/exploratory.md` for a full worked example using the Sauce Labs demo store.

## Conventions

- Test cases live in `cases/` as Markdown, one file per feature or target site.
- Each test case follows the structure: target URL, user story, numbered acceptance criteria.
- Selectors prefer `data-test` attributes when the application exposes them — they are the most stable choice for automation.
- Long-form narratives, lessons learned, and methodology notes live in `blogs/`.

## Troubleshooting

- If a `browser_click` call appears to succeed but the page state does not advance, fall back to `browser_evaluate` with a direct `element.click()`. This was observed against React handlers on Sauce Labs and is documented in `blogs/exploratory.md`.
- If the agent cannot find an element by reference, re-run `browser_snapshot` — references are scoped to the most recent snapshot and stale references will error.
- Snapshots and console logs accumulate under `.playwright-mcp/`. Clean periodically or add to `.gitignore` if not already excluded.
