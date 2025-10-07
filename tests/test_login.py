"""Tests for user authentication functionality."""
import allure
from test_config import URL_AFTER_LOGIN


@allure.feature("User Authentication")
class TestLogin:
    """Test suite for user login flow."""

    def _perform_login(self, login_page, create_account):
        """Helper method to perform user login."""
        email, password = create_account
        login_page.go_to_login_page()
        login_page.fill_email_and_password(email, password)

    @allure.story("Navigation after login")
    @allure.title("Verify redirect to main page after login")
    def test_check_transition_to_main_page_after_login(self, login_page, create_account):
        """Test that user is redirected to main page after successful login."""
        self._perform_login(login_page, create_account)

        actual_url = login_page.get_current_url_after_enter()
        assert actual_url == URL_AFTER_LOGIN, f"Expected {URL_AFTER_LOGIN}, got {actual_url}"

    @allure.story("UI validation after login")
    @allure.title("Verify exit button visibility after login")
    def test_check_visibility_exit_button_after_login(self, login_page, create_account):
        """Test that exit button is visible after successful login."""
        self._perform_login(login_page, create_account)

        is_exit_button_visible = login_page.check_visibility_exit_button()
        assert is_exit_button_visible, "Exit button should be visible after login"