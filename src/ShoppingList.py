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