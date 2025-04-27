import pytest
import random

from Helpers import constants
from Pages.shop_page import ShopPage


@pytest.mark.run(order=3)
@pytest.mark.shop_page
class TestShopPage:

    @pytest.fixture(scope="class", autouse=True)
    def initiate_driver(self, setup_browser_shop_page, request):
        request.cls.shop_page_obj = ShopPage(self.driver)

    @pytest.fixture(scope="module")
    def shop_item_details(self):
        return {}

    @pytest.mark.positive_cases
    def test_get_items_from_shop_page(self, shop_item_details):
        item_details = self.shop_page_obj.get_all_item_details()
        assert len(item_details) > 0
        shop_item_details.update(item_details)
        print(23324234)
