import pytest

from Helpers import constants
from Pages.login_register_page import LoginPage


class TestLoginRegisterPage:

    @pytest.fixture(scope="class", autouse=True)
    def initiate_driver(self, setup_browser_login_screen, request):
        request.cls.login_page_obj = LoginPage(self.driver)

    def test_register_with_empty_email_and_password(self):
        self.login_page_obj.enter_register_email("")
        self.login_page_obj.enter_register_password("")
        self.login_page_obj.click_register_button()
        assert self.login_page_obj.hello_text_should_not_be_displayed()

    def test_register_with_valid_email_and_empty_password(self):
        self.login_page_obj.enter_register_email("validemail@example.com")
        self.login_page_obj.enter_register_password("")
        self.login_page_obj.click_register_button()
        assert self.login_page_obj.hello_text_should_not_be_displayed()

    def test_register_with_empty_email_and_valid_password(self):
        self.login_page_obj.enter_register_email("")
        self.login_page_obj.enter_register_password("ValidPass123!")
        self.login_page_obj.click_register_button()
        assert self.login_page_obj.hello_text_should_not_be_displayed()

    def test_register_with_invalid_email_format(self):
        self.login_page_obj.enter_register_email("invalidemail")
        self.login_page_obj.enter_register_password("ValidPass123!")
        self.login_page_obj.click_register_button()
        assert self.login_page_obj.hello_text_should_not_be_displayed()

    def test_register_with_already_registered_email(self):
        self.login_page_obj.enter_register_email(constants.ALREADY_REGISTERED_EMAIL)
        self.login_page_obj.enter_register_password(constants.ALREADY_REGISTERED_PASSWORD)
        self.login_page_obj.click_register_button()
        assert self.login_page_obj.hello_text_should_not_be_displayed()

    def test_register_with_weak_password(self):
        self.login_page_obj.enter_register_email("weakpassuser@example.com")
        self.login_page_obj.enter_register_password("123")
        self.login_page_obj.click_register_button()
        assert self.login_page_obj.hello_text_should_not_be_displayed()

    def test_register_with_valid_new_email_and_password(self):
        import time
        unique_email = f"testuser_{int(time.time())}@example.com"
        self.login_page_obj.enter_register_email(unique_email)
        self.login_page_obj.enter_register_password("ValidPass123!")
        self.login_page_obj.click_register_button()
        assert self.login_page_obj.is_registration_successful()