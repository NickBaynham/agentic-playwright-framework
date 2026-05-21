# Sauce Labs Demo Test Cases

Target URL: <https://www.saucedemo.com/>

## TC-01: Standard User Login

User Story:
As a standard user,
I want to log in,
so that I can access the inventory page.

Acceptance Criteria:

1. Given I am on the login page
2. When I enter username "standard_user" and password "secret_sauce"
3. And I submit the login form
4. Then I should be redirected to /inventory.html
5. And I should see the Products page heading
6. And I should see a shopping cart icon

## TC-02: Add Item to Cart from Inventory

User Story:
As a logged-in user,
I want to add a product to my cart from the inventory page,
so that I can purchase it later.

Acceptance Criteria:

1. Given I am on the Products page
2. When I click the "Add to cart" button for "Sauce Labs Backpack"
3. Then the button label should change to "Remove"
4. And the shopping cart badge should display "1"

## TC-03: Navigate to Cart

User Story:
As a user with items in my cart,
I want to navigate to the cart page,
so that I can review my selections.

Acceptance Criteria:

1. Given I have at least one item in the cart
2. When I navigate to the cart page
3. Then I should be on /cart.html
4. And I should see the "Your Cart" heading
5. And I should see each added item with its quantity, name, description, and price
6. And I should see "Continue Shopping" and "Checkout" buttons

## TC-04: Proceed to Checkout

User Story:
As a user reviewing my cart,
I want to proceed to checkout,
so that I can complete my purchase.

Acceptance Criteria:

1. Given I am on the cart page with at least one item
2. When I click the "Checkout" button
3. Then I should be redirected to /checkout-step-one.html
4. And I should see the "Checkout: Your Information" heading
5. And I should see input fields for First Name, Last Name, and Zip/Postal Code

## TC-05: Submit Checkout Information

User Story:
As a checking-out user,
I want to submit my shipping information,
so that I can proceed to the order overview.

Acceptance Criteria:

1. Given I am on the Checkout: Your Information page
2. When I enter a valid First Name, Last Name, and Zip/Postal Code
3. And I click the "Continue" button
4. Then I should be redirected to /checkout-step-two.html
5. And I should see the "Checkout: Overview" heading
6. And I should see the items, payment information, shipping information, item total, tax, and total

## TC-06: Finish Checkout

User Story:
As a user on the checkout overview,
I want to finalize my purchase,
so that my order is confirmed.

Acceptance Criteria:

1. Given I am on the Checkout: Overview page
2. When I click the "Finish" button
3. Then I should be redirected to /checkout-complete.html
4. And I should see the "Thank you for your order!" confirmation
5. And I should see a "Back Home" button

## TC-07: Return to Inventory After Checkout

User Story:
As a user who has just completed an order,
I want to return to the products page,
so that I can continue shopping.

Acceptance Criteria:

1. Given I am on the Checkout: Complete page
2. When I click the "Back Home" button
3. Then I should be redirected to /inventory.html
4. And I should see the Products page

## TC-08: Reset App State from Side Menu

User Story:
As a logged-in user,
I want to reset the application state,
so that my cart and selections are cleared.

Acceptance Criteria:

1. Given I am logged in
2. When I open the side menu
3. And I click "Reset App State"
4. Then the cart badge should no longer be displayed
5. And any previously selected "Remove" buttons should revert to "Add to cart"

## TC-09: Navigate to About Page

User Story:
As a logged-in user,
I want to navigate to the About page,
so that I can learn more about Sauce Labs.

Acceptance Criteria:

1. Given I am logged in
2. When I open the side menu
3. And I click the "About" link
4. Then I should be navigated to <https://saucelabs.com/>

## TC-10: Verify Inventory Product Count

User Story:
As a user on the Products page,
I want to view all available products,
so that I can choose what to buy.

Acceptance Criteria:

1. Given I am on the Products page
2. When the page is fully loaded
3. Then I should see exactly 6 products
4. And the products listed should be: Sauce Labs Backpack, Sauce Labs Bike Light, Sauce Labs Bolt T-Shirt, Sauce Labs Fleece Jacket, Sauce Labs Onesie, Test.allTheThings() T-Shirt (Red)

## TC-11: Identify Most Expensive Product

User Story:
As a user browsing products,
I want to identify the most expensive product,
so that I can make an informed purchasing decision.

Acceptance Criteria:

1. Given I am on the Products page
2. When I sort or inspect the product prices
3. Then the most expensive product should be "Sauce Labs Fleece Jacket" priced at $49.99

## TC-12: Purchase the Most Expensive Item End-to-End

User Story:
As a standard user,
I want to purchase the most expensive item in the catalog,
so that I can complete an end-to-end order for it.

Acceptance Criteria:

1. Given I am on the Products page
2. When I click "Add to cart" for "Sauce Labs Fleece Jacket"
3. And I navigate to the cart page
4. And I click the "Checkout" button
5. And I enter valid First Name, Last Name, and Zip/Postal Code
6. And I click "Continue"
7. Then the order summary should show item total $49.99, tax $4.00, and total $53.99
8. When I click "Finish"
9. Then I should be redirected to /checkout-complete.html
10. And I should see the "Thank you for your order!" confirmation
