@checkout @login @cart
Feature: Standard User Checkout
  A returning standard user can sign in, add a product, complete checkout,
  and receive an order confirmation on the Swag Labs storefront.

  @ui @smoke @login @positive @automatable
  Scenario: Standard user logs in successfully
    Given the standard user is on the saucedemo login page
    When the user signs in with valid standard credentials
    Then the user lands on the products page

  @ui @smoke @cart @positive @automatable
  Scenario: Adding one product updates the cart badge and toggles the Add button to Remove
    Given the standard user is logged in and viewing the inventory page
    When the user adds "Sauce Labs Backpack" to the cart from the inventory listing
    Then the cart badge shows 1
    And the "Sauce Labs Backpack" action button is labeled "Remove"

  @ui @smoke @cart @positive @automatable
  Scenario: Cart page lists the added item with the correct name, quantity, and price
    Given the standard user is logged in
    And the user has added "Sauce Labs Backpack" to the cart
    When the user opens the cart
    Then the cart lists exactly one line item for "Sauce Labs Backpack"
    And the line item shows quantity 1 and price "$29.99"
    And a Checkout action is available

  @ui @smoke @checkout @positive @automatable
  Scenario: Checkout information form advances to the overview with valid input
    Given the standard user is on the checkout information page with one item in the cart
    When the user submits the checkout information form with:
      | First Name | Last Name | Zip/Postal Code |
      | Test       | User      | 12345           |
    Then the user lands on the checkout overview page

  @ui @smoke @checkout @positive @automatable
  Scenario: Overview page totals satisfy Item total + Tax = Total
    Given the standard user is on the checkout overview page with "Sauce Labs Backpack" in the cart
    When the user reads the Item total, Tax, and Total values
    Then Total equals Item total plus Tax
    And Item total, Tax, and Total are all present and non-empty

  @ui @smoke @checkout @positive @automatable
  Scenario: Finishing the order shows the order confirmation page
    Given the standard user is on the checkout overview page with "Sauce Labs Backpack" in the cart
    When the user submits the order
    Then the user lands on the order confirmation page
    And a "Thank you for your order!" confirmation heading is visible

  @ui @cart @positive @needs-clarification
  Scenario: Cart is empty after order completion
    Given the standard user has just completed a checkout
    When the user returns to the inventory page
    Then the cart badge is not displayed

  @ui @checkout @negative @needs-clarification
  Scenario Outline: Checkout information form rejects missing required fields
    Given the standard user is on the checkout information page with one item in the cart
    When the user submits the checkout information form with first name "<first_name>", last name "<last_name>", and postal code "<postal_code>"
    Then the user remains on the checkout information page
    And a field-specific error message is displayed for the missing required field

    Examples:
      | first_name | last_name | postal_code |
      |            | User      | 12345       |
      | Test       |           | 12345       |
      | Test       | User      |             |
