# Locator Strategy

## Priority

Always try these in order. Drop to the next only when the prior tier is insufficient.

1. `page.get_by_role(role, name=...)` — accessible role plus accessible name.
2. `page.get_by_label("...")` — labelled form controls.
3. `page.get_by_placeholder("...")` — when a label is not present.
4. `page.get_by_text("...")` — stable, unambiguous visible text.
5. `page.get_by_test_id("...")` — when accessible locators are insufficient.
6. Stable CSS selectors.
7. XPath — last resort, with a comment explaining why.

The principle: locators should reflect how a user identifies the element, not how the DOM happens to be structured.

## Practical Exceptions

- **Repeated elements:** if multiple elements share the same visible text or role/name (e.g., six `Add to cart` buttons on an inventory page), prefer a scoped locator (locate the parent product card, then find the action inside it) or a per-instance `data-test` attribute.
- **Icon-only controls:** elements that render only an icon often have no accessible name. Prefer `data-test` over text or role/name.
- **Conditional elements:** elements that appear only after a state change (badges, error banners, confirmation messages) need locators that can also assert absence cleanly. Use `expect(...).to_be_hidden()` and `to_be_visible()` rather than presence-based reads.
- **Dynamic numeric content:** totals, counters, and timestamps render with varying text. Locate by structure (`[data-test='total-label']`) and parse the value rather than exact-matching the string.

## Source

Locator candidates come from MCP exploration session reports under `sessions/mcp-exploration/` and from Markdown BDD Automation Notes under `specs/bdd/markdown/`. These are evidence, not final decisions. The implementation report's Locator Decision Log records the final choice.

## Decisions

Every locator selection records a decision in the implementation report:

- **Accepted** — exploration candidate used as-is.
- **Accepted with Scope** — exploration candidate adopted with additional scoping.
- **Modified** — exploration candidate adjusted (different role name, switched from text to `data-test`, etc.).
- **Rejected** — exploration candidate not used; alternative selected, with rationale.
- **Needs Review** — decision deferred pending clarification.

## XPath

Avoid XPath unless none of the above works. When XPath is unavoidable, add a code comment explaining why and record it as an Open Question in the implementation report. A required XPath usually indicates a missing accessible name or `data-test`; that gap is worth flagging to the application team.
