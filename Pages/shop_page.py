import time

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
