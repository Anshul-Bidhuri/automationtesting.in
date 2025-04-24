import pytest

from Pages.login_register_page import LoginPage


class TestLoginRegisterPage:

    @pytest.fixture(scope="class", autouse=True)
    def initiate_driver(self, setup_browser_login_screen, request):
        request.cls.login_page_obj = LoginPage(self.driver)

    def test_login_with_invalid_username(self):
        self.login_page_obj.enter_login_username("testing1")
        self.login_page_obj.enter_login_password("testing1")
        self.login_page_obj.click_login_button()
        assert self.login_page_obj.is_error_message_displayed()