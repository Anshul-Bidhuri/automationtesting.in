import time

from Helpers import driver_helpers, locators
from Pages.base_page import BasePage

from Helpers import customLogger, constants

log = customLogger.get_logger()


class LoginRegisterPage(BasePage):

    def enter_login_username(self, username):
        return driver_helpers.type_text(self.driver, locators.input_field_login_username, username)

    def enter_register_email(self, username):
        return driver_helpers.type_text(self.driver, locators.input_field_register_username, username)

    def enter_login_password(self, password):
        return driver_helpers.type_text(self.driver, locators.input_field_login_password, password)

    def enter_register_password(self, password):
        return driver_helpers.type_text(self.driver, locators.input_field_register_password, password)

    def click_login_button(self):
        return driver_helpers.click_element(self.driver, locators.button_login)

    def click_register_button(self):
        return driver_helpers.click_element(self.driver, locators.button_register)

    def is_error_message_displayed(self):
        return driver_helpers.is_displayed(self.driver, locators.error_message)

    def hello_text_should_not_be_displayed(self):
        time.sleep(1)
        status = driver_helpers.wait_until_element_not_visible(self.driver, locators.text_hello, timeout=10)
        if status:
            return True
        else:
            log.error("Hello text found after login")
            log.error("Going back to login page")
            driver_helpers.click_element(self.driver, locators.button_log_out)
            return False

    def is_registration_or_login_successful(self):
        status = driver_helpers.wait_till_element_is_clickable(self.driver, locators.button_sign_out, timeout=10)
        if status:
            log.info("Login successful")
            driver_helpers.click_element(self.driver, locators.button_log_out)
            return True
        else:
            log.error("Registration failed with correct creds")
            return False