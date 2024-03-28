class ButtonLocator:

    def __init__(self, button_name=None):

        self.button_name = button_name

    def get_button_locator(self):

        return f"xpath=//button[text()='{self.button_name}']"
    
    def get_locator(self):

        return f"xpath=//*[text()='{self.button_name}']"
