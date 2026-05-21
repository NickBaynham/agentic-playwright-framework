@login
Feature: SauceDemo Standard User Login
  A standard user can sign in to the SauceDemo storefront and reach the product catalog.

  Background:
    Given the user is on the SauceDemo login page

  @ui @smoke @login @positive @automatable
  Scenario: Standard user logs in successfully
    When the user signs in with valid standard credentials
    Then the user is taken to the products page
    And the shopping cart is visible in the header
