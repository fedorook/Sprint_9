"""
Test configuration and shared fixtures for the Sprint 9 test suite.

This module provides pytest fixtures for browser setup, page objects,
and test data generation for automated testing.
"""
import pytest
import random
from selenium import webdriver
from pages.create_account_page import CreateAccountPage
from pages.login_page import LoginPage
from pages.create_recipe_page import CreateRecipePage
from test_config import LOGIN_PAGE_URL, username, password
from helper.randomizer import generate_random_string


# Constants for test data generation
USER_NAME_LENGTH = 10
RECIPE_NAME_LENGTH = 8
DESCRIPTION_LENGTH = 20
MIN_AMOUNT = 1
MAX_AMOUNT = 100


def get_default_chrome_options():
    """Configure Chrome options for Selenoid browser sessions."""
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    return options


@pytest.fixture
def driver():
    """Create and configure WebDriver instance with teardown."""
    import os
    selenoid_uri = os.getenv('SELENOID_URI', 'http://selenoid:4444/wd/hub')
    options = get_default_chrome_options()
    driver = webdriver.Remote(command_executor=selenoid_uri, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def create_account_page(driver):
    """Create account page object instance."""
    return CreateAccountPage(driver)


@pytest.fixture
def login_page(driver):
    """Login page object instance."""
    return LoginPage(driver)


@pytest.fixture
def create_recipe_page(driver):
    """Create recipe page object instance."""
    return CreateRecipePage(driver)


@pytest.fixture
def generate_user_data():
    """Generate random user registration data."""
    first_name = generate_random_string(USER_NAME_LENGTH)
    second_name = generate_random_string(USER_NAME_LENGTH)
    email = generate_random_string(USER_NAME_LENGTH) + "@mail.ru"
    user_name = email  # Make username same as email for compatibility
    password = generate_random_string(USER_NAME_LENGTH)
    return first_name, second_name, user_name, email, password


@pytest.fixture
def create_account(create_account_page, generate_user_data):
    """Create a new user account and return credentials."""
    first_name, second_name, user_name, email, password = generate_user_data
    create_account_page.go_to_create_account_page()
    create_account_page.fill_in_registration_fields(first_name, second_name, user_name, email, password)
    return email, password


@pytest.fixture
def login_user(login_page):
    """Login with predefined user credentials."""
    login_page.go_to_login_page()
    login_page.fill_email_and_password(username, password)


@pytest.fixture
def generate_recipe_data():
    """Generate random recipe data for testing."""
    recipe_name = generate_random_string(RECIPE_NAME_LENGTH)
    grams = random.randint(MIN_AMOUNT, MAX_AMOUNT)
    time_cooking = random.randint(MIN_AMOUNT, MAX_AMOUNT)
    description = generate_random_string(DESCRIPTION_LENGTH)
    return recipe_name, grams, time_cooking, description
