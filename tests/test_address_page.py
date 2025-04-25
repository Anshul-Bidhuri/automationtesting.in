import pytest

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

    def test_save_billing_address_first_name_field_min_length_check(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(first_name="f")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_box_displayed()

    def test_save_billing_address_with_empty_first_name_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(first_name="")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.first_name_mandatory_message_displayed()

    def test_save_billing_address_with_invalid_first_name_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(first_name="@anshu!")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_box_displayed()

    def test_save_billing_address_with_javascript_code_inside_first_name_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(first_name="<script>alert(1)</script>")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_box_displayed()

    def test_save_billing_address_last_name_field_min_length_check(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(last_name="f")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.error_box_displayed()

    def test_save_billing_address_with_empty_last_name_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(last_name="")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.first_name_mandatory_message_displayed()

    def test_save_billing_address_with_invalid_last_name_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(last_name="@anshu!")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.first_name_mandatory_message_displayed()

    def test_save_billing_address_with_empty_email_field(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(email="")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.first_name_mandatory_message_displayed()

    def test_save_billing_address_with_invalid_email_format(self):
        self.address_page_obj.fill_mandatory_fields_billing_address(email="anshu.com")
        self.address_page_obj.click_save_address_button()
        assert self.address_page_obj.first_name_mandatory_message_displayed()