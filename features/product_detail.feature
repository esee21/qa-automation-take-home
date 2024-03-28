Feature: Product Detail

  Scenario: Implement a test to verify that clicking on a product in the listing page navigates to the correct product details page.
    Given user is already logged in
    When user clicks an '1' ID in the list
    Then user should see product details page
    
  Scenario: Test adding a product to the shopping cart from the product details page.
    Given user is already logged in
    When user clicks an '1' ID in the list
    And user adds 'add_to_cart' by clicking 'Add to Cart'
    Then user should be redirected to 'product_listing' screen
    And validate that the product was added successfully