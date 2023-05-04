Feature: Check the Login functionality

  Background:
     Given login: I am a user on the login page

  @login_test
  Scenario: Enter wrong credentials and check the error
    When login: I fill in an email "email@mail.com"
    When login: I fill in a password "pass"
    When login: I click the login button
    Then login: It shown an error message "Login was unsuccessful. Please correct the errors and try again."

  @check_url
  Scenario: Check the login page url
    Then base: Check the current url to be "https://demo.nopcommerce.com/login"