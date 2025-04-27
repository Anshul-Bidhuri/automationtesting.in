import random

from Helpers import driver_helpers, locators
from Pages.base_page import BasePage

from Helpers import customLogger, constants

log = customLogger.get_logger()


class ShopPage(BasePage):

    def get_all_item_details(self):
        item_dict = {}
        items_in_shop = driver_helpers.find_elements(self.driver, locators.items_in_shop)
        log.info(f"Found {len(items_in_shop)} items in the shop")
        for item in range(1, len(items_in_shop) + 1):
            item_name = driver_helpers.get_text(self.driver, locators.item_names.format(item_num=item))
            item_price = driver_helpers.get_text(self.driver, locators.item_prices.format(item_num=item))
            item_dict[item] = {"name": item_name, "price": int(float(item_price.replace('₹', '').replace(',', '').strip()))}
        log.info(f"Item details: {item_dict}")
        return item_dict

    def add_random_items_to_cart(self, all_item_details):
        log.info(f"Adding randomly {len(all_item_details)} items to cart")
        count = 1
        for key, value in all_item_details:
            log.info(f"Adding item number {key} to cart")
            log.info(f"item name is: {value['name']} and price: {value['price']}")
            driver_helpers.click_element(self.driver, locators.button_add_to_cart.format(item_num=key))
            log.info(f"Added {value['name']} to cart")
            driver_helpers.wait_till_element_is_visible(self.driver, locators.current_cart_count.format(item_num=count), timeout=10)
            count += 1

    def get_number_of_items_in_cart(self):
        num_of_items_in_cart = int(driver_helpers.get_text(self.driver, locators.number_of_items_in_cart).replace(" Items", ""))
        log.info(f"Number of items in cart: {num_of_items_in_cart}")
        return num_of_items_in_cart

    def calculate_expected_cart_amount(self, all_item_details):
        total_expected_price = sum((item[1]['price']) for item in all_item_details)
        log.info(f"Expected cart amount: {total_expected_price}")
        return total_expected_price

    def get_total_amount_of_cart(self):
        total_amount_of_cart = int(float(driver_helpers.get_text(self.driver, locators.cart_amount).replace("₹", "").replace(",", "")))
        log.info(f"Total amount of cart: {total_amount_of_cart}")
        return total_amount_of_cart