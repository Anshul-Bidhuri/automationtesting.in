import pytest
import random

from Helpers import constants
from Pages.address_page import AddressPage
import utility


@pytest.mark.run(order=3)
@pytest.mark.address_page
class TestAddressPage:

    @pytest.fixture(scope="class", autouse=True)
    def initiate_driver(self, setup_browser_address_page, request):
        request.cls.address_page_obj = AddressPage(self.driver)

    @pytest.fixture(scope="function", autouse=True)
    def navigate_to_edit_bill_address_page(self, request):
        self.address_page_obj.open_edit_billing_address_page()

    @pytest.fixture(scope="module")
    def values_of_address_page(self):
        return {'country': random.choice(constants.COUNTRIES), 'state': random.choice(constants.STATES),
                'first_name': random.choice(constants.FIRST_NAME), 'last_name': random.choice(constants.LAST_NAME),
                'company_name': random.choice(constants.COMPANY_NAME), 'email': random.choice(constants.EMAIL),
                'phone': random.choice(constants.PHONE), 'address_1': random.choice(constants.ADDRESS_1),
                'address_2': random.choice(constants.ADDRESS_2), 'city': random.choice(constants.CITY),
                'postcode': random.choice(constants.POSTCODE)}

    def test_save_billing_address_first_name_field_min_length_check(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(first_name="f")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="First Name is too short (minimum is 3 characters).")  # there should be some error message like this

    def test_save_billing_address_with_empty_first_name_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(first_name="")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="First Name is a required field.")

    def test_save_billing_address_with_invalid_first_name_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(first_name="@anshu!")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="First Name field should not contain special characters.")

    def test_save_billing_address_with_javascript_code_inside_first_name_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(first_name="<script>alert(1)</script>")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="First Name should not contain special characters.")

    def test_save_billing_address_last_name_field_min_length_check(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(last_name="f")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Last Name is too short (minimum is 3 characters).")

    def test_save_billing_address_with_empty_last_name_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(last_name="")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Last Name is a required field.")

    def test_save_billing_address_with_invalid_last_name_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(last_name="@anshu!")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Last Name field should not contain special characters.")

    def test_save_billing_address_with_javascript_code_inside_last_name_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(last_name="<script>alert(1)</script>")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Last Name should not contain special characters.")

    def test_save_billing_address_with_empty_email_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(email="")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Email Address is a required field.")

    def test_save_billing_address_with_invalid_email_format(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(email="anshu.com")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Email Address is not valid.")

    def test_save_billing_address_with_javascript_code_inside_email_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(email="<script>alert(1)</script>")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Email Address is not valid.")

    def test_save_billing_address_with_javascript_code_inside_company_name_field(self):
        self.address_page_obj.enter_billing_address_company_name(value="<script>alert(1)</script>")
        self.address_page_obj.fill_mandatory_fields_billing_address()
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Company Name should not contain special characters.")

    def test_save_billing_address_with_invalid_char_inside_company_name_field(self):
        self.address_page_obj.enter_billing_address_company_name(value="@&^!#^&*")
        self.address_page_obj.fill_mandatory_fields_billing_address()
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Company Name field should not contain special characters.")

    def test_save_billing_address_with_empty_phone_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(phone="")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Phone is a required field.")

    def test_save_billing_address_with_invalid_phone_format(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(phone="98")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Phone is not valid.")

    def test_save_billing_address_with_max_length_phone_check(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(phone="987987987987987987987")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Phone is not valid.")

    def test_save_billing_address_with_javascript_code_inside_phone_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(phone="<script>alert(1)</script>")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Phone is not valid.")

    def test_save_billing_address_with_string_inside_phone_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(phone="abcdefgh")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Phone is not valid.")

    def test_save_billing_address_with_empty_address_1_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(address_1="")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Address is a required field.")

    def test_save_billing_address_with_invalid_address_1_format(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(address_1="98@$@@!!")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Address is not valid.")

    def test_save_billing_address_with_min_length_address_1_check(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(address_1="abc")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Address is not valid.")

    def test_save_billing_address_with_javascript_code_inside_address_1_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(address_1="<script>alert(1)</script>")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Address is not valid.")

    def test_save_billing_address_with_javascript_code_inside_address_2_field(self):
        self.address_page_obj.enter_billing_address_address_2(value="<script>alert(1)</script>")
        self.address_page_obj.fill_mandatory_fields_billing_address()
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Address field should not contain special characters.")

    def test_save_billing_address_with_invalid_char_inside_address_2_field(self):
        self.address_page_obj.enter_billing_address_address_2(value="@&^!#^&*")
        self.address_page_obj.fill_mandatory_fields_billing_address()
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Address field should not contain special characters.")

    def test_save_billing_address_with_empty_city_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(city="")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Town / City is a required field.")

    def test_save_billing_address_with_invalid_city_format(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(city="98@$@@!!")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="City is not valid.")

    def test_save_billing_address_with_min_length_city_check(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(city="ab")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="City is not valid.")

    def test_save_billing_address_with_javascript_code_inside_city_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(city="<script>alert(1)</script>")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="City is not valid.")

    def test_save_billing_address_with_empty_postcode_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(postcode="")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Postcode / ZIP is a required field.")

    def test_save_billing_address_with_invalid_postcode_format(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(postcode="98")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Postcode is not valid.")

    def test_save_billing_address_with_max_length_postcode_check(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(postcode="987987987987987987987")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Postcode is not valid.")

    def test_save_billing_address_with_javascript_code_inside_postcode_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(postcode="<script>alert(1)</script>")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Postcode is not valid.")

    def test_save_billing_address_with_string_inside_postcode_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(postcode="abcdefgh")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_message_displayed(error_message="Postcode is not valid.")

    def test_billing_address_country_dropdown(self):
        country = random.choice(constants.COUNTRIES)
        self.address_page_obj.select_country_from_dropdown(country_name=country)
        selected_country = self.address_page_obj.get_selected_country_from_dropdown()
        assert selected_country == country

    def test_billing_address_state_dropdown(self):
        state_name = random.choice(constants.STATES)
        self.address_page_obj.select_state_from_dropdown(state_name=state_name)
        selected_state = self.address_page_obj.get_selected_state_from_dropdown()
        assert selected_state == state_name

    def test_complete_edit_billing_address(self, values_of_address_page):
        self.address_page_obj.fill_mandatory_fields_billing_address(city=values_of_address_page['city'], postcode=values_of_address_page['postcode'])
