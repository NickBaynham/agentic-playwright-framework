# Locator Decision Checklist

Apply when generating or reviewing page object locators after exploration and BDD artifacts have provided locator candidates. Each item should be Pass, Fail, or Needs Review.

| Check | Status | Notes |
|---|---|---|
| Exploration locator candidates were reviewed before writing locators | | |
| Markdown BDD Automation Notes were reviewed where present | | |
| A final locator was selected for each element used in the page object | | |
| The decision (Accepted / Accepted with Scope / Modified / Rejected / Needs Review) is documented | | |
| Rationale is included for each decision | | |
| Repeated elements are scoped or disambiguated (per-product data-test, parent-card scope, etc.) | | |
| Dynamic or conditional elements have their risk acknowledged | | |
| Accessible locators (role/name, label, placeholder, text) were preferred when stable | | |
| `data-test` / test id was used when it improves stability or disambiguation | | |
| Stable CSS was used only where accessible locators are insufficient | | |
| XPath was avoided unless unavoidable, with a comment explaining why | | |
| Locator traceability from final locator back to the exploration candidate is preserved | | |
| Page object uses the final locator, not a raw unreviewed candidate | | |
