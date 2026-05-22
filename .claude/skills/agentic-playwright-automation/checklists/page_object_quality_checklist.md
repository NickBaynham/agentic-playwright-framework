# Page Object Quality Checklist

Apply per page object class. Mark each item Pass, Fail, or Needs Review.

| Check | Status | Notes |
|---|---|---|
| Class is responsible for a single page or significant view | | |
| Important locators are exposed as `@property` for visibility from tests | | |
| User actions are methods named for user intent | | |
| No business assertions are hidden inside methods | | |
| No hard-coded URLs, credentials, or environment-specific data | | |
| Locator strategy follows the priority order (role/name > label > placeholder > text > test id > stable CSS > XPath) | | |
| No duplicate page objects exist for the same page | | |
| Class design is simple and readable | | |
