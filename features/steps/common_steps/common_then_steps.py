from behave import Then
from playwright.sync_api import TimeoutError

@Then("user should be redirected to '{screen}' screen")
def check_current_screen_url(context, screen):

    url = f"/{screen}"

    try:
        context.page.wait_for_url(url=url)
    except TimeoutError:
        raise Exception("Page with the given URL is not loading within 30sec")
    except:
        raise Exception("Unknown error occured")

    assert screen in context.page.url

@Then("validate that the product was added successfully")
def validate_cart_response(context):
    
    assert context.add_response.status == 302

@Then("user should see product details page")
def validate_product_details_screen(context):
    
    context.page.wait_for_selector("//a[text()='View Cart']")
    context.page.wait_for_selector("//h1[contains(text(), 'Product')]")
    context.page.wait_for_selector("//p[contains(text(), 'This is product')]")
    context.page.wait_for_selector("//a[text()='Add to Cart']")
