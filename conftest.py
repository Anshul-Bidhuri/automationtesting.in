import pytest

from Helpers import constants, driver_helpers, locators


@pytest.fixture(scope="class")
def setup_browser_login_page(request):
    driver = driver_helpers.get_chrome_driver()
    driver.get(constants.LOGIN_PAGE_URL)
    request.cls.driver = driver
    yield driver
    driver.close()


@pytest.fixture(scope="class")
def setup_browser_address_page(request):
    driver = driver_helpers.get_chrome_driver()
    driver.get(constants.LOGIN_PAGE_URL)
    driver_helpers.type_text(driver, locators.input_field_login_username, constants.ALREADY_REGISTERED_EMAIL)
    driver_helpers.type_text(driver, locators.input_field_login_password, constants.ALREADY_REGISTERED_PASSWORD)
    driver_helpers.click_element(driver, locators.button_login)
    driver_helpers.wait_till_element_is_clickable(driver, locators.button_sign_out, timeout=10)
    driver.get(constants.ADDRESS_PAGE_URL)
    yield driver
    driver.close()