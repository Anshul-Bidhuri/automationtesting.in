import random

from Helpers import driver_helpers, locators
from Pages.base_page import BasePage

from Helpers import customLogger, constants

log = customLogger.get_logger()


class CartPage(BasePage):

    def get_item_details_on_cart_page(self):
        num_of_items = driver_helpers.find_elements(self.driver, locators.button_remove_item_from_cart)
        log.info(f"Found {len(num_of_items)} items in the cart")
        item_dicts = {}
        for item in range(1, len(num_of_items) + 1):
            item_name = driver_helpers.get_text(self.driver, locators.product_name_on_cart_page.format(item_num=item))
            item_price = driver_helpers.get_text(self.driver, locators.product_price_on_cart_page.format(item_num=item))
            item_quantity = driver_helpers.get_attribute(self.driver, locators.product_quantity_on_cart_page.format(item_num=item), "value")
            item_dicts[item] = {"name": item_name, "price": int(float(item_price.replace('₹', '').replace(',', '').strip())), "quantity": int(item_quantity)}
        log.info(f"Item details: {item_dicts}")
        return item_dicts

    def update_dict_quantity_values(self, item_details_on_cart_page):
        keys = list(item_details_on_cart_page.keys())
        zero_quantity_key = random.choice(keys)
        item_details_on_cart_page[zero_quantity_key]['quantity'] = 0
        for key in keys:
            if key != zero_quantity_key:
                item_details_on_cart_page[key]['quantity'] += random.randint(1, 10)
        log.info(f"Updated item details: {item_details_on_cart_page}")
        return item_details_on_cart_page

    def update_quantity_as_per_updated_item_dict(self, updated_item_quantity):
        for key, value in updated_item_quantity.items():
            driver_helpers.send_keystrokes(self.driver, locators.input_field_update_product_quantity.format(product_name=value["name"]), value["quantity"])
        driver_helpers.click_element(self.driver, locators.button_update_basket)
        driver_helpers.wait_till_element_is_visible(self.driver, locators.cart_updated_message, timeout=30)