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
    

class Recipe:
    def __init__(self, title: str, ingredients: Ingredient) -> None:
        self.title = title
        self.ingredients = ingredients
    def add_ingredient(self, ingredient: Ingredient) -> None:
        if ingredient in self.ingredients:
            for i in range(len(self.ingredients)):
                if self.ingredients[i] == ingredient: self.ingredients[i].quantity += ingredient.quantity
        else:
            self.ingredients.append(ingredient)
    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        if isinstance(ratio, (int,float,complex)):
            if ratio > 0: return True
        return False
    def scale(self, ratio: float) -> Recipe:
        new_recipe = Recipe(self.title, [])
        for ingredient in self.ingredients:
            new_ingredient = Ingredient(ingredient.name, ingredient.quantity * ratio, ingredient.unit)
            new_recipe.add_ingredient(new_ingredient)
        return new_recipe
    def  __len__(self): return len(self.ingredients)
    def __str__(self):
        return self.title + " Ингридиенты:" +  ", ".join(str(ingridient) for ingridient in self.ingredients)
    
class ShoppingList:
    def __init__(self, _items) -> None:
        self._items = _items
    def add_recipe(self, recipe: Recipe, portions: float) -> None:
        if portions <= 0: raise ValueError("Количество порций должно быть положительным")
        scale_recipe = recipe.scale(portions)
        for ingredient in scale_recipe.ingredients:
            self._items.append((ingredient, recipe.title))
    def remove_recipe(self,title: str):
        for elem in self._items:
            if elem[1] == title: self._items.remove(elem)
    # def get_list() доделать

    # def __add__(self, other: ShoppingList):

class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingridients: Ingredient) -> None:
        super()
        self.diet_type = diet_type
    
    #def scale(ratio: float) -> DietaryRecipe:
    #def __str__(self):
