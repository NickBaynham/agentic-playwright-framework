---
name: mcp-exploratory-testing
description: Use when the user wants to drive Playwright MCP to perform bounded exploratory testing of a live web application — given a target URL plus a workflow scope, user story, business flow, feature area, regression risk area, or a prompt such as "use Playwright MCP to explore the standard user checkout flow". Produces structured exploration session reports, page observations, action timelines, anomaly reports, candidate test ideas, and candidate page models. Does not generate BDD specs or Playwright/PyTest automation code in v0.1.
---

# MCP Exploratory Testing

## Version

0.1

## Purpose

Guide Claude Code through bounded, human-directed exploratory testing of a live web application using Playwright MCP, and capture the session as structured, reviewable Markdown evidence that can later be converted into BDD specs by the `exploratory-to-bdd` skill or into automation by a future skill.

This skill standardizes the first stage of the agentic testing workflow:

```
Target URL + workflow scope
    -> mcp-exploratory-testing skill
    -> Playwright MCP browser exploration
    -> Structured exploration session report
    -> exploratory-to-bdd skill
    -> Markdown BDD specs + Gherkin .feature files
    -> Future conversion to Playwright/PyTest automation
```

## When to Use This Skill

Use this skill when the input is any of the following and the desired output is a structured exploratory testing artifact:

- A target URL plus a workflow scope.
- A user story or business flow to explore in a live app.
- A feature area to reconnoiter before writing specs.
- An exploratory testing goal ("learn what the checkout actually does").
- A regression risk area that needs evidence before automation.
- A prompt such as "use Playwright MCP to explore the standard user checkout flow".

Do not use this skill to generate BDD specs, Gherkin `.feature` files, Playwright code, or PyTest code. Hand off to the `exploratory-to-bdd` skill for BDD generation. Automation code generation is out of scope for v0.1.

## Inputs

- Target URL of the application under exploration.
- Workflow scope, user story, business flow, feature area, or regression risk area.
- Optional: user role, test data, credentials (public demo only), browser preference, stop condition.
- Optional: prior exploration notes or session reports for re-exploration.

## Outputs

- Exploration session report under `sessions/mcp-exploration/<app-name>/<workflow-name>_session.md`.
- Optional split reports under `reports/exploration/<app-name>/`:
  - `<workflow-name>_observations.md`
  - `<workflow-name>_anomalies.md`
  - `<workflow-name>_test_ideas.md`
  - `<workflow-name>_review.md`
- Optional app reconnaissance report under `sessions/mcp-exploration/<app-name>/app_reconnaissance_session.md`.

## Core Principles

1. Explore only the requested workflow or bounded scope.
2. Prefer Playwright MCP accessibility snapshots (`browser_snapshot`) for reasoning.
3. Use screenshots (`browser_take_screenshot`) only when visual evidence is needed.
4. Record observations in structured Markdown using the provided templates.
5. Separate observed application behavior from expected or intended behavior.
6. Separate application anomalies from tooling anomalies.
7. Do not invent requirements.
8. Do not silently decide product correctness without a stated requirement.
9. Document assumptions, uncertainty, and open questions.
10. Capture data used during exploration.
11. Capture pages visited and their observed purpose.
12. Capture actions performed and their observed outcomes.
13. Capture state changes such as URL changes, button text changes, cart badge changes, validation messages, and confirmation messages.
14. Identify candidate assertions from observed outcomes.
15. Identify candidate test cases, but do not generate formal BDD specs.
16. Identify candidate page models, but do not generate page object code.
17. Do not generate Playwright or PyTest automation code in this skill version.
18. Do not generate Cucumber or Behave feature files in this skill version.
19. Do not modify application data destructively unless the user explicitly allows it.
20. Do not store secrets, tokens, or private credentials in reports.
21. Treat public demo credentials as acceptable only when they are visibly provided by the demo app or the user.
22. Clearly mark any tool workaround, such as using DOM `.click()` through `browser_evaluate` when an MCP click does not trigger expected behavior.

## Required Output Structure

```
sessions/
  mcp-exploration/
    <app-name>/
      <workflow-name>_session.md
reports/
  exploration/
    <app-name>/
      <workflow-name>_observations.md
      <workflow-name>_anomalies.md
      <workflow-name>_test_ideas.md
      <workflow-name>_review.md
```

Create directories as needed. Use `kebab-case` for `<app-name>` and `<workflow-name>`. For a small exploration, a single session report is sufficient. Recommend splitting observations, anomalies, and test ideas into separate reports when the session report grows beyond roughly 400 lines or covers multiple distinct workflows.

## Exploration Scope Rules

- Restate the scope in the session report before exploring.
- If scope is ambiguous, choose the smallest reasonable workflow, document the assumption, and proceed.
- Record what is out of scope so a reviewer can see what was intentionally skipped.
- Stop exploration when the stop condition is met (workflow complete, anomaly threshold reached, requested step count reached, or user-defined limit).
- Do not silently expand scope. If a follow-up workflow is discovered, list it under Recommended Next Step rather than exploring it in the same session.

## Playwright MCP Usage Rules

- Open the target URL using `browser_navigate`.
- Use `browser_snapshot` as the primary observation tool; the accessibility tree is the source of truth for what is on the page.
- Use `browser_take_screenshot` only when visual evidence adds information the snapshot does not (layout, color, image content).
- Use `browser_click`, `browser_type`, `browser_fill_form`, `browser_select_option`, `browser_press_key`, and `browser_hover` for user actions.
- Use `browser_console_messages` and `browser_network_requests` to capture browser-side signals only when relevant to an observation or anomaly.
- Use `browser_evaluate` sparingly. When it is used to drive UI (for example a DOM `.click()` to work around a click that returned success but did not trigger the application handler), mark the step as a Tool Workaround in the action timeline and record an entry in Tooling Notes.
- Use `browser_wait_for` rather than arbitrary sleeps when waiting for application state.
- Do not leave the browser tab navigated to a destructive or unstable state at the end of the session.

## Observation Rules

- Every action recorded must have an observed result.
- Observed results must come from the snapshot, screenshot, console, or network response, not from assumption.
- When the observed result is "nothing visible changed", record that explicitly and note what was expected.
- When behavior is correct only by assumption (no explicit requirement was given), tag it as an Assumption in the session report rather than as confirmed correct behavior.

## Action Timeline Rules

- Maintain a numbered, chronological Action Timeline for the workflow.
- Each entry records: step number, page, action, test data, observed result, evidence reference, notes.
- Reference evidence by snapshot or screenshot filename, console message excerpt, or network request URL.
- Mark any Tool Workaround in the Notes column.

## Page Observation Rules

- Create a Page Observation entry for each distinct page or significant view.
- Record URL or path, observed purpose, entry conditions, visible elements, available actions, state changes, candidate assertions, candidate test ideas, and open questions.
- Use the user-visible text for elements. Locator hints (id, role, label, data-test) are optional and only when easily observable from the accessibility tree.
- Do not propose CSS or XPath selectors; locator strategy is an automation concern.

## Data Capture Rules

- Record every data value used: usernames, search terms, form inputs, addresses, postal codes, quantities, dropdown selections.
- Record the source of each value: demo app, user-provided, generated, environmental default.
- Record whether the data was required by the application or supplied by the tester.
- Do not record private credentials, tokens, API keys, or PII. Public demo credentials such as `standard_user / secret_sauce` on saucedemo.com are acceptable.

## Anomaly and Risk Rules

- Use the anomaly report template for every anomaly.
- Classify anomaly type: Application Behavior, Tooling Behavior, Environment, Data, Usability, Accessibility, Performance Observation, Unknown.
- Assign severity: Low, Medium, High, Critical, Needs Clarification.
- Assign status: Open, Needs Review, Clarified, Potential Defect, Tooling Limitation, Closed.
- Keep application anomalies and tooling anomalies in distinct rows; do not merge them.
- Provide a recommendation for every anomaly even if the recommendation is "needs requirement to evaluate".
- Mark anything that may be a defect as a Potential Defect rather than asserting it is a defect.

## Candidate Test Idea Rules

- Use the test idea template.
- Each idea has: Candidate ID, Title, Behavior Area, Priority (High, Medium, Low, Needs Clarification), Suggested Type, Rationale, Notes.
- Suggested Type values: BDD Spec, Exploratory Follow-Up, Playwright UI Automation Candidate, API Automation Candidate, Manual Review, Defect Investigation, Do Not Automate.
- Each idea must have an observable expected result.
- Do not generate Gherkin or step definitions; this skill only proposes the test idea.

## Candidate Page Model Rules

- Use the page model candidate template.
- Treat candidate page models as design observations only.
- Do not generate page object code, locator strategies, or fixtures.
- A real page object should be implemented later, against a real requirement, by an automation-focused skill or engineer.

## Safety and Credential Rules

- Never perform destructive actions (Delete Account, Cancel Order, Reset App State on shared environments, payment submission against a real processor) unless the user explicitly authorizes the action in writing for that session.
- Never store private credentials, tokens, session cookies, or PII in any report.
- Public demo credentials are acceptable only when the application itself publishes them on its landing page or the user provides them as test credentials.
- If the session navigates to a domain outside the originally requested target, stop and confirm with the user before continuing.

## Tooling Limitation Rules

- Treat Playwright MCP as a tool under observation, not an oracle.
- When a tool call returns success but the application does not respond, record this as a Tooling Behavior anomaly and try one alternative: refreshed snapshot, retry, or `browser_evaluate` fallback.
- Always document fallbacks in Tooling Notes so reviewers and downstream automation engineers know which steps relied on a workaround.
- Do not silently retry until "it works". Retries are observations and belong in the timeline.

## Workflow: Bounded Workflow Exploration

1. Read the user's scope and target URL.
2. Create the session report file under `sessions/mcp-exploration/<app-name>/<workflow-name>_session.md` from `templates/exploration_session_template.md`.
3. Populate Session Metadata, Exploration Scope, Out of Scope, Assumptions, and Test Data Used.
4. Navigate to the target URL with `browser_navigate` and take an initial `browser_snapshot`.
5. Execute the workflow step by step. After each action, take a snapshot and record an Action Timeline entry.
6. Create a Page Observation entry the first time you reach a distinct page or significant view.
7. Record anomalies as they appear, classified per the anomaly rules.
8. After the workflow completes (or the stop condition fires), populate Observed Outcomes, Candidate Test Cases, Candidate Page Models, Candidate Data Needs, Open Questions, Tooling Notes, and Recommended Next Step.
9. Apply the Final Review Checklist before returning.

## Workflow: App Reconnaissance

1. Read the user's scope or goal.
2. Create `sessions/mcp-exploration/<app-name>/app_reconnaissance_session.md` from the exploration session template.
3. Identify major pages, navigation paths, forms, flows, visible user roles, and obvious risk areas — only within the stated scope.
4. Avoid destructive actions.
5. Produce a list of candidate workflows under Recommended Next Step. Each candidate should be small enough to run through Bounded Workflow Exploration on its own.
6. Do not generate BDD specs or automation code.

## Workflow: Exploration Review

1. Read the provided exploration artifact (single session report or a folder of reports).
2. Apply `templates/exploration_review_template.md` and the checklists.
3. Identify gaps, ambiguity, missing data, missing outcomes, missing anomalies, and weak evidence.
4. Write or update the review file at `reports/exploration/<app-name>/<workflow-name>_review.md`.
5. End with a Recommended Next Step (re-explore, hand off to `exploratory-to-bdd`, file as potential defect, etc.).

## Workflow: Exploration to BDD Handoff

1. Read the exploration session file.
2. Confirm it has scope, pages, actions, outcomes, test data, and at least one candidate test case with an observable expected result.
3. If sufficient, hand off to the `exploratory-to-bdd` skill, which is responsible for generating Markdown BDD specs, Gherkin `.feature` files, traceability matrices, automation candidate reviews, and BDD quality reviews.
4. If not sufficient, write an exploration review describing the missing information and recommend a focused re-exploration.
5. Do not generate BDD specs or automation code from inside this skill.

## What This Skill Does Not Do in v0.1

Included in v0.1:

- Bounded workflow exploration.
- App reconnaissance.
- Page observations.
- Action timeline.
- Observed outcomes.
- Test data capture.
- Anomaly and risk capture.
- Candidate test ideas.
- Candidate page models.
- Open questions.
- Exploration quality review.
- Handoff guidance to the `exploratory-to-bdd` skill.

Not included in v0.1:

- BDD spec generation.
- Gherkin `.feature` generation.
- Playwright or PyTest code generation.
- Page object implementation.
- Test fixture implementation.
- Formal defect filing.
- Jira or GitHub issue creation.
- Performance testing.
- Accessibility audit.
- Security testing.
- Visual regression testing.

## Final Review Checklist

Before returning the session report:

- Session Metadata is fully populated.
- Exploration Scope and Out of Scope are stated.
- Assumptions are listed (or "None").
- Test Data Used table is populated (or "None").
- At least one Page Observation entry exists per distinct page visited.
- Action Timeline is complete, numbered, and references evidence.
- Observed Outcomes are listed.
- Anomalies are classified by type, severity, and status, with application and tooling anomalies kept distinct.
- Candidate Test Cases each have an observable expected result and a priority.
- Candidate Page Models are marked as design observations only.
- Open Questions are listed (or "None").
- Tooling Notes record any workaround.
- Recommended Next Step is present and concrete.
- No BDD specs, Gherkin files, or automation code were generated by this skill.
- No private credentials, tokens, or PII appear in the report.
