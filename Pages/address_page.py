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

    def error_message_displayed(self, error_message):
        log.info(f"Error message: '{error_message}' should be displayed")
        status = driver_helpers.is_displayed(self.driver, locators.error_message_field_required.format(error_message=error_message), timeout=3)
        if status:
            log.info(f"Error message: '{error_message}' is displayed")
            return True
        else:
            log.error(f"Error message: '{error_message}' is not found")
            return False

    def error_box_displayed(self):
        time.sleep(2)
        return driver_helpers.is_displayed(self.driver, locators.error_box, timeout=5)

    def select_country_from_dropdown(self, country_name):
        driver_helpers.click_element(self.driver, locators.dropdown_selected_country)
        driver_helpers.type_text(self.driver, locators.input_dropdown_select_country, country_name)
        driver_helpers.click_element(self.driver, locators.dropdown_select_country_result.format(country_name=country_name))

    def get_selected_country_from_dropdown(self):
        return driver_helpers.get_text(self.driver, locators.dropdown_selected_country)

    def select_state_from_dropdown(self, state_name):
        try:
            # this is another bug, website dropdown sometimes changes to input field
            driver_helpers.type_text(self.driver, locators.input_field_state, state_name)
        except:
            driver_helpers.click_element(self.driver, locators.dropdown_selected_state, timeout=5)
            driver_helpers.type_text(self.driver, locators.input_dropdown_select_state, state_name)
            driver_helpers.click_element(self.driver, locators.dropdown_select_state_result.format(state_name=state_name))

    def get_selected_state_from_dropdown(self):
        return driver_helpers.get_text(self.driver, locators.dropdown_selected_state)

    def save_address_message_displayed(self):
        return driver_helpers.is_displayed(self.driver, locators.message_address_changed_successfully, timeout=5)

    def open_edit_billing_address_page(self):
        current_url = driver_helpers.get_current_url(self.driver)
        if current_url != constants.BILL_ADDRESS_EDIT_PAGE_URL:
            driver_helpers.get_page(self.driver, constants.BILL_ADDRESS_EDIT_PAGE_URL)

    def open_address_page(self):
        current_url = driver_helpers.get_current_url(self.driver)
        if current_url != constants.ADDRESS_PAGE_URL:
            driver_helpers.get_page(self.driver, constants.ADDRESS_PAGE_URL)

    def get_current_saved_billing_address(self):
        return driver_helpers.get_text(self.driver, locators.text_billing_address)

    def compare_saved_address_with_billing_address(self, entered_values):
        address_on_ui = self.get_current_saved_billing_address()
        count = 0
        for key, value in (entered_values.items()):
            if value not in address_on_ui:
                log.error(f"Expected '{key}' address value '{value}' is not present on UI address")
                count +=1
        if count == 0:
            log.info(f"Expected address values are present on UI {address_on_ui}")
            return True
        else:
            return False

    def fill_mandatory_fields_billing_address(self, **kwargs):
        self.enter_billing_address_first_name(value=kwargs.get("first_name")) if "first_name" in kwargs else self.enter_billing_address_first_name()
        self.enter_billing_address_last_name(value=kwargs.get("last_name")) if "last_name" in kwargs else self.enter_billing_address_last_name()
        self.enter_billing_address_email(value=kwargs.get("email")) if "email" in kwargs else self.enter_billing_address_email()
        self.enter_billing_address_phone_number(value=kwargs.get("phone")) if "phone" in kwargs else self.enter_billing_address_phone_number()
        self.enter_billing_address_address_1(value=kwargs.get("address_1")) if "address_1" in kwargs else self.enter_billing_address_address_1()
        self.enter_billing_address_city(value=kwargs.get("city")) if "city" in kwargs else self.enter_billing_address_city()
        self.enter_billing_address_postcode(value=kwargs.get("postcode")) if "postcode" in kwargs else self.enter_billing_address_postcode()
