Feature: Login

  Scenario: Verify that a user can log in with valid credentials.
    Given user is in the login page
    When user inputs 'testuser' username
		And user inputs 'password123' password
    And user login 'login' by clicking 'Login'
    Then user is logged in
    
  Scenario: Ensure the system correctly handles invalid login attempts.
    Given user is in the login page
    When user inputs 'test' username
		And user inputs 'gibberish@123!' password
    And user login 'login' by clicking 'Login'
    Then user is not logged in and receives an 'Invalid credentials. Please try again.' error

  Scenario: Failed test to trigger screenshots of the final state of each test in the report for failed tests.
    Given user is in the login page
    When user inputs 'random' username
		And user inputs 'password123' password
    And user login 'login' by clicking 'Login'
    Then user is logged in