import pytest

from Helpers import constants
from Pages.address_page import AddressPage
import utility


@pytest.mark.run(order=3)
@pytest.mark.login_user
class TestAddressPage:

    @pytest.fixture(scope="class", autouse=True)
    def initiate_driver(self, setup_browser_address_page, request):
        request.cls.address_page_obj = AddressPage(self.driver)

    def test_save_billing_address_with_empty_first_name_field(self):
        self.address_page_obj.enter_billing_address_first_name("")
