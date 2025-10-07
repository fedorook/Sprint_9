"""Locators for Create Recipe page elements."""
from selenium.webdriver.common.by import By


class CreateRecipePageLocators:
    """Page elements for recipe creation flow."""

    # Navigation
    CREATE_RECIPE_LINK = (By.XPATH, "//a[contains(text(),'Создать рецепт')]")

    # Recipe form fields
    RECIPE_NAME_FIELD = (By.XPATH, "//div[contains(text(), 'Название рецепта')]/following::input[@type='text']")
    COOKING_TIME_FIELD = (By.XPATH, "//div[contains(text(), 'Время приготовления')]/following::input[@type='text']")
    DESCRIPTION_FIELD = (By.XPATH, "//div[contains(text(), 'Описание рецепта')]/following::textarea[1]")
    IMAGE_LOCATOR = (By.CSS_SELECTOR, "input[type='file']")

    # Ingredients section
    INGREDIENT_NAME_FIELD = (By.XPATH, "//div[contains(text(), 'Ингредиенты')]/following::input[@type='text']")
    INGREDIENT_AMOUNT_FIELD = (By.XPATH, "//input[@class='styles_inputField__3eqTj styles_ingredientsAmountValue__2matT']")
    INGREDIENT = (By.XPATH, "//div[contains(@class, 'styles_container__3ukwm')]//div[text()='кабачки']")
    ADD_INGREDIENT = (By.XPATH, "//div[contains(text(),'Добавить ингредиент')]")

    # Actions
    CREATE_RECIPE_BUTTON = (By.XPATH, "//button[contains(text(),'Создать рецепт')]")

    # Recipe display
    RECIPE_CARD = (By.XPATH, "//div[@class='styles_single-card__1yTTj']")
    RECIPE_NAME_HEADER = (By.XPATH, "//h1[contains(text(), '{recipe_name}')]")
    EDIT_RECIPE = (By.XPATH, "//a[contains(text(),'Редактировать рецепт')]")