from Helpers import driver_helpers, locators
from Pages.base_page import BasePage


class LoginPage(BasePage):

    def enter_login_username(self, username):
        return driver_helpers.type_text(self.driver, locators.input_field_login_username, username)

    def enter_login_password(self, password):
        return driver_helpers.type_text(self.driver, locators.input_field_login_password, password)

    def click_login_button(self):
        return driver_helpers.click_element(self.driver, locators.button_login)

    def is_error_message_displayed(self):
        return driver_helpers.is_displayed(self.driver, locators.error_message)