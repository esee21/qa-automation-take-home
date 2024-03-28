from behave import Given, When, Then
from pages.Login.Login import Login

@When("user inputs '{email}' username")
def input_wrong_email(context, email):
    
    context.login.input_email(email)

@When("user inputs '{password}' password")
def input_wrong_password(context, password):
    
    context.login.input_password(password)
