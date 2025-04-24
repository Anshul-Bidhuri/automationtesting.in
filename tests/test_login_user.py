import pytest

from Helpers import constants
from Pages.login_register_page import LoginRegisterPage
import utility


@pytest.mark.run(order=2)
@pytest.mark.login_user
class TestLoginUser:

    @pytest.fixture(scope="class", autouse=True)
    def initiate_driver(self, setup_browser_login_screen, request):
        request.cls.login_page_obj = LoginRegisterPage(self.driver)

    def test_login_with_empty_email_and_password(self):
        self.login_page_obj.enter_login_username("")
        self.login_page_obj.enter_login_password("")
        self.login_page_obj.click_login_button()
        assert self.login_page_obj.is_error_message_displayed()

    def test_login_with_valid_email_and_empty_password(self):
        self.login_page_obj.enter_login_username(constants.ALREADY_REGISTERED_EMAIL)
        self.login_page_obj.enter_login_password("")
        self.login_page_obj.click_login_button()
        assert self.login_page_obj.is_error_message_displayed()

    def test_login_with_empty_email_and_valid_password(self):
        self.login_page_obj.enter_login_username("")
        self.login_page_obj.enter_login_password(constants.ALREADY_REGISTERED_PASSWORD)
        self.login_page_obj.click_login_button()
        assert self.login_page_obj.is_error_message_displayed()

    def test_login_with_invalid_email_format(self):
        self.login_page_obj.enter_login_username("invalidemail")
        self.login_page_obj.enter_login_password(constants.ALREADY_REGISTERED_PASSWORD)
        self.login_page_obj.click_login_button()
        assert self.login_page_obj.is_error_message_displayed()

    def test_login_with_unregistered_email(self):
        self.login_page_obj.enter_login_username("notregistered@example.com")
        self.login_page_obj.enter_login_password("SomePass123!")
        self.login_page_obj.click_login_button()
        assert self.login_page_obj.is_error_message_displayed()

    def test_login_with_wrong_password(self):
        self.login_page_obj.enter_login_username(constants.ALREADY_REGISTERED_EMAIL)
        self.login_page_obj.enter_login_password("WrongPassword!")
        self.login_page_obj.click_login_button()
        assert self.login_page_obj.is_error_message_displayed()

    def test_login_with_old_valid_credentials(self):
        self.login_page_obj.enter_login_username(constants.ALREADY_REGISTERED_EMAIL)
        self.login_page_obj.enter_login_password(constants.ALREADY_REGISTERED_PASSWORD)
        self.login_page_obj.click_login_button()
        assert self.login_page_obj.is_registration_or_login_successful()

    def test_login_with_new_registered_credentials(self):
        new_creds = utility.read_json_file("config.json").get("new_user_email_address")
        email, password = new_creds.get("consent_id"), new_creds.get("new_user_password")
        self.login_page_obj.enter_login_username(email)
        self.login_page_obj.enter_login_password(password)
        self.login_page_obj.click_login_button()
        assert self.login_page_obj.is_registration_or_login_successful()