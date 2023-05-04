from behave import *


@Given('login: I am a user on the login page')
def step_impl(context):
    context.login_page.navigate_to_login_page()

@When('login: I fill in an email "{mail}"')
def step_impl(context,mail):
    context.login_page.set_email(mail)

@When('login: I fill in a password "{password}"')
def step_impl(context,password):
    context.login_page.set_password(password)

@When('login: I click the login button')
def step_impl(context):
    context.login_page.click_login_button()

@Then('login: It shown an error message "{msg}"')
def step_impl(context,msg):
    context.login_page.verify_login_error_message(msg)