from playwright.sync_api import Page

class LoginLocators:

    EMAIL = "[placeholder='Username']"
    PASSWORD = "[placeholder='Password']"

class Login:

    def __init__(self, page: Page):

        self.page = page
    
    def load_page(self):

        self.page.goto("http://127.0.0.1:5000/login")
    
    def input_email(self, email):

        self.page.locator(LoginLocators.EMAIL) \
        .type(email)
    
    def input_password(self, password):

        self.page.locator(LoginLocators.PASSWORD) \
        .type(password)
    
    def error_message_is_visible(self, selector):

        assert self.page.locator(selector).is_visible()