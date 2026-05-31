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
    def get_list(self) -> dict:
        new_dict = {}
        for item in self._items:
            ingredient = item[0]
            key = (ingredient.name, ingredient.unit)
            if not key in new_dict:
                new_dict[key] = ingredient.quantity
            else:
                new_dict[key] += ingredient.quantity
        array = []
        for item in new_dict:
            ingredient = Ingredient(item[0], new_dict[item], item[1])
            array.append(ingredient)
        array.sort(key = lambda ingredient: ingredient.name)
        
        return array
    def __add__(self, other: ShoppingList):
        arr = []
        for item in self._items:
            copy = (item[0], item[1])
            arr.append(copy)
        for item in other._items:
            copy = (item[0], item[1])
            arr.append(copy)
        return arr


class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: Ingredient) -> None:
        super(title, self.ingredients)
        self.diet_type = diet_type
    
    def scale(self, ratio: float) -> DietaryRecipe:
        ingredients = super().scale(ratio)
        diet = DietaryRecipe(self.title, self.diet_type, ingredients)
        return diet
    def __str__(self): return f"[{self.diet_type}] {self.title}"

    print()

