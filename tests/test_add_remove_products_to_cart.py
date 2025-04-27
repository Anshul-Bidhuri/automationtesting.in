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
        return {"all_items": {}, "selected_items": {}}

    @pytest.mark.positive_cases
    def test_delete_already_added_items_from_cart(self, shop_item_details):
        self.shop_page_obj.make_cart_empty()

    @pytest.mark.positive_cases
    def test_get_items_from_shop_page(self, shop_item_details):
        item_details = self.shop_page_obj.get_all_item_details()
        assert len(item_details) > 0
        shop_item_details["all_items"] = item_details

    @pytest.mark.positive_cases
    def test_random_items_from_shop_page_to_cart(self, shop_item_details):
        random_item_numbers_that_going_to_be_add = random.randint(1, len(shop_item_details["all_items"]))
        random_item_choices = random.choices(list(shop_item_details["all_items"].items()), k=random_item_numbers_that_going_to_be_add)
        self.shop_page_obj.add_random_items_to_cart(random_item_choices)
        shop_item_details["selected_items"] = random_item_choices

    @pytest.mark.positive_cases
    def test_number_of_items_in_cart(self, shop_item_details):
        expected_number_of_items = len(shop_item_details["selected_items"])
        actual_number_of_items = self.shop_page_obj.get_number_of_items_in_cart()
        assert expected_number_of_items == actual_number_of_items

    @pytest.mark.positive_cases
    def test_total_amount_of_cart(self, shop_item_details):
        expected_amount = self.shop_page_obj.calculate_expected_cart_amount(shop_item_details["selected_items"])
        actual_amount = self.shop_page_obj.get_total_amount_of_cart()
        assert expected_amount == actual_amount