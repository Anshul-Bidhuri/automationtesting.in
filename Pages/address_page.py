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


    def fill_mandatory_fields_billing_address(self, except_field=None):
        if except_field ==