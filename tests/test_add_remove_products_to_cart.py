import pytest
import random

from Helpers import constants
from Pages.shop_page import ShopPage
from Pages.cart_page import CartPage


@pytest.mark.run(order=3)
@pytest.mark.shop_page
class TestShopPage:

    @pytest.fixture(scope="class", autouse=True)
    def initiate_driver(self, setup_browser_shop_page, request):
        request.cls.shop_page_obj = ShopPage(self.driver)
        request.cls.cart_page_obj = CartPage(self.driver)

    @pytest.fixture(scope="module")
    def shop_item_details(self):
        return {"all_items": {}, "selected_items_on_shop_page": {}, "total_amount": 0, "item_details_on_cart_page": {}}

    @pytest.fixture(scope="function")
    def navigate_to_cart_page(self):
        self.shop_page_obj.open_page(constants.CART_PAGE_URL)

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
        shop_item_details["selected_items_on_shop_page"] = random_item_choices

    @pytest.mark.positive_cases
    def test_number_of_items_in_cart(self, shop_item_details):
        expected_number_of_items = len(shop_item_details["selected_items_on_shop_page"])
        actual_number_of_items = self.shop_page_obj.get_number_of_items_in_cart()
        assert expected_number_of_items == actual_number_of_items

    @pytest.mark.positive_cases
    def test_total_amount_of_cart(self, shop_item_details):
        expected_amount = self.shop_page_obj.calculate_expected_cart_amount(shop_item_details["selected_items_on_shop_page"])
        shop_item_details["total_amount"] = expected_amount
        actual_amount = self.shop_page_obj.get_total_amount_of_cart()
        assert expected_amount == actual_amount

    def test_page_reload_is_not_resetting_the_cart(self, shop_item_details):
        self.shop_page_obj.reload_page()
        expected_number_of_items = len(shop_item_details["selected_items_on_shop_page"])
        actual_number_of_items = self.shop_page_obj.get_number_of_items_in_cart()
        assert expected_number_of_items == actual_number_of_items

    def test_items_quantity_matching_with_total_on_cart_page(self, shop_item_details, navigate_to_cart_page):
        item_details_on_cart_page = self.cart_page_obj.get_item_details_on_cart_page()
        shop_item_details["item_details_on_cart_page"] = item_details_on_cart_page
        total_quantity = sum((item[1]['quantity']) for item in item_details_on_cart_page.items())
        assert total_quantity == len(shop_item_details["selected_items_on_shop_page"])

    def test_items_price_matching_with_total_on_cart_page(self, shop_item_details, navigate_to_cart_page):
        total_amount_on_cart = sum((item[1]['price']) for item in shop_item_details["item_details_on_cart_page"].items())
        assert total_amount_on_cart == shop_item_details["total_amount"]

    def test_items_name_matching_with_total_on_cart_page(self, shop_item_details, navigate_to_cart_page):
        item_names_on_cart_page = [item['name'] for item in shop_item_details["item_details_on_cart_page"].values()]
        selected_item_names_from_shop_page = [item[1]['name'] for item in shop_item_details["selected_items_on_shop_page"]]
        assert sorted(item_names_on_cart_page) == sorted(selected_item_names_from_shop_page)

    def test_update_items_quantity_in_cart(self, shop_item_details, navigate_to_cart_page):
        updated_item_quantity = self.cart_page_obj.update_dict_quantity_values(shop_item_details["item_details_on_cart_page"])
        self.cart_page_obj.update_quantity_as_per_updated_item_dict(updated_item_quantity)