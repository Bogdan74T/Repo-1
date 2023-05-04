Feature: Check the forgot password functionality

  Background:
    Given forgot_pass: I am a user on the forgot password page

  @regression
  Scenario: Check validation error message when email is invalid format
    When forgot_pass: I fill in my email "my_email@"
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "Wrong email"

  @regression
  Scenario:  Check validation error message when email is empty
    When forgot_pass: I make sure the email input is cleared
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "Enter your email"

  @check_url
  Scenario: Check the forgot password page url
    Then base: Check the current url to be "https://demo.nopcommerce.com/passwordrecovery"

  @bat
  Scenario Outline: Check various email validation
    When forgot_pass: I fill in my email "<email>"
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "<expected_error>"
    Then forgot_pass: I verify the notification "<expected_notification>"

  Examples:
    |email        |expected_error  |expected_notification     |
    |test         |Wrong email     |None                      |
    |test@        |Wrong email     |None                      |
    |test@mail.com|None            |Email not found.          |