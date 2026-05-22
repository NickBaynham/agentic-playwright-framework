# Role
You are a senior QA automation architect, Playwright MCP specialist, BDD test designer, and Python Playwright/PyTest framework expert.
# Goal
Update the existing Claude Code skills and commands to support locator candidate capture during MCP exploratory testing and locator handoff during BDD-to-automation conversion.
The purpose is to improve the workflow:
```text
MCP Exploration
  ↓
Pages, actions, outcomes, anomalies, data needs, locator candidates
  ↓
BDD specs with optional automation notes
  ↓
Automation candidate review
  ↓
Page object locator decisions
  ↓
Playwright/PyTest implementation

Important distinction:

The exploration skill should collect locator candidates, not final page object locators.

Locator candidates are evidence gathered during exploration. Final locator decisions happen during the automation phase when page objects are created.

⸻

Existing Skills to Update

Update these existing skills if they are present:

.claude/skills/mcp-exploratory-testing/
.claude/skills/exploratory-to-bdd/
.claude/skills/agentic-playwright-automation/

Update related commands under:

.claude/commands/

Do not delete existing content. Modify and extend the skills, templates, examples, checklists, and commands in place.

⸻

High-Level Required Behavior

Skill 1: mcp-exploratory-testing

This skill must collect locator candidates for meaningful elements observed during exploration.

It should capture:

* user-facing fields
* buttons
* links
* headings
* menus
* product cards
* cart badges
* validation messages
* confirmation messages
* workflow-critical controls
* repeated or dynamic elements

It should record locator candidates with:

* element name
* element type
* accessibility role
* accessible name or visible text
* placeholder or label if available
* test ID or data attribute if available
* candidate Playwright locator
* locator confidence
* rationale
* notes or risks

It must clearly state that these are locator candidates, not final implementation decisions.

⸻

Skill 2: exploratory-to-bdd

This skill must preserve locator candidate information as optional automation notes in Markdown BDD specs and traceability artifacts.

It must not pollute Gherkin scenarios with selectors.

BDD rule:

Gherkin = behavior only
Markdown BDD = behavior plus optional automation notes
Traceability = source evidence, including locator candidate references when useful

⸻

Skill 3: agentic-playwright-automation

This skill must use locator candidates from exploration artifacts as inputs during page object generation.

It must:

* review locator candidates before creating page objects
* select final locators using the project locator strategy
* document final locator decisions
* explain when it accepts or rejects an exploration candidate
* prefer robust, user-centered locators
* use data-test locators when they are clearly more stable or disambiguate repeated elements
* avoid XPath unless unavoidable
* preserve locator decision traceability in the implementation report

⸻

Locator Strategy

Use this locator priority as a general guide:

1. role/name
2. label
3. placeholder
4. text
5. test id / data-test
6. stable CSS
7. XPath only as a last resort

However, the skill must also recognize practical exceptions:

* If multiple elements share the same visible text, prefer a scoped locator, a product/card relationship, or a stable data-test locator.
* If an element is icon-only, a stable data-test locator may be better than text.
* If a control appears only after state changes, document that as a locator risk.
* If the locator depends on dynamic data, capture the data dependency.
* If MCP click behavior is unreliable for an element, document the tooling note separately from the locator decision.

⸻

Updates Required for mcp-exploratory-testing

Update SKILL.md

Add or update principles:

- Capture locator candidates for meaningful user-facing elements and workflow-critical controls.
- Record locator confidence and rationale.
- Prefer locator candidates in this order: role/name, label, placeholder, text, test id, stable CSS, XPath last.
- Treat locator candidates as exploration evidence, not final automation implementation decisions.
- Capture element relationships when locators depend on context, such as product cards, table rows, menus, repeated buttons, dialogs, and lists.
- Record locator risks for dynamic, repeated, hidden, conditional, or ambiguous elements.
- Separate application behavior observations from locator/tooling observations.

Add or update a section:

## Locator Candidate Capture Rules
During exploration, collect locator candidates for meaningful elements that may be used later in automation.
For each candidate, record:
| Field | Description |
|---|---|
| Element | Human-readable element name |
| Type | button, input, link, heading, message, card, list, menu, badge, etc. |
| Role | Accessibility role if available |
| Accessible Name / Text | Name or visible text used by a user |
| Placeholder / Label | Useful for form fields |
| Test ID / Data Attribute | Stable test attribute if available |
| Candidate Locator | Suggested Playwright locator |
| Confidence | High, Medium, Low |
| Rationale | Why this locator may be useful |
| Notes | Risks, ambiguity, dynamic state, repeated element issues |
Locator confidence guide:
- High: Stable accessible locator or stable test ID; element is unique in context.
- Medium: Visible text or CSS appears stable but may require scoping.
- Low: Dynamic, ambiguous, repeated, fragile, or dependent on layout.
Locator candidates must not be treated as final page object implementation decisions. Final locator decisions are made by the automation skill during page object creation.

Add or update:

## Repeated and Dynamic Element Rules
When elements repeat, such as product cards, table rows, search results, menu items, or repeated buttons:
1. Capture the repeated element group.
2. Identify the parent-child relationship.
3. Prefer scoped locator strategies.
4. Record whether a data-test attribute exists.
5. Record risks if a locator would click the first matching element globally.
6. Recommend a page object strategy but do not implement it.
Example:
| Element Group | Locator Challenge | Suggested Strategy |
|---|---|---|
| Product cards | Multiple buttons share text `Add to cart` | Locate card by product name, then find action inside card, or use product-specific `data-test` |

Add or update:

## Automation Handoff Rules
Exploration reports should include an Automation Handoff Notes section.
This section should summarize:
- recommended page models
- locator candidates to review
- locator risks
- repeated/dynamic element notes
- data dependencies
- tool interaction notes

⸻

Update Templates

Update these templates if they exist:

.claude/skills/mcp-exploratory-testing/templates/exploration_session_template.md
.claude/skills/mcp-exploratory-testing/templates/page_observation_template.md
.claude/skills/mcp-exploratory-testing/templates/page_model_candidate_template.md
.claude/skills/mcp-exploratory-testing/templates/exploration_review_template.md

In exploration_session_template.md

Inside each page section, add:

#### Locator Candidates
| Element | Type | Role | Accessible Name / Text | Placeholder / Label | Test ID / Data Attribute | Candidate Locator | Confidence | Rationale | Notes |
|---|---|---|---|---|---|---|---|---|---|
#### Locator Risks
- <Risk 1>
- <Risk 2>
#### Repeated or Dynamic Elements
| Element Group | Locator Challenge | Suggested Strategy | Notes |
|---|---|---|---|

Near the end of the report, add:

## Automation Handoff Notes
### Recommended Page Models
- <PageModelName>
### Locator Candidates to Review
| Page | Element | Candidate Locator | Confidence | Notes |
|---|---|---|---|---|
### Locator Risks
- <Risk 1>
- <Risk 2>
### Data Dependencies for Locators
| Element or Action | Data Dependency | Notes |
|---|---|---|
### Tooling Interaction Notes
- <Tooling note, such as MCP click fallback>

In page_observation_template.md

Add:

## Locator Candidates
| Element | Type | Role | Accessible Name / Text | Placeholder / Label | Test ID / Data Attribute | Candidate Locator | Confidence | Rationale | Notes |
|---|---|---|---|---|---|---|---|---|---|
## Locator Risks
- <Risk 1>
## Repeated or Dynamic Elements
| Element Group | Locator Challenge | Suggested Strategy | Notes |
|---|---|---|---|

In page_model_candidate_template.md

Add to each page model:

### Locator Candidates
| Element | Candidate Locator | Confidence | Notes |
|---|---|---|---|
### Locator Risks
- <Risk 1>

In exploration_review_template.md

Add checks:

| Locator candidates were captured | Pass/Fail/Needs Review |  |
| Locator confidence and rationale were included | Pass/Fail/Needs Review |  |
| Repeated or dynamic element risks were documented | Pass/Fail/Needs Review |  |
| Locator candidates were not treated as final implementation | Pass/Fail/Needs Review |  |

⸻

Add New Template

Create:

.claude/skills/mcp-exploratory-testing/templates/locator_candidate_template.md

Content:

# Locator Candidates: <Workflow Name>
## Purpose
This document records locator candidates observed during MCP exploration. These candidates are evidence for later automation design and are not final implementation decisions.
## Locator Strategy Reference
Preferred general order:
1. role/name
2. label
3. placeholder
4. text
5. test id / data-test
6. stable CSS
7. XPath only as a last resort
Practical exceptions:
- Use scoped locators or stable test IDs for repeated elements.
- Use data-test locators for icon-only elements or ambiguous controls.
- Document dynamic and conditional elements as locator risks.
## Candidates
| Page | Element | Type | Role | Accessible Name / Text | Placeholder / Label | Test ID / Data Attribute | Candidate Locator | Confidence | Rationale | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
## Repeated or Dynamic Elements
| Page | Element Group | Locator Challenge | Suggested Strategy | Notes |
|---|---|---|---|---|
## Locator Risks
| Page | Element | Risk | Impact | Recommendation |
|---|---|---|---|---|
## Automation Handoff Summary
| Page | Element | Recommended Candidate | Confidence | Review Needed? |
|---|---|---|---|---|

⸻

Update Checklists

Update:

.claude/skills/mcp-exploratory-testing/checklists/observation_quality_checklist.md
.claude/skills/mcp-exploratory-testing/checklists/test_idea_quality_checklist.md

Add a new checklist:

.claude/skills/mcp-exploratory-testing/checklists/locator_candidate_checklist.md

Content should include checks for:

* meaningful workflow elements captured
* candidate locator recorded
* role/name considered
* label or placeholder considered for inputs
* test ID or data attribute captured if available
* repeated element risks documented
* dynamic element risks documented
* confidence assigned
* rationale included
* not treated as final locator decision
* automation handoff notes included

⸻

Update Examples

Update SauceDemo examples to include locator candidates.

Files likely to update:

.claude/skills/mcp-exploratory-testing/examples/saucedemo_checkout_exploration.md
.claude/skills/mcp-exploratory-testing/examples/saucedemo_checkout_test_ideas.md

Add example locator candidates such as:

#### Locator Candidates
| Element | Type | Role | Accessible Name / Text | Placeholder / Label | Test ID / Data Attribute | Candidate Locator | Confidence | Rationale | Notes |
|---|---|---|---|---|---|---|---|---|---|
| Username input | input | textbox | Username | Username | `user-name` | `page.get_by_placeholder("Username")` | High | Stable placeholder observed | Alternative: `[data-test='username']` if present |
| Password input | input | textbox | Password | Password | `password` | `page.get_by_placeholder("Password")` | High | Stable placeholder observed | Alternative: `[data-test='password']` if present |
| Login button | button | button | Login |  | `login-button` | `page.get_by_role("button", name="Login")` | High | Accessible role/name is clear | Alternative: `[data-test='login-button']` |
| Shopping cart link | link | link | cart |  | `shopping-cart-link` | `page.locator("[data-test='shopping-cart-link']")` | High | Icon-only element; data-test is stable | Visible text may not be reliable |
| Backpack add button | button | button | Add to cart |  | `add-to-cart-sauce-labs-backpack` | `page.locator("[data-test='add-to-cart-sauce-labs-backpack']")` | High | Disambiguates repeated Add to cart buttons | Good page object candidate |
| Cart badge | badge |  | 1 |  | `shopping-cart-badge` | `page.locator("[data-test='shopping-cart-badge']")` | High | Conditional state indicator | Only visible after cart has item |

Also include:

#### Repeated or Dynamic Elements
| Element Group | Locator Challenge | Suggested Strategy | Notes |
|---|---|---|---|
| Inventory product cards | Multiple Add to cart buttons have similar text | Use product-specific data-test or locate product card by product name and scope button lookup | Avoid first global Add to cart locator |
| Cart badge | Appears only after cart has items | Assert visible after add; assert hidden after remove/reset | Conditional locator |

⸻

Updates Required for exploratory-to-bdd

Update SKILL.md

Add or update rules:

- Preserve locator candidate references from exploration artifacts as optional automation notes in Markdown BDD specs.
- Do not include raw selectors in Gherkin steps unless explicitly requested.
- Keep Gherkin behavior-focused and implementation-neutral.
- Include locator candidates in traceability or automation notes when they are useful for later automation.
- Do not treat locator candidates as final automation locators.

Add a section:

## Locator Candidate Handoff Rules
When source exploration artifacts include locator candidates:
1. Preserve them in Markdown BDD specs under an Automation Notes section.
2. Reference them in the traceability matrix when useful.
3. Do not place selectors directly inside Gherkin steps.
4. Mark locator candidates as non-final.
5. Preserve locator risks and repeated/dynamic element notes.
6. Carry forward open questions about unstable or ambiguous locators.

⸻

Update Markdown BDD Template

Update:

.claude/skills/exploratory-to-bdd/templates/markdown_bdd_spec_template.md

Add after Observed Evidence:

#### Automation Notes
These notes are optional implementation hints carried forward from exploration. They are not final automation decisions.
| Element or Action | Locator Candidate | Confidence | Source | Notes |
|---|---|---|---|---|
#### Locator Risks
- <Risk 1>
- <Risk 2>

⸻

Update Traceability Template

Update:

.claude/skills/exploratory-to-bdd/templates/traceability_matrix_template.md

Add columns:

| Locator Candidate Reference | Locator Risk |

The updated table should include:

| Case ID | Feature | Scenario | Source Type | Source Reference | Observed Evidence | Expected Outcome | Locator Candidate Reference | Locator Risk | Automation Priority | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|

⸻

Update BDD Quality Review Template

Update:

.claude/skills/exploratory-to-bdd/templates/bdd_quality_review_template.md

Add review checks:

| Gherkin avoids raw implementation selectors | Pass/Fail/Needs Review |  |
| Markdown spec preserves useful locator candidates as automation notes | Pass/Fail/Needs Review |  |
| Locator risks are preserved where relevant | Pass/Fail/Needs Review |  |

⸻

Update Examples

Update SauceDemo BDD examples to include locator candidates only in Markdown automation notes and traceability.

Do not add raw selectors to .feature files.

⸻

Updates Required for agentic-playwright-automation

Update SKILL.md

Add or update principles:

- Use locator candidates from exploration artifacts as evidence during page object generation.
- Review locator candidates before selecting final locators.
- Select final locators using the project locator strategy and practical stability rules.
- Document final locator decisions in the implementation report.
- Explain when an exploration locator candidate is accepted, modified, scoped, or rejected.
- Prefer scoped locators for repeated elements.
- Prefer stable data-test attributes when they disambiguate repeated controls or icon-only elements.
- Preserve traceability from final page object locator back to exploration candidate when possible.

Add a section:

## Locator Candidate Review and Final Locator Decision Rules
When generating page objects:
1. Read locator candidates from exploration reports, Markdown BDD automation notes, or traceability files.
2. Compare candidates against the locator strategy.
3. Check for repeated elements, dynamic elements, and ambiguity.
4. Select final locators for page object implementation.
5. Document the decision.
Decision values:
- Accepted
- Accepted with Scope
- Modified
- Rejected
- Needs Review
Decision table format:
| Page Object | Element | Candidate Locator | Final Locator | Decision | Rationale | Source |
|---|---|---|---|---|---|---|
Final locators should be implemented only after review against framework standards.

Add to page object rules:

Page objects should use final locator decisions, not raw unreviewed exploration candidates.

Add to implementation report rules:

Implementation reports must include a Locator Decision Log when locator candidates were available.

⸻

Update Templates

Update:

.claude/skills/agentic-playwright-automation/templates/page_object_template.py
.claude/skills/agentic-playwright-automation/templates/implementation_report_template.md
.claude/skills/agentic-playwright-automation/templates/automation_review_template.md

In implementation_report_template.md

Add:

## Locator Decision Log
| Page Object | Element | Candidate Locator | Final Locator | Decision | Rationale | Source |
|---|---|---|---|---|---|---|
Decision values:
- Accepted
- Accepted with Scope
- Modified
- Rejected
- Needs Review

Add:

## Locator Risks Carried Forward
| Page Object | Element | Risk | Mitigation |
|---|---|---|---|

In automation_review_template.md

Add review checks:

| Locator candidates were reviewed | Pass/Fail/Needs Review |  |
| Final locator decisions were documented | Pass/Fail/Needs Review |  |
| Repeated element locators are scoped or disambiguated | Pass/Fail/Needs Review |  |
| Dynamic element locator risks are addressed | Pass/Fail/Needs Review |  |

⸻

Add New Template

Create:

.claude/skills/agentic-playwright-automation/templates/locator_decision_log_template.md

Content:

# Locator Decision Log: <Feature or Scenario>
## Purpose
This document records how locator candidates from exploration were reviewed and converted into final page object locators.
## Locator Strategy Reference
Preferred general order:
1. role/name
2. label
3. placeholder
4. text
5. test id / data-test
6. stable CSS
7. XPath only as a last resort
Practical exceptions:
- Use scoped locators or data-test locators for repeated elements.
- Use data-test locators for icon-only elements.
- Document dynamic or conditional element risks.
## Decisions
| Page Object | Element | Candidate Locator | Final Locator | Decision | Rationale | Source |
|---|---|---|---|---|---|---|
## Rejected Candidates
| Element | Rejected Candidate | Reason | Replacement |
|---|---|---|---|
## Risks and Mitigations
| Page Object | Element | Risk | Mitigation |
|---|---|---|---|

⸻

Update Checklists

Update:

.claude/skills/agentic-playwright-automation/checklists/page_object_quality_checklist.md
.claude/skills/agentic-playwright-automation/checklists/locator_quality_checklist.md
.claude/skills/agentic-playwright-automation/checklists/automation_implementation_checklist.md

Add a new checklist:

.claude/skills/agentic-playwright-automation/checklists/locator_decision_checklist.md

Content should include:

* locator candidates reviewed
* final locator selected
* decision documented
* rationale included
* repeated element scoped or disambiguated
* dynamic element risk considered
* accessible locator preferred where stable
* data-test used when it improves stability or disambiguation
* XPath avoided unless unavoidable
* locator traceability preserved
* page object uses final locator, not raw unreviewed candidate

⸻

Update Examples

Update SauceDemo examples to include locator decision logs.

In:

.claude/skills/agentic-playwright-automation/examples/saucedemo_implementation_report.md

Add:

## Locator Decision Log
| Page Object | Element | Candidate Locator | Final Locator | Decision | Rationale | Source |
|---|---|---|---|---|---|---|
| LoginPage | Username input | `page.get_by_placeholder("Username")` | `page.get_by_placeholder("Username")` | Accepted | Stable placeholder and unique field | SauceDemo exploration |
| LoginPage | Password input | `page.get_by_placeholder("Password")` | `page.get_by_placeholder("Password")` | Accepted | Stable placeholder and unique field | SauceDemo exploration |
| LoginPage | Login button | `page.get_by_role("button", name="Login")` | `page.get_by_role("button", name="Login")` | Accepted | Accessible role/name is clear | SauceDemo exploration |
| InventoryPage | Shopping cart link | `page.locator("[data-test='shopping-cart-link']")` | `page.locator("[data-test='shopping-cart-link']")` | Accepted | Icon-only element; data-test is stable | SauceDemo exploration |

If existing example page objects exist, add comments only if appropriate, but do not clutter code.

⸻

Command Updates

Update these command files if present:

.claude/commands/explore-workflow.md
.claude/commands/explore-app.md
.claude/commands/review-exploration.md
.claude/commands/exploration-to-bdd.md
.claude/commands/generate-bdd.md
.claude/commands/review-bdd.md
.claude/commands/convert-bdd-to-playwright.md
.claude/commands/generate-playwright-test.md
.claude/commands/generate-playwright-suite.md
.claude/commands/review-playwright-test.md

explore-workflow.md

Add requirements:

- Capture locator candidates for meaningful workflow elements.
- Include locator confidence, rationale, and risks.
- Include repeated/dynamic element locator notes.
- Include Automation Handoff Notes with locator candidates to review.
- Do not treat locator candidates as final page object implementation.

explore-app.md

Add requirements:

- Capture locator candidates for primary navigation, forms, menus, and workflow-critical controls.
- Do not attempt exhaustive locator inventory for the entire application unless requested.

review-exploration.md

Add requirements:

- Review whether locator candidates were captured for meaningful elements.
- Review whether locator risks and repeated/dynamic element notes were documented.
- Review whether candidates are clearly marked as non-final.

exploration-to-bdd.md and generate-bdd.md

Add requirements:

- Preserve useful locator candidates in Markdown BDD Automation Notes.
- Do not insert raw selectors into Gherkin steps.
- Carry locator risks into traceability or BDD review artifacts.

review-bdd.md

Add requirements:

- Verify Gherkin remains behavior-focused and selector-free.
- Verify Markdown BDD preserves useful locator candidates as optional automation notes.

convert-bdd-to-playwright.md, generate-playwright-test.md, generate-playwright-suite.md

Add requirements:

- Read locator candidates from exploration reports, Markdown BDD automation notes, and traceability files if available.
- Produce a Locator Decision Log.
- Use final locator decisions in page objects.
- Explain accepted, modified, scoped, rejected, or needs-review locator decisions.

review-playwright-test.md

Add requirements:

- Review whether final locators align with locator candidate evidence and project locator strategy.
- Check whether repeated/dynamic elements are scoped or disambiguated.
- Check whether locator decisions are documented in the implementation report.

⸻

README Update

If a root README.md exists, add a short section:

## Locator Candidate Handoff
During MCP exploration, Claude Code captures locator candidates for meaningful elements. These candidates are stored in exploration reports as evidence for later automation.
Locator candidates are not final implementation decisions.
The BDD layer may preserve locator hints in Markdown Automation Notes, but Gherkin scenarios remain behavior-focused and selector-free.
During Playwright automation generation, Claude reviews locator candidates, chooses final locators using the framework locator strategy, and documents decisions in a Locator Decision Log.

Do not rewrite the full README unless necessary.

⸻

Acceptance Criteria

After implementation:

1. mcp-exploratory-testing skill includes locator candidate capture rules.
2. Exploration templates include locator candidate tables.
3. Exploration templates include locator risks.
4. Exploration templates include repeated/dynamic element notes.
5. Exploration templates include Automation Handoff Notes.
6. A new locator_candidate_template.md exists.
7. A new locator_candidate_checklist.md exists.
8. SauceDemo exploration examples include locator candidates.
9. exploratory-to-bdd skill preserves locator candidates as Markdown Automation Notes.
10. Gherkin template or rules explicitly avoid raw selectors.
11. Traceability template includes locator candidate references and locator risks.
12. BDD review template checks selector-free Gherkin and locator note preservation.
13. agentic-playwright-automation skill includes locator candidate review and final locator decision rules.
14. Automation implementation report includes a Locator Decision Log.
15. A new locator_decision_log_template.md exists.
16. A new locator_decision_checklist.md exists.
17. SauceDemo automation examples include locator decision log examples.
18. Commands are updated to capture, preserve, review, and use locator candidates appropriately.
19. README includes the Locator Candidate Handoff section if a README exists.
20. No automation code is generated outside examples.
21. No unrelated files are modified.

⸻

Implementation Instructions

Update the existing files now.

Do not ask follow-up questions.

Do not delete existing skill or command content.

Extend existing content cleanly.

Use clear, professional Markdown.

Do not install packages.

Do not run tests.

Do not generate project automation outside skill examples.

Do not modify unrelated files.

At the end, summarize:

* files updated
* files created
* how locator candidates now flow from exploration to BDD to automation
* any assumptions made
