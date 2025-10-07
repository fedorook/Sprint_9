"""Locators for Create Account page elements."""
from selenium.webdriver.common.by import By


class CreateAccountPageLocators:
    """Page elements for user registration flow."""

    # Navigation and titles
    CREATE_ACCOUNT_LINK = (By.XPATH, "//a[contains(text(),'Создать аккаунт')]")
    REGISTRATION_HEADING = (By.XPATH, "//h1[contains(text(),'Регистрация')]")
    SIGNIN_HEADING = (By.XPATH, "//h1[contains(text(),'Войти на сайт')]")

    # Form fields
    FIRST_NAME_FIELD = (By.XPATH, "//input[@name='first_name']")
    SECOND_NAME_FIELD = (By.XPATH, "//input[@name='last_name']")
    USER_NAME_FIELD = (By.XPATH, "//input[@name='username']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")

    # Actions
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Создать аккаунт')]")