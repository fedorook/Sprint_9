"""Create recipe page object with recipe creation functionality."""
from pathlib import Path
import allure
from pages.base_page import BasePage
from locators.create_recipe_page_locators import CreateRecipePageLocators


class CreateRecipePage(BasePage):
    """Page object for recipe creation functionality."""

    DEFAULT_IMAGE_FILE = 'image.jpg'
    INGREDIENT_SEARCH_TERM = 'к'  # Search term for ingredient autocomplete

    @allure.step("Upload recipe image")
    def upload_file(self, file_name=None):
        """Upload an image file for the recipe."""
        if file_name is None:
            file_name = self.DEFAULT_IMAGE_FILE

        # Get current file directory (project root)
        project_dir = Path(__file__).parent.parent

        # Form path to file in assets folder
        file_path = project_dir / 'assets' / file_name

        # Get absolute path (needed for send_keys)
        absolute_path = str(file_path.resolve())

        # Find input for file upload
        file_input = self.check_element_is_located(CreateRecipePageLocators.IMAGE_LOCATOR)

        # Pass file path
        file_input.send_keys(absolute_path)

    @allure.step("Fill recipe form and submit")
    def create_recipe(self, recipe_name, grams, time_cooking, description):
        """Fill complete recipe form and submit it."""
        self.click_to_element(CreateRecipePageLocators.CREATE_RECIPE_LINK)
        self.add_text_to_element(CreateRecipePageLocators.RECIPE_NAME_FIELD, recipe_name)

        # Add ingredient through autocomplete
        self.add_text_to_element(CreateRecipePageLocators.INGREDIENT_NAME_FIELD, self.INGREDIENT_SEARCH_TERM)
        self.click_to_element(CreateRecipePageLocators.INGREDIENT)
        self.add_text_to_element(CreateRecipePageLocators.INGREDIENT_AMOUNT_FIELD, grams)
        self.click_to_element(CreateRecipePageLocators.ADD_INGREDIENT)

        # Fill remaining fields
        self.add_text_to_element(CreateRecipePageLocators.COOKING_TIME_FIELD, time_cooking)
        self.add_text_to_element(CreateRecipePageLocators.DESCRIPTION_FIELD, description)
        self.upload_file()
        self.click_to_element(CreateRecipePageLocators.CREATE_RECIPE_BUTTON)

        return recipe_name

    @allure.step("Check recipe card visibility")
    def check_visibility_of_recipe_card(self):
        """Check if the created recipe card is visible."""
        self.find_element_with_wait(CreateRecipePageLocators.RECIPE_CARD)
        return self.check_displaying_of_element(CreateRecipePageLocators.RECIPE_CARD)

    @allure.step("Check recipe name visibility")
    def check_visibility_recipe_name(self, recipe_name):
        """Check if the recipe name is visible on the created recipe page."""
        recipe_name_locator = (
            CreateRecipePageLocators.RECIPE_NAME_HEADER[0],
            CreateRecipePageLocators.RECIPE_NAME_HEADER[1].format(recipe_name=recipe_name)
        )
        self.find_element_with_wait(CreateRecipePageLocators.EDIT_RECIPE)
        return self.check_displaying_of_element(recipe_name_locator)