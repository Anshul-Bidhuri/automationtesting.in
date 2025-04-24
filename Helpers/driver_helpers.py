"""Browser based functions via Selenium WebDriver"""
import time
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from Helpers import customLogger

log = customLogger.get_logger()


def type_text(driver, locator=None, text=None, element=None):
    log.info(f"typing {text} inside the locator {locator}")
    sleep(1)
    element = get_element(driver, locator) if not element else element
    move_to_element(driver, element)
    element.clear()
    sleep(1)
    return element.send_keys(text)


def click_enter(element):
    element.send_keys(Keys.ENTER)


def wait_till_element_is_present(driver, locator, timeout=30):
    log.info(f"waiting for locator {locator} to be present")
    element = WebDriverWait(driver, timeout=timeout).until(
        expected_conditions.presence_of_element_located((By.XPATH, locator)))
    log.info(f"locator {locator} present")
    return element


def wait_until_element_not_visible(driver, locator, timeout=30):
    log.info(f"waiting for locator {locator} to be invisible")
    wait = WebDriverWait(driver, timeout)
    element = wait.until(expected_conditions.invisibility_of_element_located(locator))
    log.info(f"locator {locator} to be vanished")


def wait_till_element_is_visible(driver, locator, timeout=60):
    log.info(f"waiting for locator {locator} to be visible")
    element = WebDriverWait(driver, timeout=timeout).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locator)))
    log.info(f"locator {locator} visible")
    return element


def wait_till_element_disappears(driver, locator):
    log.info(f"waiting for locator {locator} to disappears")
    element = WebDriverWait(driver, timeout=30).until(
        expected_conditions.invisibility_of_element_located((By.XPATH, locator)))
    return element


def upload_file_to_input_field(driver, locator, file_path):
    try:
        log.info(f"uploading file {file_path} to locator {locator}")
        get_element(driver, locator).send_keys(file_path)
    except:
        log.error("ERROR: unable to upload file")


def wait_till_element_is_clickable(driver, locator, timeout=30):
    log.info(f"waiting for locator {locator} to be clickable")
    try:
        WebDriverWait(driver, timeout=timeout).until(expected_conditions.element_to_be_clickable((By.XPATH, locator)))
        log.info(f"locator {locator} clickable")
        return True
    except:
        return False


def send_keystrokes(driver, locator, text):
    element = get_element(driver, locator)
    element.clear()
    for character in text:
        element.send_keys(character)
        sleep(0.15)


def is_displayed(driver, locator, timeout=10):
    try:
        return get_element(driver, locator, timeout).is_displayed()
    except StaleElementReferenceException:
        return driver.find_element(By.XPATH, locator).is_displayed()
    except TimeoutException:
        return False


def is_enabled(driver, locator, timeout=10):
    try:
        get_element(driver, locator, timeout).is_enabled()
    except TimeoutException:
        return False
    return True


def is_text_present(driver, text):
    return text in driver.page_source


def refresh_page(driver):
    driver.refresh()


def get_element(driver, locator, timeout=30):
    try:
        return WebDriverWait(driver, timeout).until(
            expected_conditions.presence_of_element_located((By.XPATH, locator)))
    except NoSuchElementException:
        log.error(f"ERROR: Element present on locator '{locator}' not found")


def load_time(driver, timeout):
    return driver.set_page_load_timeout(timeout)


def click_element(driver, locator, timeout=30):
    wait_till_element_is_clickable(driver, locator, timeout)
    element = get_element(driver, locator, timeout)
    move_to_element(driver, element)
    log.info(f"clicking on locator {locator}")
    try:
        return element.click()
    except Exception as e:
        log.error(f"ERROR: unable to click {locator} with selenium click " + str(e))
        element = get_element(driver, locator, timeout)
        return driver.execute_script("arguments[0].click();", element)


def main_window(driver):
    log.info(f"switching to the main window")
    driver.close()
    handles = driver.window_handles
    driver.switch_to.window(handles[0])


def switch_to_tab(driver, tab):
    log.info(f"switching to the tab no. {tab}")
    handles = driver.window_handles
    driver.switch_to.window(handles[tab])


def get_current_url(driver):
    return driver.current_url


def move_to_element(driver, element):
    actions = ActionChains(driver)
    sleep(1)
    actions.move_to_element(element).perform()


def accept_javascript_alert(driver):
    time.sleep(2)
    alert = driver.switch_to.alert
    alert.accept()


def get_text(driver, locator, max_tries=3, timeout=10):
    tries = 0
    text = ""
    while not text and tries < max_tries:
        text = get_element(driver, locator, timeout=timeout).text
        if not text:
            sleep(0.3)
            tries += 1
    return text


def move_to_the_element_using_javascript(driver, locator=None, element=None):
    sleep(0.3)
    try:
        element = get_element(driver, locator) if not element else element
        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)
        sleep(0.5)
    except:
        pass


def get_value(driver, locator):
    return get_element(driver, locator).get_attribute("value")


def get_attribute(driver, locator, attribute, timeout=30):
    return get_element(driver, locator, timeout=timeout).get_attribute(attribute)


def explicit_wait(driver, expected_condition, timeout=20):
    return WebDriverWait(driver, timeout).until(expected_condition)


def select_by_value(driver, locator, value):
    element = get_element(driver, locator)
    select = Select(element)
    select.select_by_value(value)


def select_by_index(driver, locator, index):
    element = get_element(driver, locator)
    select = Select(element)
    select.select_by_index(index)


def select_by_visible_text(driver, locator, text):
    element = get_element(driver, locator)
    scroll_to_the_element(driver, locator)
    select = Select(element)
    select.select_by_visible_text(text)


def find_elements(driver, locator, locator_type=By.XPATH):
    return driver.find_elements(locator_type, value=locator)


def scroll_to_the_element(driver, locator):
    element = driver.find_element(By.XPATH, locator)
    driver.execute_script("arguments[0].scrollIntoView();", element)


def check_element_in_viewport(driver, locator):
    return driver.execute_script(
        "var element = arguments[0];" +
        "var rect = element.getBoundingClientRect();" +
        "return (rect.top >= 0 && rect.left >= 0 && "
        "(rect.bottom - rect.top) <= (window.innerHeight || document.documentElement.clientHeight) && "
        "(rect.right - rect.left) <= (window.innerWidth || document.documentElement.clientWidth));",
        get_element(driver, locator)
    )


def scroll_element_in_viewport(driver, locator):
    driver.execute_script("""
        var element = arguments[0];
        var rect = element.getBoundingClientRect();
        var topOffset = rect.top;
        var bottomOffset = rect.bottom;

        window.scrollBy(0, topOffset);

        var windowHeight = window.innerHeight || document.documentElement.clientHeight;
        if (bottomOffset > windowHeight) {
            window.scrollBy(0, bottomOffset - windowHeight);
        }
        """, get_element(driver, locator)
                          )


def scroll_to_bottom(driver):
    """Scrolls to the bottom of the page using JavaScript."""
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")


def get_chrome_driver():
    options = webdriver.ChromeOptions()
    options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    options.add_experimental_option("w3c", True)
    options.accept_untrusted_certs = True
    options.assume_untrusted_cert_issuer = True
    options.add_argument("--ignore-certificate-errors")
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--disk-cache-size=0")
    options.add_argument("--disable-cache")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd("Network.enable", {})
    log.info("New Chrome driver instance created")
    driver.maximize_window()
    return driver
