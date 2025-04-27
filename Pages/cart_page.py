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