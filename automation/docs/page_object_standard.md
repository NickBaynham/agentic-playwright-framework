# Page Object Standard

## Shape

- One class per page or significant view.
- Inherit from `framework.pages.base_page.BasePage`.
- Set `URL_PATH` to the route fragment relative to `base_url`.
- Constructor signature: `(self, page: Page, base_url: str)`.

## What belongs in a page object

- Locators exposed as `@property`.
- User actions named for intent: `login_as(user)`, `add_to_cart(product)`, `proceed_to_checkout()`.
- Composite actions that map to a single user step in the BDD spec.

## What does not belong in a page object

- Business assertions. A page object may call `expect(...).to_be_visible()` to confirm a precondition (the page actually loaded), but the assertion that proves the scenario passed lives in the test, not in the page object.
- Environment-specific data (URLs, credentials, product names). Accept these as method arguments or read them from injected fixtures.
- Cross-page navigation outside the page object's domain. If the action ends the page object's scope, return the new page object or have the test construct it.

## Locator placement

- Use the locator strategy: `get_by_role` > `get_by_label` > `get_by_placeholder` > `get_by_text` > `get_by_test_id` > stable CSS > XPath (last resort, with a comment).
- For repeated elements, scope by parent locator or use a per-instance `data-test`.
- Do not duplicate locator definitions across page objects. If the same region appears on multiple pages, extract a component.

## Example skeleton

```python
from playwright.sync_api import Page

from framework.pages.base_page import BasePage


class LoginPage(BasePage):
    URL_PATH = "/"

    @property
    def username_input(self):
        return self.page.get_by_placeholder("Username")

    @property
    def password_input(self):
        return self.page.get_by_placeholder("Password")

    @property
    def login_button(self):
        return self.page.get_by_role("button", name="Login")

    def login_as(self, user):
        self.username_input.fill(user.username)
        self.password_input.fill(user.password)
        self.login_button.click()
```
