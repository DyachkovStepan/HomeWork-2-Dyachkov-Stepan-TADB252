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
