class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str) -> None:
        self.name = name
        self._quantity = quantity
        self.unit = unit
    @property
    def quantity(self) -> float: return self._quantity
    
    @quantity.setter
    def quantity(self, value: float) -> float:
        if value <= 0: raise ValueError("Количество должно быть положительным")
        self._quantity = value

    def __str__(self): return f"{self.name} {self.quantity} {self.unit}"
    def __repr__(self): return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Ingredient): return NotImplemented
        return self.name == other.name and self.unit == other.unit
    
ing1 = Ingredient("Мука", 500.0, "г")
ing2 = Ingredient("Мука", 203.0, "г")
print(ing1 == ing2)