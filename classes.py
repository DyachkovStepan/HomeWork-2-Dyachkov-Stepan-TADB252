# Ваш код здесь
class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit
    
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity):
        if new_quantity <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(new_quantity)

    def __str__(self):
        return f"{self.name}: {self._quantity} {self.unit}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self._quantity}, '{self.unit}')"
    
    def __eq__(self, other):
        return (other.name == self.name) and (other.unit == self.unit)

# Ваш код здесь
class Recipe:
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients

    def add_ingredient(self, ingredient):
        for i in self.ingredients:
            if  i.name == ingredient.name and i.unit == ingredient.unit:
                i.quantity += ingredient.quantity
                break
        else:
            self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if isinstance(ratio, (int,float)) and ratio > 0:
            return True
        return False
    
    def scale(self,ratio):
        ingredients = [Ingredient(ingredient.name, ingredient.quantity * ratio, ingredient.unit) for ingredient in self.ingredients]
        return Recipe(self.title, ingredients)
    
    def __len__(self):
        return len(self.ingredients)
    
    def __str__(self):
        ingredients_sup = "\n".join(str(ingredient) for ingredient in self.ingredients)
        return f"{self.title} состоит из ингредиентов: \n{ingredients_sup}"

# Ваш код здесь
class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients):
        super().__init__(title, ingredients)
        self.diet_type = diet_type
    
    def scale(self, ratio):
        new_recipe = super().scale(ratio)
        return DietaryRecipe(new_recipe.title, self.diet_type, new_recipe.ingredients)
    
    def __str__(self):
        old_str = super().__str__()
        return f"[{self.diet_type}] {old_str}"

# Ваш код здесь
class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe, portions):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        recipe = recipe.scale(portions)
        for ingredient in recipe.ingredients:
            self._items.append((ingredient, recipe.title))
    
    def remove_recipe(self, title):
        new_items = []
        for kortezh in self._items:
            if kortezh[1] != title:
                new_items.append(kortezh)
        self._items = new_items
    
    def get_list(self):
        ingredients = {}
        for kortezh in self._items:
            ingredient = kortezh[0]
            ingr_name, ingr_quantity, ingr_unit = ingredient.name,ingredient.quantity,ingredient.unit
            if (f"{ingr_name},{ingr_unit}") in ingredients:
                ingredients[f"{ingr_name},{ingr_unit}"] += ingr_quantity
            else:
                ingredients[f"{ingr_name},{ingr_unit}"] = ingr_quantity

        ans = []
        for key,value in ingredients.items():
            ingr_name, ingr_unit = key.split(",")
            ans.append(Ingredient(ingr_name,value,ingr_unit))
        return sorted(ans, key  = lambda x: x.name) #https://pythonru.com/osnovy/vse-chto-nuzhno-znat-o-lambda-funkcijah-v-python - О lambda-функции
    
    def __add__(self, other):
        combined = ShoppingList()
        combined._items = self._items + other._items
        return combined
