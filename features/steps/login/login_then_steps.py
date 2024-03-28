from behave import Given, When, Then
from pages.Login.Login import Login

@Then("user is logged in")
def user_is_logged_in(context):

    assert context.login_response.status == 302

@Then("user is not logged in and receives an '{error_message}' error")
def check_error_message(context, error_message):

    context.page.wait_for_load_state("networkidle")
    assert context.login_response.status == 200
    selector = f"text='{error_message}'"
    context.login.error_message_is_visible(selector)
