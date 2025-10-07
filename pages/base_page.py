"""Base page class with common Selenium operations."""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    """Base class for all page objects with common web element operations."""

    DEFAULT_TIMEOUT = 10
    LONG_TIMEOUT = 20

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.DEFAULT_TIMEOUT)

    @allure.step("Navigate to URL")
    def go_to_url(self, url):
        """Navigate to specified URL."""
        self.driver.get(url)

    @allure.step("Find element")
    def find_element_with_wait(self, locator):
        """Find element with explicit wait for visibility."""
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Check element clickability")
    def check_element_is_clickable(self, locator):
        """Wait for element to be clickable."""
        return WebDriverWait(self.driver, self.LONG_TIMEOUT).until(EC.element_to_be_clickable(locator))

    @allure.step("Click on element")
    def click_to_element(self, locator):
        """Click on element after waiting for it to be visible."""
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step("Check element visibility")
    def check_displaying_of_element(self, locator):
        """Check if element is displayed."""
        return self.driver.find_element(*locator).is_displayed()

    @allure.step("Check element invisibility")
    def check_invisibility_of_element(self, locator):
        """Wait for element to become invisible."""
        return WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(EC.invisibility_of_element_located(locator))

    @allure.step("Check text presence in element")
    def check_text_to_be_present_in_element(self, locator, text):
        """Wait for specific text to appear in element."""
        return WebDriverWait(self.driver, self.LONG_TIMEOUT).until(EC.text_to_be_present_in_element(locator, text))

    @allure.step("Add text to element")
    def add_text_to_element(self, locator, text):
        """Add text to element after waiting for it to be visible."""
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    @allure.step("Get element text")
    def get_text_from_element(self, locator):
        """Get text from element."""
        return self.find_element_with_wait(locator).text

    @allure.step("Scroll to element")
    def scroll_to_element(self, locator):
        """Scroll element into view."""
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Get current URL")
    def get_current_url(self):
        """Get current page URL."""
        return self.driver.current_url

    @allure.step("Wait for element to appear")
    def check_element_is_located(self, locator):
        """Wait for element to be present in DOM."""
        return WebDriverWait(self.driver, self.LONG_TIMEOUT).until(EC.presence_of_element_located(locator))