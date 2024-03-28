Feature: Product Listing

  Scenario: Verify that after login, the user can navigate to the product listing page.
    Given user is already logged in
    Then user should be redirected to 'product_listing' screen