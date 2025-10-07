"""Locators for Login page elements."""
from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Page elements for user authentication flow."""

    # Login form
    USERNAME_FIELD = (By.XPATH, "//input[@name='email']")  # Actually used for username
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")

    # Post-login elements
    TITLE_RECIPES = (By.XPATH, "//h1[contains(text(),'Рецепты')]")
    EXIT_BUTTON = (By.XPATH, "//a[contains(text(),'Выход')]")

    # Elements that appear on login page but belong to other flows
    USER_NAME_FIELD = (By.XPATH, "//input[@name='username']")
    CREATE_ACCOUNT_LINK = (By.XPATH, "//a[contains(text(),'Создать аккаунт')]")
    REGISTRATION_HEADING = (By.XPATH, "//h1[contains(text(),'Регистрация')]")
    FIRST_NAME_FIELD = (By.XPATH, "//input[@name='first_name']")
    SECOND_NAME_FIELD = (By.XPATH, "//input[@name='last_name']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Создать аккаунт')]")
    CREATE_RECIPE_LINK = (By.XPATH, "//a[contains(text(),'Создать рецепт')]")
    SIGNIN_HEADING = (By.XPATH, "//h1[contains(text(),'Войти на сайт')]")

    # Legacy compatibility aliases
    EMAIL_FIELD = USERNAME_FIELD  # For backward compatibility
    ENTER_BUTTON = LOGIN_BUTTON   # For backward compatibility