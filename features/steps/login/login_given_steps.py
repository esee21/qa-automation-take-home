from behave import Given, When, Then
from pages.Login.Login import Login

@Given("user is in the login page")
def load_login(context):
    
    context.login = Login(context.page)
    context.login.load_page()
