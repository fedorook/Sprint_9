"""Tests for recipe creation functionality."""
import allure


@allure.feature("Recipe Management")
class TestCreateRecipe:
    """Test suite for recipe creation flow."""

    def _create_recipe(self, create_recipe_page, generate_recipe_data):
        """Helper method to create recipe with generated data."""
        recipe_name, grams, time_cooking, description = generate_recipe_data
        return create_recipe_page.create_recipe(recipe_name, grams, time_cooking, description)

    @allure.story("Recipe creation validation")
    @allure.title("Verify recipe card visibility after creation")
    def test_check_visibility_created_recipe(self, login_user, create_recipe_page, generate_recipe_data):
        """Test that recipe card is visible after successful creation."""
        self._create_recipe(create_recipe_page, generate_recipe_data)

        is_recipe_card_visible = create_recipe_page.check_visibility_of_recipe_card()
        assert is_recipe_card_visible, "Recipe card should be visible after creation"

    @allure.story("Recipe creation validation")
    @allure.title("Verify recipe name visibility after creation")
    def test_check_visibility_recipe_name(self, login_user, create_recipe_page, generate_recipe_data):
        """Test that recipe name is visible on the created recipe page."""
        recipe_name = self._create_recipe(create_recipe_page, generate_recipe_data)

        is_recipe_name_visible = create_recipe_page.check_visibility_recipe_name(recipe_name)
        assert is_recipe_name_visible, f"Recipe name '{recipe_name}' should be visible after creation"

