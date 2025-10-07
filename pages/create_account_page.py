"""Create account page object with user registration functionality."""
import allure
from pages.base_page import BasePage
from locators.create_account_page_locators import CreateAccountPageLocators
from test_config import LOGIN_PAGE_URL


class CreateAccountPage(BasePage):
    """Page object for user registration functionality."""

    @allure.step("Navigate to registration page")
    def go_to_create_account_page(self):
        """Navigate to registration page from login page."""
        self.go_to_url(LOGIN_PAGE_URL)
        self.click_to_element(CreateAccountPageLocators.CREATE_ACCOUNT_LINK)
        self.find_element_with_wait(CreateAccountPageLocators.REGISTRATION_HEADING)

    @allure.step("Fill registration form and submit")
    def fill_in_registration_fields(self, first_name, second_name, user_name, email, password):
        """Fill all registration fields and submit the form."""
        self.add_text_to_element(CreateAccountPageLocators.FIRST_NAME_FIELD, first_name)
        self.add_text_to_element(CreateAccountPageLocators.SECOND_NAME_FIELD, second_name)
        self.add_text_to_element(CreateAccountPageLocators.USER_NAME_FIELD, user_name)
        self.add_text_to_element(CreateAccountPageLocators.EMAIL_FIELD, email)
        self.add_text_to_element(CreateAccountPageLocators.PASSWORD_FIELD, password)
        self.click_to_element(CreateAccountPageLocators.CREATE_ACCOUNT_BUTTON)
        self.find_element_with_wait(CreateAccountPageLocators.SIGNIN_HEADING)

    @allure.step("Get URL after account creation")
    def url_after_push_create_account(self):
        """Get current URL after successful account creation."""
        self.find_element_with_wait(CreateAccountPageLocators.SIGNIN_HEADING)
        return self.get_current_url()

    @allure.step("Check login form visibility")
    def check_visibility_autorisation_form(self):
        """Check if login form elements are visible after account creation."""
        self.find_element_with_wait(CreateAccountPageLocators.EMAIL_FIELD)
        return (self.check_displaying_of_element(CreateAccountPageLocators.EMAIL_FIELD) and
                self.check_displaying_of_element(CreateAccountPageLocators.PASSWORD_FIELD))