"""Login page object with authentication functionality."""
import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from test_config import LOGIN_PAGE_URL


class LoginPage(BasePage):
    """Page object for user login functionality."""

    @allure.step("Navigate to login page")
    def go_to_login_page(self):
        """Navigate to the login page."""
        self.go_to_url(LOGIN_PAGE_URL)

    @allure.step("Fill username and password")
    def fill_email_and_password(self, username, password):
        """Fill login credentials and submit the form."""
        self.add_text_to_element(LoginPageLocators.USERNAME_FIELD, username)
        self.add_text_to_element(LoginPageLocators.PASSWORD_FIELD, password)
        self.click_to_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Check transition to main page after login")
    def get_current_url_after_enter(self):
        """Verify successful login by checking recipes page and return current URL."""
        self.find_element_with_wait(LoginPageLocators.TITLE_RECIPES)
        return self.get_current_url()

    @allure.step("Check exit button visibility")
    def check_visibility_exit_button(self):
        """Check if the exit button is visible after login."""
        self.find_element_with_wait(LoginPageLocators.EXIT_BUTTON)
        return self.check_displaying_of_element(LoginPageLocators.EXIT_BUTTON)