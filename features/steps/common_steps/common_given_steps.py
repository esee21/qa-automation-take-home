from behave import Given
from playwright.sync_api import TimeoutError

@Given("user is already logged in")
def load_login(context):
    
    context.execute_steps('''
            Given user is in the login page
            When user inputs 'testuser' username
            And user inputs 'password123' password
            And user clicks 'Login' button
        ''')
