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

Absolutely — here’s a polished README.md you can use as the project root README.

# Agentic Playwright Testing Workflow
A discovery-first, agent-assisted testing project that uses **Claude Code**, **Playwright MCP**, **BDD specifications**, and **Python Playwright/PyTest automation** to explore applications, document behavior, and convert high-value scenarios into maintainable automated tests.
This project demonstrates a practical agentic testing workflow:
```text
Explore with MCP.
Specify with BDD.
Automate with Playwright.

⸻

Project Purpose

Traditional test automation often starts too late or too fast:

* A requirement is handed to QA.
* Someone writes test code.
* The test may or may not represent the actual application behavior.
* Exploratory insights are often lost in notes, screenshots, or memory.

This project takes a different approach.

Instead of asking an AI agent to immediately generate automation code, Claude Code first uses browser automation through Playwright MCP to explore the live application like a human tester. The agent captures what it observes, identifies workflows and anomalies, derives BDD-style test specifications, and only then converts selected high-value scenarios into Python Playwright/PyTest automation.

The goal is not to replace testers. The goal is to give testers and automation engineers a structured agentic workflow for turning exploration into durable regression coverage.

⸻

Core Thesis

Claude Code should not simply generate tests from vague prompts.

A better workflow is:

1. Explore the live application.
2. Record observed behavior.
3. Identify pages, actions, data needs, outcomes, and anomalies.
4. Convert observations into reviewable BDD specifications.
5. Select the best automation candidates.
6. Generate maintainable Playwright/PyTest automation.
7. Execute, review, and investigate failures with evidence.

This project demonstrates that process.

⸻

High-Level Workflow

Target URL + Workflow Scope
        ↓
Playwright MCP Exploration
        ↓
Exploration Session Report
        ↓
BDD Markdown + Gherkin Specs
        ↓
Traceability Matrix + Quality Review
        ↓
Automation Candidate Selection
        ↓
Python Playwright/PyTest Implementation
        ↓
Test Execution + Reports
        ↓
Failure Investigation + Defect Notes

⸻

Skills Included

This project uses three Claude Code skills.

1. mcp-exploratory-testing

Uses Playwright MCP to explore a live web application and produce structured exploratory testing artifacts.

This skill answers:

* What pages did we observe?
* What actions were available?
* What data was needed?
* What happened after each action?
* What state changes occurred?
* What anomalies or risks appeared?
* What candidate tests should we consider?
* What page models might later support automation?

Primary outputs:

sessions/mcp-exploration/
reports/exploration/

Example command:

/explore-workflow https://www.saucedemo.com/ "standard user checkout flow"

⸻

2. exploratory-to-bdd

Converts exploration notes, user stories, acceptance criteria, and observed behavior into structured BDD artifacts.

This skill answers:

* What features and scenarios should be specified?
* What behavior was observed?
* What expected behavior is supported by requirements?
* What assumptions are being made?
* What open questions remain?
* Which scenarios are good automation candidates?

Primary outputs:

specs/bdd/markdown/
specs/bdd/features/
specs/bdd/traceability/
specs/bdd/reviews/
specs/bdd/automation/

Example command:

/generate-bdd sessions/mcp-exploration/saucedemo/standard_user_checkout_session.md

⸻

3. agentic-playwright-automation

Converts approved BDD specs or automation candidate reports into maintainable Python Playwright/PyTest automation.

This skill answers:

* What tests should be created?
* What page objects are needed?
* What fixtures are needed?
* What test data should be externalized?
* What environment configuration is required?
* Did the generated test follow framework standards?
* How should failures be investigated?

Primary outputs:

automation/tests/
automation/framework/
automation/test_data/
automation/config/
automation/reports/

Example command:

/convert-bdd-to-playwright specs/bdd/features/checkout.feature

⸻

Recommended Project Structure

.
├── .claude/
│   ├── skills/
│   │   ├── mcp-exploratory-testing/
│   │   ├── exploratory-to-bdd/
│   │   └── agentic-playwright-automation/
│   │
│   └── commands/
│       ├── explore-workflow.md
│       ├── explore-app.md
│       ├── review-exploration.md
│       ├── exploration-to-bdd.md
│       ├── generate-bdd.md
│       ├── review-bdd.md
│       ├── execute-bdd-mcp.md
│       ├── setup-playwright-framework.md
│       ├── generate-playwright-test.md
│       ├── generate-playwright-suite.md
│       ├── review-playwright-test.md
│       ├── investigate-playwright-failure.md
│       └── convert-bdd-to-playwright.md
│
├── sessions/
│   └── mcp-exploration/
│
├── reports/
│   ├── exploration/
│   └── bdd-mcp-execution/
│
├── specs/
│   └── bdd/
│       ├── markdown/
│       ├── features/
│       ├── traceability/
│       ├── reviews/
│       └── automation/
│
└── automation/
    ├── README.md
    ├── pyproject.toml
    ├── pytest.ini
    ├── Makefile
    ├── config/
    ├── framework/
    ├── tests/
    ├── test_data/
    ├── reports/
    └── docs/

⸻

Prerequisites

Install Claude Code:

npm install -g @anthropic-ai/claude-code

Install Playwright MCP:

claude mcp add playwright -- npx -y @playwright/mcp@latest

Install Playwright browser binaries:

npx playwright install

Verify the MCP server is available:

claude mcp list

You should see a registered playwright MCP server.

For project-scoped MCP configuration, add a .mcp.json file:

{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  }
}

⸻

End-to-End Usage

The recommended workflow has five major stages.

⸻

Stage 1: Explore the Application

Start with a target URL and a bounded workflow.

Example:

/explore-workflow https://www.saucedemo.com/ "standard user checkout flow"

Claude Code should use the mcp-exploratory-testing skill and Playwright MCP to:

* open the target URL
* inspect the app through accessibility snapshots
* interact with the application
* document pages visited
* record actions performed
* record observed outcomes
* identify data used
* identify anomalies
* propose candidate test cases
* propose candidate page models

Expected output:

sessions/mcp-exploration/saucedemo/standard_user_checkout_session.md

The exploration report should include:

* session metadata
* exploration scope
* out-of-scope areas
* assumptions
* test data used
* pages observed
* action timeline
* observed outcomes
* anomalies and risks
* candidate test cases
* candidate page models
* open questions
* recommended next step

⸻

Stage 2: Convert Exploration to BDD

Once the exploration report exists, convert it into BDD specs.

Example:

/generate-bdd sessions/mcp-exploration/saucedemo/standard_user_checkout_session.md

Claude Code should use the exploratory-to-bdd skill to generate:

specs/bdd/markdown/checkout.md
specs/bdd/features/checkout.feature
specs/bdd/traceability/checkout_traceability_matrix.md
specs/bdd/reviews/checkout_bdd_quality_review.md
specs/bdd/automation/checkout_automation_candidates.md

The BDD output should separate:

* observed behavior
* expected behavior
* assumptions
* open questions
* potential defects
* automation candidates

This distinction is important. Observed behavior is not automatically the same as intended behavior.

⸻

Stage 3: Review BDD Specs

Review generated BDD specs before automation.

Example:

/review-bdd specs/bdd/features/checkout.feature

The review should check:

* Are scenarios focused?
* Are expected outcomes clear?
* Are assumptions documented?
* Are open questions documented?
* Are potential defects separated from expected behavior?
* Is traceability preserved?
* Is automation priority justified?
* Are any scenarios too broad or vague?

Expected output:

specs/bdd/reviews/checkout_bdd_quality_review.md

Only scenarios marked as clear, high-value, and automatable should move forward.

⸻

Stage 4: Convert BDD Specs to Playwright Automation

Use approved BDD specs to generate Python Playwright/PyTest tests.

Example:

/convert-bdd-to-playwright specs/bdd/features/checkout.feature

Claude Code should use the agentic-playwright-automation skill to create or update:

automation/tests/ui/
automation/framework/pages/
automation/framework/components/
automation/framework/models/
automation/test_data/
automation/config/
automation/reports/automation/

Generated automation must follow these rules:

* Use Python, PyTest, and Playwright.
* Keep meaningful assertions at the test level.
* Use fixtures for pages, config, and test data.
* Use page objects for actions and locators.
* Do not hide important business assertions inside page objects.
* Do not hard-code URLs, credentials, products, or environment-specific values in tests.
* Use environment configuration.
* Prefer accessible Playwright locators.
* Do not use time.sleep.
* Do not add arbitrary waits.
* Preserve traceability to the source BDD spec.

Expected output:

automation/reports/automation/checkout_implementation_report.md

⸻

Stage 5: Run Tests and Investigate Failures

Run the automation suite.

From the automation/ directory:

make install
make test-smoke
make test-ui
make test-report

If a test fails, use:

/investigate-playwright-failure automation/tests/ui/test_checkout.py::test_standard_user_can_complete_checkout

Claude Code should:

* reproduce the failure if possible
* inspect PyTest output
* inspect screenshots, traces, and logs
* check config
* check test data
* compare against the source BDD spec
* classify the failure
* recommend the correct action
* avoid weakening assertions just to make the test pass

Failure categories include:

* Product Defect
* Test Data Issue
* Locator Issue
* Environment Issue
* Timing/Flakiness
* Framework Issue
* Tooling Issue
* Ambiguous Requirement

Expected output:

automation/reports/automation/failures/<failure_name>_investigation.md

⸻

Example Workflow: SauceDemo Checkout

1. Explore the checkout flow

/explore-workflow https://www.saucedemo.com/ "standard user checkout flow"

Output:

sessions/mcp-exploration/saucedemo/standard_user_checkout_session.md

⸻

2. Generate BDD specs

/generate-bdd sessions/mcp-exploration/saucedemo/standard_user_checkout_session.md

Output:

specs/bdd/markdown/checkout.md
specs/bdd/features/checkout.feature
specs/bdd/traceability/checkout_traceability_matrix.md
specs/bdd/reviews/checkout_bdd_quality_review.md
specs/bdd/automation/checkout_automation_candidates.md

⸻

3. Convert high-priority scenarios to automation

/convert-bdd-to-playwright specs/bdd/features/checkout.feature

Output:

automation/tests/ui/test_checkout.py
automation/framework/pages/login_page.py
automation/framework/pages/inventory_page.py
automation/framework/pages/cart_page.py
automation/framework/pages/checkout_info_page.py
automation/framework/pages/checkout_overview_page.py
automation/framework/pages/checkout_complete_page.py
automation/test_data/local/users.yaml
automation/test_data/local/products.yaml
automation/test_data/local/checkout.yaml
automation/reports/automation/checkout_implementation_report.md

⸻

4. Run tests

cd automation
make test-ui

⸻

Automation Framework Standards

The automation framework is designed to be friendly to both humans and agents.

Tests

Tests should read like behavior specs.

Good:

def test_standard_user_can_login(login_page, inventory_page, standard_user):
    login_page.open()
    login_page.login_as(standard_user)
    expect(inventory_page.products_heading).to_be_visible()
    expect(inventory_page.shopping_cart_link).to_be_visible()

Avoid:

def test_standard_user_can_login(login_page):
    login_page.login_and_verify_success()

The second example hides the meaningful assertions inside the page object.

⸻

Page Objects

Page objects should:

* represent one page or screen
* expose locators as properties
* provide user actions as methods
* avoid major business assertions
* avoid hard-coded test data
* use stable Playwright locators

Example:

class LoginPage:
    def __init__(self, page, base_url: str):
        self.page = page
        self.base_url = base_url
    @property
    def username_input(self):
        return self.page.get_by_placeholder("Username")
    @property
    def password_input(self):
        return self.page.get_by_placeholder("Password")
    @property
    def login_button(self):
        return self.page.get_by_role("button", name="Login")
    def open(self):
        self.page.goto(self.base_url)
    def login_as(self, user):
        self.username_input.fill(user.username)
        self.password_input.fill(user.password)
        self.login_button.click()

⸻

Fixtures

Fixtures should provide:

* config
* page objects
* test data
* generated entities
* reusable setup
* cleanup when needed

Fixtures should be readable and composable. Avoid overly magical fixture chains.

⸻

Test Data

Test data should live outside the tests.

Example:

automation/test_data/local/users.yaml
automation/test_data/qa/users.yaml

Example data:

users:
  standard_user:
    username: standard_user
    password: secret_sauce

Do not commit private credentials or production secrets.

⸻

Environment Configuration

Environment-specific values should live in:

automation/config/environments.yaml

Example:

local:
  base_url: "https://www.saucedemo.com/"
  api_url: ""
  test_data_path: "automation/test_data/local"
  browser: "chromium"
  headless: true
qa:
  base_url: "https://qa.example.com"
  api_url: "https://api-qa.example.com"
  test_data_path: "automation/test_data/qa"
  browser: "chromium"
  headless: true

Tests should not hard-code base URLs.

⸻

Locator Strategy

Preferred locator order:

1. role/name
2. label
3. placeholder
4. text
5. test id
6. stable CSS
7. XPath only as a last resort

Use locators that reflect user-visible behavior where possible.

⸻

Locator Candidate Handoff

During MCP exploration, Claude Code captures locator candidates for meaningful elements (fields, buttons, links, headings, menus, product cards, cart badges, validation and confirmation messages, repeated/dynamic controls). These candidates are stored in the exploration session reports under `sessions/mcp-exploration/` as evidence for later automation.

Locator candidates are not final implementation decisions.

The BDD layer may preserve locator hints in Markdown Automation Notes (and reference them in the traceability matrix), but Gherkin scenarios remain behavior-focused and selector-free.

During Playwright automation generation, Claude reviews locator candidates, selects final locators using the framework locator strategy and practical stability rules, and documents the outcome in a Locator Decision Log inside the implementation report. Decisions are recorded as Accepted, Accepted with Scope, Modified, Rejected, or Needs Review, with rationale and source.

The handoff flow:

```
MCP Exploration -> locator candidates (evidence)
       |
       v
Markdown BDD spec -> Automation Notes (optional hints)
                  -> Traceability Matrix (Locator Candidate Reference)
       |
       v
Playwright/PyTest implementation -> Locator Decision Log (final decisions)
```

⸻

Reporting

The project produces several types of reports.

Exploration reports

sessions/mcp-exploration/
reports/exploration/

Used to document what the agent observed during browser exploration.

⸻

BDD reports

specs/bdd/reviews/
specs/bdd/traceability/
specs/bdd/automation/

Used to review behavior specs and select automation candidates.

⸻

Automation reports

automation/reports/automation/
automation/reports/html/
automation/reports/junit/
automation/reports/traces/
automation/reports/screenshots/

Used to understand implementation, test execution, and failure evidence.

⸻

Key Commands

Exploration

/explore-workflow <target-url> <workflow-scope>

Explore a bounded workflow with Playwright MCP.

/explore-app <target-url> <scope-or-goal>

Perform broader app reconnaissance.

/review-exploration <exploration-file-or-folder>

Review exploration notes for completeness.

⸻

BDD

/generate-bdd <source-file-or-description>

Convert exploration notes or requirements into BDD specs.

/review-bdd <bdd-file-or-folder>

Review BDD specs for quality and ambiguity.

/execute-bdd-mcp <bdd-file-or-folder> <target-url>

Execute BDD scenarios manually through Playwright MCP without writing automation code.

⸻

Automation

/setup-playwright-framework <optional app name or target URL>

Create or review the base Python Playwright/PyTest framework.

/generate-playwright-test <source-file-or-scenario>

Generate one Playwright/PyTest test.

/generate-playwright-suite <bdd-folder-or-automation-candidate-file>

Generate a small automation suite from approved scenarios.

/review-playwright-test <test-file-or-folder>

Review Playwright/PyTest automation for quality.

/investigate-playwright-failure <test-path-or-report>

Investigate a failing Playwright/PyTest test.

/convert-bdd-to-playwright <bdd-file-or-folder>

Convert reviewed BDD specs into Playwright/PyTest automation.

⸻

Example Automation Commands

From the automation/ directory:

make install

Install dependencies and Playwright browsers.

make lint

Run linting.

make test

Run all tests.

make test-ui

Run UI tests.

make test-api

Run API tests.

make test-smoke

Run smoke tests.

make test-report

Run tests with HTML and JUnit reporting.

make test-debug

Run tests in Playwright debug mode.

⸻

Human Review Points

This workflow is agent-assisted, not agent-autonomous.

Human review is expected at these points:

1. After exploration reports are generated.
2. After BDD specs are generated.
3. Before scenarios are selected for automation.
4. After Playwright tests are generated.
5. After any failure investigation.
6. Before any defect is filed.
7. Before code is merged.

The agent can accelerate the work, but the human tester or automation engineer remains responsible for judgment.

⸻

Important Guardrails

Claude Code should not:

* explore outside the requested scope
* store secrets in reports
* invent requirements
* treat observed behavior as intended behavior without confirmation
* generate automation from unclear specs
* automate scenarios marked Do Not Automate
* hide important assertions inside page objects
* hard-code environment-specific data in tests
* add arbitrary waits or time.sleep
* weaken assertions to make tests pass
* perform destructive actions unless explicitly allowed
* automatically file defects without review
* automatically commit or open pull requests unless explicitly requested

⸻

What This Project Demonstrates

This project demonstrates:

* agent-assisted exploratory testing
* Playwright MCP browser exploration
* structured test discovery
* BDD generation from observed behavior
* traceability from exploration to specification
* automation candidate selection
* Python Playwright/PyTest framework design
* page object modeling
* fixture-driven test data
* environment-aware test configuration
* failure investigation
* evidence-based QA reporting
* responsible human-in-the-loop agentic engineering

⸻

Why This Matters

Exploratory testing is valuable because it finds gaps that scripted tests miss.

Automation is valuable because it makes important checks repeatable.

BDD is valuable because it creates a shared language between product, QA, and engineering.

This project connects all three:

Exploration discovers behavior.
BDD clarifies behavior.
Automation preserves behavior.

Claude Code and Playwright MCP act as accelerators, but the workflow remains grounded in structured QA thinking.

⸻

Current Status

This project is intended to evolve in phases.

Phase 1

* Create MCP exploratory testing skill.
* Generate structured exploration reports.
* Validate workflow on SauceDemo.

Phase 2

* Create exploratory-to-BDD skill.
* Generate Markdown and Gherkin specs.
* Add traceability and review artifacts.

Phase 3

* Create agentic Playwright automation skill.
* Scaffold Python Playwright/PyTest framework.
* Convert approved BDD specs into tests.

Phase 4

* Add CI execution.
* Add richer reporting.
* Add failure investigation examples.
* Publish portfolio case study.

⸻

Recommended First Experiment

Use SauceDemo as the first target:

/explore-workflow https://www.saucedemo.com/ "standard user checkout flow"

Then run:

/generate-bdd sessions/mcp-exploration/saucedemo/standard_user_checkout_session.md

Then run:

/convert-bdd-to-playwright specs/bdd/features/checkout.feature

This gives a complete demonstration of the workflow:

Live app exploration
    ↓
Structured session notes
    ↓
BDD specs
    ↓
Automation implementation

⸻

Project Philosophy

This project is not about AI replacing QA.

It is about making QA work more observable, reusable, and scalable.

The best use of AI in testing is not blind automation generation. It is:

* faster exploration
* better documentation
* clearer test design
* stronger traceability
* repeatable automation
* better failure analysis
* more informed human review

That is the purpose of this project.
