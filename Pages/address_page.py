import time

from Helpers import driver_helpers, locators
from Pages.base_page import BasePage

from Helpers import customLogger, constants

log = customLogger.get_logger()


class AddressPage(BasePage):

    def enter_billing_address_first_name(self, value="raju"):
        return driver_helpers.type_text(self.driver, locators.input_billing_first_name, value)

    def enter_billing_address_last_name(self, value="kumar"):
        return driver_helpers.type_text(self.driver, locators.input_billing_last_name, value)

    def enter_billing_address_company_name(self, value="centime"):
        return driver_helpers.type_text(self.driver, locators.input_billing_company_name, value)

    def enter_billing_address_email(self, value="ansh@123.com"):
        return driver_helpers.type_text(self.driver, locators.input_billing_email_address, value)

    def enter_billing_address_phone_number(self, value="9999999988"):
        return driver_helpers.type_text(self.driver, locators.input_billing_phone, value)

    def enter_billing_address_address_1(self, value="58 kailash colony"):
        return driver_helpers.type_text(self.driver, locators.input_billing_address_1, value)

    def enter_billing_address_address_2(self, value="near ram hospital"):
        return driver_helpers.type_text(self.driver, locators.input_billing_address_2, value)

    def enter_billing_address_city(self, value="Delhi"):
        return driver_helpers.type_text(self.driver, locators.input_billing_city, value)

    def enter_billing_address_postcode(self, value="110025"):
        return driver_helpers.type_text(self.driver, locators.input_billing_postcode, value)

    def click_save_address_button(self):
        return driver_helpers.click_element(self.driver, locators.button_save_address)

    def first_name_mandatory_message_displayed(self):
        return driver_helpers.is_displayed(self.driver, locators.error_message_first_name_required, timeout=5)

    def error_box_displayed(self):
        time.sleep(2)
        return driver_helpers.is_displayed(self.driver, locators.error_box, timeout=5)

    def save_address_message_displayed(self):
        return driver_helpers.is_displayed(self.driver, locators.message_address_changed_successfully, timeout=5)

    def open_edit_billing_address_page(self):
        current_url = driver_helpers.get_current_url(self.driver)
        if current_url != constants.BILL_ADDRESS_EDIT_PAGE_URL:
            self.driver.get(constants.BILL_ADDRESS_EDIT_PAGE_URL)

    def fill_mandatory_fields_billing_address(self, **kwargs):
        self.enter_billing_address_first_name(value=kwargs.get("first_name")) if "first_name" in kwargs else self.enter_billing_address_first_name()
        self.enter_billing_address_last_name(value=kwargs.get("last_name")) if "last_name" in kwargs else self.enter_billing_address_last_name()
        self.enter_billing_address_email(value=kwargs.get("email")) if "email" in kwargs else self.enter_billing_address_email()
        self.enter_billing_address_phone_number(value=kwargs.get("phone")) if "phone" in kwargs else self.enter_billing_address_phone_number()
        self.enter_billing_address_address_1(value=kwargs.get("address_1")) if "address_1" in kwargs else self.enter_billing_address_address_1()
        self.enter_billing_address_city(value=kwargs.get("city")) if "city" in kwargs else self.enter_billing_address_city()
        self.enter_billing_address_postcode(value=kwargs.get("postcode")) if "postcode" in kwargs else self.enter_billing_address_postcode()
