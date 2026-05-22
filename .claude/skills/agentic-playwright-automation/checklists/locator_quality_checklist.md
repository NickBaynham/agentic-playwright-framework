# Locator Quality Checklist

Apply per locator used in tests, page objects, or components. Mark each item Pass, Fail, or Needs Review.

| Check | Status | Notes |
|---|---|---|
| `get_by_role(role, name=...)` preferred when an accessible role and name exist | | |
| `get_by_label(...)` used for labelled form controls | | |
| `get_by_placeholder(...)` used when label is unavailable | | |
| `get_by_text(...)` used only when the text is stable and unambiguous | | |
| `get_by_test_id(...)` used when accessible locators are insufficient | | |
| Stable CSS used only when no accessible locator works | | |
| XPath used only as a last resort, with a comment explaining why | | |
| Locator reflects user behavior rather than DOM structure | | |
