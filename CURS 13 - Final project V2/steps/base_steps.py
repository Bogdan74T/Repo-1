from behave import *


@Then('base: Check the current url to be "{url}"')
def step_impl(context,url):
    context.base_page.check_the_current_url(url)