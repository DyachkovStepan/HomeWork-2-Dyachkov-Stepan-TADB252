#https://ipython.readthedocs.io/en/stable/interactive/magics.html - magic command, создает файл в папке
import pytest
from classes import Ingredient, Recipe, ShoppingList

def test_ingredient_init():
    ingredient = Ingredient("Мука", 500, "г")
    assert ingredient.name == "Мука"
    assert ingredient.quantity == 500.0
    assert ingredient.unit == "г"

    with pytest.raises(ValueError):
        Ingredient("Мука", -50, "г")

    with pytest.raises(ValueError):
        ingredient.quantity = -100

def test_ingredient_str():
    ingredient1 = Ingredient("Мука", 500, "г")
    assert str(ingredient1) == "Мука: 500.0 г"

    ingredient2 = Ingredient("Молоко", 200, "г")
    assert str(ingredient2) == "Молоко: 200.0 г"

    ingredient3 = Ingredient("Яблоко", 1, "кг")
    assert str(ingredient3) == "Яблоко: 1.0 кг"


def test_ingredient_eq():
    ingredient1 = Ingredient("Мука", 500, "г")
    ingredient2 = Ingredient("Мука", 499, "г")
    assert ingredient1 == ingredient2

    ingredient3 = Ingredient("Молоко", 500, "г")
    assert ingredient1 != ingredient3

    ingredient4 = Ingredient("Мука", 500, "кг")
    assert ingredient1 != ingredient4
#https://ipython.readthedocs.io/en/stable/interactive/magics.html - атрибут а указывает на добавление в конец файла

def test_recipe_init():
    ingredient1 = Ingredient("Мука", 500, "г")
    ingredient2 = Ingredient("Молоко", 200, "г")
    recipe = Recipe("Торт", [ingredient1, ingredient2])
    assert recipe.title == "Торт"
    assert recipe.ingredients == [ingredient1, ingredient2]

def test_add_ingredient_add_new():
    ingredient1 = Ingredient("Мука", 500, "г")
    ingredient2 = Ingredient("Молоко", 200, "г")
    recipe = Recipe("Торт", [ingredient1])
    recipe.add_ingredient(ingredient2)
    assert recipe.ingredients == [ingredient1, ingredient2]
    assert len(recipe.ingredients) == 2

def test_add_ingredient_add_old():
    ingredient1 = Ingredient("Мука", 500, "г")
    ingredient2 = Ingredient("Мука", 100, "г")
    recipe = Recipe("Торт", [ingredient1])
    recipe.add_ingredient(ingredient2)
    assert recipe.ingredients[0].quantity == 600.0
    assert len(recipe.ingredients) == 1 

def test_add_ingredient_scale():
    ingredient1 = Ingredient("Мука", 500, "г")
    ingredient2 = Ingredient("Молоко", 200, "г")
    recipe1 = Recipe("Торт", [ingredient1, ingredient2])
    ratio = 2
    recipe2 = recipe1.scale(ratio)
    assert isinstance(recipe2, Recipe)
    assert recipe1.ingredients[0].quantity == 500.0  
    assert recipe1.ingredients[1].quantity == 200.0
    assert recipe2.ingredients[0].quantity == 1000.0
    assert recipe2.ingredients[1].quantity == 400.0
    with pytest.raises(ValueError):
        recipe1.scale(-2)

def test_recipe_len():
    ingredient1 = Ingredient("Мука", 500, "г")
    ingredient2 = Ingredient("Молоко", 200, "г")
    recipe1 = Recipe("Торт", [ingredient1, ingredient2])
    assert len(recipe1) == 2
    recipe1.add_ingredient(Ingredient("Мука", 200, "г"))
    assert len(recipe1) == 2
    recipe1.add_ingredient(Ingredient("Соль", 10, "г"))
    assert len(recipe1) == 3
#https://ipython.readthedocs.io/en/stable/interactive/magics.html - атрибут а указывает на добавление в конец файла

def test_add_recipe():

    recipe = Recipe("Торт", [Ingredient("Мука", 500, "г")])
    shop_list = ShoppingList()
    shop_list.add_recipe(recipe, 2)
    assert len(shop_list._items) == 1
    assert shop_list._items[0][0].quantity == 1000.0
    assert shop_list._items[0][1] == "Торт"
    with pytest.raises(ValueError):
        shop_list.add_recipe(recipe, 0)

def test_remove_recept():
    recipe1 = Recipe("Торт", [Ingredient("Мука", 500, "г"), Ingredient("Молоко", 200, "г")])
    recipe2 = Recipe("Кекс", [Ingredient("Мука", 300, "г")])
    shop_list = ShoppingList()
    shop_list.add_recipe(recipe1, 2)
    shop_list.add_recipe(recipe2, 1)
    shop_list.remove_recipe("Торт")
    assert len(shop_list._items) == 1 
    assert shop_list._items[0][1] == "Кекс"
    shop_list.remove_recipe("Спартак Champion")
    assert len(shop_list._items) == 1

def test_get_list():
    recipe1 = Recipe("Торт", [Ingredient("Мука", 500, "г"),Ingredient("Молоко", 200, "г")])
    recipe2 = Recipe("Кекс", [Ingredient("Мука", 300, "г"), Ingredient("Изюм", 50, "г")])
    shop_list = ShoppingList()
    shop_list.add_recipe(recipe1, 2)
    shop_list.add_recipe(recipe2, 1)
    final_ingredients = shop_list.get_list()
    assert len(final_ingredients) == 3
    assert final_ingredients[0].name == "Изюм"
    assert final_ingredients[2].name == "Мука"
    assert final_ingredients[0].quantity == 50.0
    assert final_ingredients[2].quantity == 1300.0

def test_shop_list_add():
    recipe1 = Recipe("Торт", [Ingredient("Мука", 500, "г"), Ingredient("Молоко", 200, "г")])
    recipe2 = Recipe("Кекс", [Ingredient("Изюм", 50, "г"), Ingredient("Мука", 300, "г")])
    list1 = ShoppingList()
    list1.add_recipe(recipe1, 1)
    list2 = ShoppingList()
    list2.add_recipe(recipe2, 1)
    combined_list = list1 + list2
    assert isinstance(combined_list, ShoppingList)
    assert len(combined_list._items) == 4
    assert len(list1._items) == 2
    assert len(list2._items) == 2

