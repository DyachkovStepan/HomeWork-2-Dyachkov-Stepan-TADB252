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