from behave import When
from playwright.sync_api import TimeoutError
import components

@When("user clicks '{button_name}' button")
def clicks_button(context, button_name):
    
    button = components.ButtonLocator(button_name=button_name)

    context.page.locator(button.get_button_locator()).click()
    context.page.wait_for_load_state("networkidle")

@When("user clicks '{button_name}'")
def clicks_button(context, button_name):
    
    button = components.ButtonLocator(button_name=button_name)

    context.page.locator(button.get_locator()).click()
    context.page.wait_for_load_state("networkidle")

@When("user login '{record}' by clicking '{button}'")
def login_record(context, record, button):
    
    context.page.wait_for_load_state("networkidle")
    with context.page.expect_response(
            lambda response: record in response.url and response.request.method == 'POST') as response_info:
        context.execute_steps(f'''
            When user clicks '{button}' button
        ''')

    context.login_response = response_info.value

@When("user adds '{record}' by clicking '{button}'")
def add_record(context, record, button):
    
    context.page.wait_for_load_state("networkidle")
    with context.page.expect_response(
            lambda response: record in response.url and response.request.method == 'GET') as response_info:
        context.execute_steps(f'''
            When user clicks '{button}'
        ''')

    context.add_response = response_info.value

@When("user clicks an '{id}' ID in the list")
def select_product_in_list(context, id):

    context.page.locator("xpath=//*[contains(@href, '/product_details/" + id + "')]").click()
    context.page.wait_for_load_state("networkidle")
