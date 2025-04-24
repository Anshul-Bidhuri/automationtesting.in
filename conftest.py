import pytest

from Helpers import constants, driver_helpers


@pytest.fixture(scope="class")
def setup_browser_login_screen(request):
    driver = driver_helpers.get_chrome_driver()
    driver.get(constants.LOGIN_PAGE_URL)
    request.cls.driver = driver
    yield driver
    driver.close()