"""Tests for user account creation functionality."""
import allure
from test_config import LOGIN_PAGE_URL


@allure.feature("User Registration")
class TestCreateAccount:
    """Test suite for user account creation flow."""

    def _create_account(self, create_account_page, generate_user_data):
        """Helper method to create account with generated data."""
        first_name, second_name, user_name, email, password = generate_user_data
        create_account_page.go_to_create_account_page()
        create_account_page.fill_in_registration_fields(
            first_name, second_name, user_name, email, password
        )

    @allure.story("Navigation after registration")
    @allure.title("Verify redirect to login page after account creation")
    def test_check_transition_to_login_page_after_create_account(self, create_account_page, generate_user_data):
        """Test that user is redirected to login page after successful registration."""
        self._create_account(create_account_page, generate_user_data)

        actual_url = create_account_page.url_after_push_create_account()
        assert actual_url == LOGIN_PAGE_URL, f"Expected {LOGIN_PAGE_URL}, got {actual_url}"

    @allure.story("UI validation after registration")
    @allure.title("Verify login form visibility after account creation")
    def test_check_visibility_login_form_after_create_account(self, create_account_page, generate_user_data):
        """Test that login form elements are visible after successful registration."""
        self._create_account(create_account_page, generate_user_data)

        is_login_form_visible = create_account_page.check_visibility_autorisation_form()
        assert is_login_form_visible, "Login form should be visible after account creation"